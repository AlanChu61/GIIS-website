const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();
const router = express.Router();

const COOKIE_NAME = 'giis_parent_jwt';
const COOKIE_MAX_AGE_MS = 7 * 24 * 60 * 60 * 1000;

function setCookieOptions() {
  const isProd = process.env.NODE_ENV === 'production' || process.env.TRUST_PROXY === '1';
  return { httpOnly: true, sameSite: isProd ? 'none' : 'lax', secure: isProd, maxAge: COOKIE_MAX_AGE_MS, path: '/' };
}

function signParentToken(account) {
  return jwt.sign(
    { role: 'parent', parentId: account.id, email: account.email, studentId: account.studentId },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );
}

// POST /api/parent/login
router.post('/login', async (req, res) => {
  const { email, password } = req.body || {};
  if (!email || !password) return res.status(400).json({ error: 'email and password required' });

  const account = await prisma.parentAccount.findUnique({ where: { email: email.trim().toLowerCase() } });
  if (!account) return res.status(401).json({ error: 'Invalid email or password' });

  const ok = await bcrypt.compare(password, account.passwordHash);
  if (!ok) return res.status(401).json({ error: 'Invalid email or password' });

  await prisma.parentAccount.update({ where: { id: account.id }, data: { lastLoginAt: new Date() } });

  const token = signParentToken(account);
  res.cookie(COOKIE_NAME, token, setCookieOptions());
  res.json({ ok: true, studentId: account.studentId });
});

// POST /api/parent/logout
router.post('/logout', (_req, res) => {
  res.clearCookie(COOKIE_NAME, { path: '/' });
  res.json({ ok: true });
});

// POST /api/parent/setup  — admin creates parent account (or resets password)
// Body: { studentId, email, password }
// Protected: admin only (checked via JWT role)
router.post('/setup', async (req, res) => {
  const authHeader = req.headers.authorization || '';
  const token = req.cookies?.giis_jwt || (authHeader.startsWith('Bearer ') ? authHeader.slice(7) : null);
  if (!token) return res.status(401).json({ error: 'Not authenticated' });

  let payload;
  try { payload = jwt.verify(token, process.env.JWT_SECRET); } catch { return res.status(401).json({ error: 'Invalid token' }); }
  if (payload.role !== 'admin') return res.status(403).json({ error: 'Admin only' });

  const { studentId, email, password } = req.body || {};
  if (!studentId || !email || !password) return res.status(400).json({ error: 'studentId, email, password required' });
  if (password.length < 8) return res.status(400).json({ error: 'Password must be at least 8 characters' });

  const student = await prisma.student.findUnique({ where: { id: studentId } });
  if (!student) return res.status(404).json({ error: 'Student not found' });

  const passwordHash = await bcrypt.hash(password, 12);
  const account = await prisma.parentAccount.upsert({
    where: { email: email.trim().toLowerCase() },
    update: { passwordHash, studentId },
    create: { email: email.trim().toLowerCase(), passwordHash, studentId },
  });

  res.json({ ok: true, id: account.id });
});

module.exports = router;
