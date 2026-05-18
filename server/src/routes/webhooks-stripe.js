const express = require('express');
const router = express.Router();
const Stripe = require('stripe');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();
const stripe = process.env.STRIPE_SECRET_KEY ? Stripe(process.env.STRIPE_SECRET_KEY) : null;

/**
 * POST /api/webhooks/stripe
 *
 * IMPORTANT: index.js mounts this route with `express.raw()` so req.body is a Buffer.
 * Do NOT use express.json() before this route — Stripe signature verification needs raw bytes.
 *
 * Events we handle:
 *   checkout.session.completed        → upsert Subscription with status from Stripe
 *   customer.subscription.updated     → refresh status, currentPeriodEnd, cancelAtPeriodEnd
 *   customer.subscription.deleted     → status = 'cancelled'
 *   invoice.payment_failed            → status = 'past_due'
 *
 * In dev, STRIPE_WEBHOOK_SECRET may be empty; we skip signature verification and parse
 * raw body directly. NEVER do this in production — Stripe explicitly warns about it.
 */
router.post('/', async (req, res) => {
  if (!stripe) return res.status(500).send('Stripe not configured.');

  const sig = req.headers['stripe-signature'];
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let event;
  try {
    if (webhookSecret && sig) {
      event = stripe.webhooks.constructEvent(req.body, sig, webhookSecret);
    } else {
      event = JSON.parse(req.body.toString());
      console.warn('[webhook] No STRIPE_WEBHOOK_SECRET — skipping signature verification (DEV ONLY)');
    }
  } catch (err) {
    console.error('[webhook] Signature verification failed:', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  try {
    switch (event.type) {
      case 'checkout.session.completed':
        await handleCheckoutCompleted(event.data.object);
        break;
      case 'customer.subscription.updated':
        await handleSubscriptionUpdated(event.data.object);
        break;
      case 'customer.subscription.deleted':
        await handleSubscriptionDeleted(event.data.object);
        break;
      case 'invoice.payment_failed':
        await handlePaymentFailed(event.data.object);
        break;
      default:
        // Unhandled event types still return 200 so Stripe stops retrying.
        console.log(`[webhook] Unhandled event type: ${event.type}`);
    }
  } catch (handlerErr) {
    // Returning 500 makes Stripe retry up to 3 days. Only do this for transient errors;
    // for permanent failures (bad data), log and return 200 so we don't get stuck.
    console.error('[webhook] Handler error:', handlerErr.message, handlerErr.stack);
    return res.status(500).json({ error: 'Webhook handler failed.' });
  }

  res.json({ received: true });
});

// ─── Event handlers ───────────────────────────────────────────────────────────

async function handleCheckoutCompleted(session) {
  const planType = session.metadata?.planType || 'unknown';
  const maxStudents = Number(session.metadata?.maxStudents || 1);

  // For subscription mode the status comes from the subscription itself.
  // For one-time payment mode there's no Subscription on Stripe's side; we record as 'paid'.
  const isSubscription = session.mode === 'subscription';
  let status = 'incomplete';
  let currentPeriodEnd = null;
  let stripeSubscriptionId = null;
  let stripePriceId = null;

  if (isSubscription && session.subscription) {
    const sub = await stripe.subscriptions.retrieve(session.subscription);
    status = sub.status;  // 'active' | 'trialing' | 'past_due' | etc.
    currentPeriodEnd = new Date(sub.current_period_end * 1000);
    stripeSubscriptionId = sub.id;
    stripePriceId = sub.items?.data?.[0]?.price?.id || null;
  } else {
    // one-time payment (e.g. live_test)
    status = session.payment_status === 'paid' ? 'paid' : 'incomplete';
    stripePriceId = session.line_items?.data?.[0]?.price?.id || null;
  }

  await prisma.subscription.upsert({
    where: { stripeCheckoutSessionId: session.id },
    update: {
      status,
      currentPeriodEnd,
      stripeCustomerId:     session.customer,
      stripeSubscriptionId,
      stripePriceId,
      amountTotal:          session.amount_total,
    },
    create: {
      purchaserEmail:          session.customer_email || session.customer_details?.email || 'unknown',
      stripeCustomerId:        session.customer,
      stripeSubscriptionId,
      stripePriceId,
      stripeCheckoutSessionId: session.id,
      planType,
      maxStudents,
      status,
      currentPeriodEnd,
      amountTotal:             session.amount_total,
    },
  });

  console.log(`[webhook] ✓ checkout.session.completed — ${planType} · ${session.customer_email} · ${status}`);

  // TODO (next): create Student / ParentAccount automatically, send welcome email via Resend.
}

async function handleSubscriptionUpdated(sub) {
  const existing = await prisma.subscription.findUnique({
    where: { stripeSubscriptionId: sub.id },
  });
  if (!existing) {
    // Stripe may send subscription.updated before checkout.session.completed in rare cases.
    // We'll catch it next time around or via re-sync.
    console.warn(`[webhook] subscription.updated for unknown sub ${sub.id} — skipping`);
    return;
  }
  await prisma.subscription.update({
    where: { stripeSubscriptionId: sub.id },
    data: {
      status:             sub.status,
      currentPeriodEnd:   new Date(sub.current_period_end * 1000),
      cancelAtPeriodEnd:  !!sub.cancel_at_period_end,
      stripePriceId:      sub.items?.data?.[0]?.price?.id || existing.stripePriceId,
    },
  });
  console.log(`[webhook] ✓ subscription.updated — ${sub.id} · ${sub.status}`);
}

async function handleSubscriptionDeleted(sub) {
  const existing = await prisma.subscription.findUnique({
    where: { stripeSubscriptionId: sub.id },
  });
  if (!existing) return;
  await prisma.subscription.update({
    where: { stripeSubscriptionId: sub.id },
    data: { status: 'cancelled', cancelAtPeriodEnd: false },
  });
  console.log(`[webhook] ✓ subscription.deleted — ${sub.id}`);
}

async function handlePaymentFailed(invoice) {
  if (!invoice.subscription) return;
  const existing = await prisma.subscription.findUnique({
    where: { stripeSubscriptionId: invoice.subscription },
  });
  if (!existing) return;
  await prisma.subscription.update({
    where: { stripeSubscriptionId: invoice.subscription },
    data: { status: 'past_due' },
  });
  console.log(`[webhook] ⚠ payment_failed — ${invoice.subscription}`);
}

module.exports = router;
