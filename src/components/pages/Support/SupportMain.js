import React from 'react';
import { Helmet } from 'react-helmet-async';
import Nav from '../Homepage/HomepageHeader/Nav.js';
import heroImg from '../../../img/Homepage/homepage5.png';

const SCHOOL_PHONE = '+1 (813) 501-5756';
const SCHOOL_EMAIL = 'support@genesisideas.school';
const MOODLE_URL = 'https://moodles.genesisideas.school/';

const SERVICES = [
  {
    icon: '📚',
    title: { en: 'Academic Advising', zh: '學業輔導' },
    body: {
      en: 'Our advisors work with each student to design a personalized course plan aligned with their college major goals and graduation requirements.',
      zh: '我們的輔導師與每位學生合作，依據其大學申請目標與畢業要求，量身規劃個人化選課計畫。',
    },
  },
  {
    icon: '🎯',
    title: { en: 'College Application Guidance', zh: '大學申請指導' },
    body: {
      en: 'We support students through the US college application process — including course selection strategy, timeline planning, and application review.',
      zh: '我們協助學生完成美國大學申請的每個環節，包含選課策略、時程規劃與申請文件審閱。',
    },
  },
  {
    icon: '💬',
    title: { en: 'Progress Check-ins', zh: '學習進度追蹤' },
    body: {
      en: 'Regular one-on-one check-ins help students stay on track, address challenges early, and maintain momentum throughout the school year.',
      zh: '定期一對一的進度確認，幫助學生保持學習節奏、提早發現問題，讓整個學年都能穩健前進。',
    },
  },
  {
    icon: '🧘',
    title: { en: 'Wellbeing & Life Counseling', zh: '身心健康與生活輔導' },
    body: {
      en: 'Online learning can be challenging. Our counselors provide emotional support and connect students with wellness resources when needed.',
      zh: '線上學習有時不易堅持。輔導老師提供情緒支持，並在需要時為學生媒合身心健康相關資源。',
    },
  },
  {
    icon: '🛠️',
    title: { en: 'Technical & Platform Support', zh: '技術與平台協助' },
    body: {
      en: 'Get help with Moodle access, coursework submission, or any technical issues — so nothing gets in the way of your learning.',
      zh: '協助解決 Moodle 登入、作業繳交或任何技術問題，確保學習不受阻礙。',
    },
  },
  {
    icon: '📖',
    title: { en: 'Study Skills & Resources', zh: '學習方法與資源' },
    body: {
      en: 'We share strategies for time management, academic writing, research, and exam preparation tailored to an online learning environment.',
      zh: '提供適合線上學習的時間管理、學術寫作、研究方法與考試準備技巧與資源。',
    },
  },
];

