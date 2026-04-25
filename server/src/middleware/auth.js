const jwt = require('jsonwebtoken');

function extractToken(req) {
  // Cookie takes priority over Authorization header
  const cookieToken = req.cookies?.giis_jwt;
  if (cookieToken) return cookieToken;
  const header = req.headers.authorization || '';
  return header.startsWith('Bearer ') ? header.slice(7) : null;
}

/**
 * Verifies JWT from cookie (primary) or Authorization header (fallback).
 * Sets req.auth on success.
 */
function authenticate(req, res, next) {
  const token = extractToken(req);
  if (!token) {
    return res.status(401).json({ error: 'Not authenticated' });
  }
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET);
    if (payload.role === 'student' && payload.studentId) {
      req.auth = { role: 'student', studentId: payload.studentId, email: payload.email };
      return next();
    }
    if (payload.role === 'admin' && payload.adminId) {
      req.auth = { role: 'admin', adminId: payload.adminId, email: payload.email };
      req.admin = { id: payload.adminId, email: payload.email };
      return next();
    }
    // Legacy admin JWT (adminId only)
    if (payload.adminId) {
      req.auth = { role: 'admin', adminId: payload.adminId, email: payload.email };
      req.admin = { id: payload.adminId, email: payload.email };
      return next();
    }
    return res.status(401).json({ error: 'Invalid token' });
  } catch {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
}

function requireAdmin(req, res, next) {
  if (req.auth?.role !== 'admin') {
    return res.status(403).json({ error: 'Admin only' });
  }
  next();
}

function requireStudentOrAdminForStudentParam(req, res, next) {
  const sid = req.params.id;
  if (req.auth?.role === 'admin') return next();
  if (req.auth?.role === 'student' && req.auth.studentId === sid) return next();
  return res.status(403).json({ error: 'Forbidden' });
}

/** @deprecated Use authenticate */
const requireAuth = authenticate;

module.exports = { authenticate, requireAuth, requireAdmin, requireStudentOrAdminForStudentParam };
