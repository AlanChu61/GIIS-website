import { Navigate } from 'react-router-dom';

/** Bookmarks to /admin/login land on the unified student portal (admin uses same form). */
export default function AdminLogin() {
  return <Navigate to="/login" replace />;
}
