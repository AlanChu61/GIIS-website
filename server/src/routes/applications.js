const express = require('express');
const { PrismaClient } = require('@prisma/client');
const { authenticate, requireAdmin } = require('../middleware/auth');

const prisma = new PrismaClient();
const router = express.Router();

// POST /api/applications  — public, no auth required
router.post('/', async (req, res) => {
  const { studentName, dob, gradeLevel, parentName, parentEmail, phone, notes } = req.body || {};
  const missing = [];
  if (!studentName?.trim()) missing.push('studentName');
  if (!dob?.trim()) missing.push('dob');
  if (!gradeLevel?.trim()) missing.push('gradeLevel');
  if (!parentName?.trim()) missing.push('parentName');
  if (!parentEmail?.trim()) missing.push('parentEmail');
  if (missing.length) return res.status(400).json({ error: `Missing fields: ${missing.join(', ')}` });

  const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRe.test(parentEmail.trim())) return res.status(400).json({ error: 'Invalid parent email' });

  const app = await prisma.application.create({
    data: {
      studentName: studentName.trim(),
      dob: dob.trim(),
      gradeLevel: gradeLevel.trim(),
      parentName: parentName.trim(),
      parentEmail: parentEmail.trim().toLowerCase(),
      phone: (phone || '').trim(),
      notes: (notes || '').trim(),
    },
  });

  // TODO: send confirmation email to parentEmail + admin notification (Resend Phase 1)

  res.status(201).json({ ok: true, id: app.id });
});

// GET /api/applications  — admin only
router.get('/', authenticate, requireAdmin, async (req, res) => {
  const status = req.query.status; // pending | approved | rejected | undefined (all)
  const where = status ? { status } : {};
  const apps = await prisma.application.findMany({
    where,
    orderBy: { createdAt: 'desc' },
    take: 200,
  });
  res.json(apps);
});

// PATCH /api/applications/:id  — approve or reject
router.patch('/:id', authenticate, requireAdmin, async (req, res) => {
  const { status } = req.body || {};
  if (!['approved', 'rejected', 'pending'].includes(status)) {
    return res.status(400).json({ error: 'status must be approved | rejected | pending' });
  }
  const app = await prisma.application.update({
    where: { id: req.params.id },
    data: { status, reviewedAt: new Date(), reviewedById: req.auth.adminId },
  });
  // TODO: on approve, send Stripe checkout link to parentEmail (Phase 2)
  res.json({ ok: true, id: app.id, status: app.status });
});

module.exports = router;