export default function SupportMain({ language, toggleLanguage }) {
  const isEn = language !== 'zh';

  return (
    <>
      <Helmet>
        <title>{isEn ? 'Student Support' : '學生支持'} | Genesis of Ideas International School</title>
        <meta
          name="description"
          content={isEn
            ? 'Student support services at Genesis of Ideas International School — advising, counseling, and academic resources.'
            : '創思國際學校學生支持服務：學業輔導、身心健康諮詢與資源說明。'}
        />
      </Helmet>

      {/* Nav */}
      <div className="row">
        <Nav language={language} toggleLanguage={toggleLanguage} />
      </div>

      {/* Hero */}
      <div style={{ position: 'relative', width: '100%' }}>
        <img src={heroImg} alt="Student Support" style={{ width: '100%', height: '400px', objectFit: 'cover', display: 'block' }} />
        <div style={{
          position: 'absolute', bottom: 0, left: 0, right: 0,
          background: 'linear-gradient(to top, rgba(0,0,0,0.75) 0%, transparent 100%)',
          padding: '48px 10%',
        }}>
          <h1 style={{ color: '#fff', fontFamily: 'Inter, sans-serif', fontWeight: 800, fontSize: '56px', margin: 0, lineHeight: 1 }}>
            {isEn ? 'STUDENT SUPPORT' : '學生支持'}
          </h1>
          <p style={{ color: 'rgba(255,255,255,0.8)', fontFamily: 'Inter, sans-serif', fontSize: '18px', marginTop: '12px', maxWidth: '540px' }}>
            {isEn
              ? 'We are with you every step of the way — academically and personally.'
              : '無論是學業還是生活，我們始終陪伴在你身旁。'}
          </p>
        </div>
      </div>

      {/* Services grid */}
      <div style={{ background: 'rgba(43,61,109,1)', padding: '80px 0', borderBottom: '8px solid rgba(213,168,54,1)' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%', fontFamily: 'Inter, sans-serif' }}>
          <h2 style={{ color: '#fff', fontSize: '56px', fontWeight: 800, lineHeight: 1, marginBottom: '12px' }}>
            {isEn ? 'HOW WE' : '我們提供'}
          </h2>
          <h2 style={{ color: '#fff', fontSize: '56px', fontWeight: 800, lineHeight: 1, marginBottom: '48px' }}>
            {isEn ? 'SUPPORT YOU' : '哪些支持'}
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '20px' }}>
            {SERVICES.map((s) => (
              <div key={s.title.en} style={{
                background: 'rgba(255,255,255,0.07)',
                border: '1px solid rgba(255,255,255,0.12)',
                borderTop: '4px solid rgba(213,168,54,1)',
                borderRadius: '10px',
                padding: '28px 24px',
              }}>
                <div style={{ fontSize: '32px', marginBottom: '14px' }}>{s.icon}</div>
                <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', marginBottom: '10px' }}>
                  {s.title[isEn ? 'en' : 'zh']}
                </h3>
                <p style={{ fontSize: '14px', color: 'rgba(255,255,255,0.65)', lineHeight: 1.7, margin: 0 }}>
                  {s.body[isEn ? 'en' : 'zh']}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Moodle callout */}
      <div style={{ background: '#fff', padding: '60px 0' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%', fontFamily: 'Inter, sans-serif' }}>
          <div style={{
            display: 'flex', alignItems: 'center', gap: '32px', flexWrap: 'wrap',
            background: '#f4f6fa', borderRadius: '12px', padding: '36px 40px',
            borderLeft: '6px solid rgba(43,61,109,1)',
          }}>
            <div style={{ flex: 1, minWidth: '200px' }}>
              <h3 style={{ fontSize: '24px', fontWeight: 700, marginBottom: '8px' }}>
                {isEn ? 'Learning Platform — Moodle' : '學習平台 — Moodle'}
              </h3>
              <p style={{ fontSize: '15px', color: '#555', lineHeight: 1.7, margin: 0 }}>
                {isEn
                  ? 'All coursework, assignments, and teacher communication happen through Moodle. Log in with the credentials provided at enrollment.'
                  : '所有課程內容、作業繳交及師生溝通皆透過 Moodle 進行。請使用入學時提供的帳號登入。'}
              </p>
            </div>
            <a
              href={MOODLE_URL}
              target="_blank"
              rel="noopener noreferrer"
              style={{
                flexShrink: 0,
                background: 'rgba(43,61,109,1)',
                color: '#fff',
                padding: '14px 28px',
                borderRadius: '6px',
                fontWeight: 700,
                fontSize: '15px',
                textDecoration: 'none',
              }}
            >
              {isEn ? 'Go to Moodle →' : '前往 Moodle →'}
            </a>
          </div>
        </div>
      </div>

      {/* Contact */}
      <div style={{ background: '#f4f6fa', padding: '60px 0' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%', fontFamily: 'Inter, sans-serif' }}>
          <h2 style={{ fontSize: '36px', fontWeight: 800, marginBottom: '32px' }}>
            {isEn ? 'Get in Touch' : '聯絡我們'}
          </h2>
          <div style={{ display: 'flex', gap: '32px', flexWrap: 'wrap' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <span style={{ fontSize: '24px' }}>📞</span>
              <div>
                <div style={{ fontSize: '12px', color: '#888', fontWeight: 600, letterSpacing: '1px', textTransform: 'uppercase' }}>{isEn ? 'Phone' : '電話'}</div>
                <a href={`tel:${SCHOOL_PHONE.replace(/\s/g,'')}`} style={{ fontSize: '17px', fontWeight: 600, color: '#2b3d6d', textDecoration: 'none' }}>{SCHOOL_PHONE}</a>
              </div>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <span style={{ fontSize: '24px' }}>✉️</span>
              <div>
                <div style={{ fontSize: '12px', color: '#888', fontWeight: 600, letterSpacing: '1px', textTransform: 'uppercase' }}>{isEn ? 'Email' : '電子郵件'}</div>
                <a href={`mailto:${SCHOOL_EMAIL}`} style={{ fontSize: '17px', fontWeight: 600, color: '#2b3d6d', textDecoration: 'none' }}>{SCHOOL_EMAIL}</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
