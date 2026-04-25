import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

/** Scrolls to top on client-side navigation (SPA). */
export default function ScrollToTop() {
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  return null;
}
