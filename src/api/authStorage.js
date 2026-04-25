// JWT is now stored in an HttpOnly cookie managed by the server.
// This module only stores non-sensitive session info (id, email, name) for UI display.

const ADMIN_SESSION_KEY = 'giis_admin_session';
const STUDENT_TOKEN_KEY = 'giis_student_token';
const STUDENT_INFO_KEY = 'giis_student_info';

// ── Admin ────────────────────────────────────────────────────────────────────

export function getAdminSession() {
  try {
    const raw = sessionStorage.getItem(ADMIN_SESSION_KEY);
    if (!raw) return null;
    const s = JSON.parse(raw);
    return s?.id ? s : null;
  } catch {
    return null;
  }
}

export function setAdminSession(admin) {
  try {
    if (admin?.id) {
      sessionStorage.setItem(ADMIN_SESSION_KEY, JSON.stringify({ id: admin.id, email: admin.email || '' }));
    } else {
      sessionStorage.removeItem(ADMIN_SESSION_KEY);
    }
  } catch {
    /* ignore */
  }
}

export function clearAdminSession() {
  try { sessionStorage.removeItem(ADMIN_SESSION_KEY); } catch { /* ignore */ }
}

// ── Backward-compat aliases (some pages still call getAdminToken / clearAdminToken) ──

export function getAdminToken() {
  // Legacy: return a non-null truthy value if an admin session exists (cookie carries the real JWT)
  return getAdminSession() ? '__cookie__' : null;
}

export function setAdminToken(_token) {
  // no-op: token is managed by the server cookie
}

export function clearAdminToken() {
  clearAdminSession();
}

// ── Student ──────────────────────────────────────────────────────────────────

/** @returns {{ token: string, student: { id: string, email: string, name?: string } } | null} */
export function getStudentSession() {
  try {
    // Keep reading legacy token key for backward compat (token value still in localStorage during migration window)
    const token = localStorage.getItem(STUDENT_TOKEN_KEY) || '__cookie__';
    const raw = localStorage.getItem(STUDENT_INFO_KEY);
    if (!raw) return null;
    const student = JSON.parse(raw);
    if (!student?.id) return null;
    return { token, student };
  } catch {
    return null;
  }
}

export function setStudentSession(token, student) {
  try {
    if (student?.id) {
      // Store token for backward compat; cookie is the real auth mechanism
      if (token && token !== '__cookie__') localStorage.setItem(STUDENT_TOKEN_KEY, token);
      localStorage.setItem(
        STUDENT_INFO_KEY,
        JSON.stringify({ id: student.id, email: student.email || '', name: student.name || '' })
      );
    } else {
      clearStudentSession();
    }
  } catch {
    /* ignore */
  }
}

export function clearStudentSession() {
  try {
    localStorage.removeItem(STUDENT_TOKEN_KEY);
    localStorage.removeItem(STUDENT_INFO_KEY);
  } catch {
    /* ignore */
  }
}
