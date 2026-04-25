import React, { useState, useEffect, Suspense, lazy } from 'react';
import { Routes, Route, Navigate, useLocation } from 'react-router-dom';
import Footer from './components/Footer/Footer';
import Header from './components/Header/Header';
import ScrollToTop from './components/ScrollToTop';
import SocialMetaDefaults from './seo/SocialMetaDefaults';
import ErrorBoundary from './components/ErrorBoundary';

const Homepage = lazy(() => import('./components/pages/Homepage/HomepageMain'));
const Discovery = lazy(() => import('./components/pages/Discovery/DiscoveryMain'));
const Academics = lazy(() => import('./components/pages/Academics/AcademicsMain'));
const Admission = lazy(() => import('./components/pages/Admission/AdmissionMain'));
const Support = lazy(() => import('./components/pages/Support/SupportMain'));
const Transcript = lazy(() => import('./components/pages/Transcript/TranscriptMain'));
const LoginPortal = lazy(() => import('./components/pages/Auth/LoginPortal'));
const AdminLogin = lazy(() => import('./components/pages/Admin/AdminLogin'));
const AdminDashboard = lazy(() => import('./components/pages/Admin/AdminDashboard'));
const AdminTranscriptPage = lazy(() => import('./components/pages/Admin/AdminTranscriptPage'));
const NotFound = lazy(() => import('./components/pages/NotFound'));
const PrivacyPolicy = lazy(() => import('./components/pages/PrivacyPolicy'));
const TermsOfUse = lazy(() => import('./components/pages/TermsOfUse'));

const LANGUAGE_STORAGE_KEY = 'giis-language';

function readInitialLanguage() {
  try {
    const saved = localStorage.getItem(LANGUAGE_STORAGE_KEY);
    if (saved === 'en' || saved === 'zh') {
      return saved;
    }
  } catch {
    /* ignore */
  }
  const browserLanguage = navigator.language || navigator.userLanguage;
  return browserLanguage && browserLanguage.includes('zh') ? 'zh' : 'en';
}

function RouteFallback() {
  return (
    <div className="py-5 text-center text-muted" role="status">
      Loading…
    </div>
  );
}

function App() {
  const [language, setLanguage] = useState(readInitialLanguage);

  useEffect(() => {
    document.documentElement.lang = language === 'en' ? 'en' : 'zh';
  }, [language]);

  useEffect(() => {
    try {
      localStorage.setItem(LANGUAGE_STORAGE_KEY, language);
    } catch {
      /* ignore */
    }
  }, [language]);

  const toggleLanguage = () => {
    setLanguage((prevLanguage) => (prevLanguage === 'en' ? 'zh' : 'en'));
  };

  const location = useLocation();
  const isTranscript = location.pathname === '/transcript';
  const isAdmin = location.pathname.startsWith('/admin');
  const hideChrome = isTranscript || isAdmin;

  return (
     <>
      <SocialMetaDefaults />
      <ScrollToTop />
      {!hideChrome && <Header language={language} toggleLanguage={toggleLanguage} />}
      <main className="container-fluid">
       <ErrorBoundary>
       <Suspense fallback={<RouteFallback />}>
       <Routes>
         <Route path="/" element={<Homepage language={language} toggleLanguage={toggleLanguage} />} />
         <Route path="/discovery" element={<Discovery language={language} toggleLanguage={toggleLanguage}  />} />
         <Route path="/academics" element={<Academics language={language}/>} />
         <Route path="/admission" element={<Admission language={language} />} />
         <Route path="/support" element={<Support language={language} />} />
         <Route path="/transcript" element={<Transcript language={language}/>}/>
         <Route path="/login" element={<LoginPortal language={language} />} />
         <Route path="/register" element={<Navigate to="/login?tab=register" replace />} />
         <Route path="/admin/login" element={<AdminLogin />} />
         <Route path="/admin" element={<AdminDashboard language={language} />} />
         <Route path="/admin/transcript/:studentId" element={<AdminTranscriptPage language={language} />} />
         <Route path="/privacy" element={<PrivacyPolicy language={language} />} />
         <Route path="/terms" element={<TermsOfUse language={language} />} />
         <Route path="*" element={<NotFound language={language} />} />
       </Routes>
       </Suspense>
       </ErrorBoundary>
      </main>
      {!hideChrome && <Footer language={language} />}
     </>
  );
}

export default App;
