import React from 'react';
import { Helmet } from 'react-helmet-async';
import Nav from '../Homepage/HomepageHeader/Nav.js';
import heroImg from '../../../img/Homepage/homepage3.png';

const SCHOOL_PHONE = '+1 (813) 501-5756';
const SCHOOL_EMAIL = 'admissions@genesisideas.school';

const STEPS = [
  {
    num: '01',
    title: { en: 'Submit Inquiry', zh: '提交申請意向' },
    body: {
      en: 'Contact our admissions office by email or phone to express your interest and receive an application packet.',
      zh: '透過電子郵件或電話聯繫招生辦公室，表達入學意向並索取申請資料。',
    },
  },
  {
    num: '02',
    title: { en: 'Provide Documents', zh: '提交申請文件' },
    body: {
      en: 'Submit academic records, transcripts from previous schools, and any required supporting materials.',
      zh: '提交過往學校的成績單、在籍證明及其他所需輔助文件。',
    },
  },
  {
    num: '03',
    title: { en: 'Interview & Assessment', zh: '面談與學力評估' },
    body: {
      en: 'Complete a brief interview or placement discussion so we can design the right academic path for you.',
      zh: '進行簡短的面談或學力評估，讓我們為你規劃最合適的學習方向。',
    },
  },
  {
    num: '04',
    title: { en: 'Enrollment', zh: '完成入學' },
    body: {
      en: 'Receive your admissions decision and enrollment instructions. Welcome to GIIS!',
      zh: '收到錄取結果與入學指引，正式成為 GIIS 的一員！',
    },
  },
];

const REQUIREMENTS = [
  { icon: '📄', label: { en: 'Previous academic transcripts', zh: '過往成績單' } },
  { icon: '🎂', label: { en: 'Proof of age / birth certificate', zh: '出生證明文件' } },
  { icon: '✍️', label: { en: 'Completed application form', zh: '填妥的申請表' } },
  { icon: '💬', label: { en: 'Brief personal statement (optional)', zh: '個人陳述（選填）' } },
];

export default function AdmissionMain({ language, toggleLanguage }) {
  const isEn = language !== 'zh';

  return (
    <>
      <Helmet>
        <title>{isEn ? 'Admission' : '入學申請'} | Genesis of Ideas International School</title>
        <meta
          name="description"
          content={isEn
            ? 'How to apply to Genesis of Ideas International School — process, requirements, and contact.'
            : '創思國際學校入學申請流程、所需文件與聯絡方式。'}
        />
      </Helmet>

      {/* Nav */}
      <div className="row">
        <Nav language={language} toggleLanguage={toggleLanguage} />
      </div>

      {/* Hero */}
      <div style={{ position: 'relative', width: '100%' }}>
        <img src={heroImg} alt="Admission" style={{ width: '100%', height: '400px', objectFit: 'cover', display: 'block' }} />
        <div style={{
          position: 'absolute', bottom: 0, left: 0, right: 0,
          background: 'linear-gradient(to top, rgba(0,0,0,0.75) 0%, transparent 100%)',
          padding: '48px 10%',
        }}>
          <h1 style={{ color: '#fff', fontFamily: 'Inter, sans-serif', fontWeight: 800, fontSize: '56px', margin: 0, lineHeight: 1 }}>
            {isEn ? 'ADMISSION' : '入學申請'}
          </h1>
          <p style={{ color: 'rgba(255,255,255,0.8)', fontFamily: 'Inter, sans-serif', fontSize: '18px', marginTop: '12px', maxWidth: '540px' }}>
            {isEn
              ? 'Start your journey at Genesis of Ideas International School.'
              : '開始你在創思國際學校的學習旅程。'}
          </p>
        </div>
      </div>

      {/* Step-by-step process */}
      <div style={{ background: 'rgba(43,61,109,1)', padding: '80px 0', borderBottom: '8px solid rgba(213,168,54,1)' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%', fontFamily: 'Inter, sans-serif' }}>
          <h2 style={{ color: '#fff', fontSize: '56px', fontWeight: 800, lineHeight: 1, marginBottom: '48px' }}>
            {isEn ? 'HOW TO APPLY' : '申請流程'}
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '24px' }}>
            {STEPS.map((s) => (
              <div key={s.num} style={{
                background: 'rgba(255,255,255,0.07)',
                border: '1px solid rgba(255,255,255,0.12)',
                borderTop: '4px solid rgba(213,168,54,1)',
                borderRadius: '10px',
                padding: '28px 24px',
              }}>
                <div style={{ fontSize: '40px', fontWeight: 800, color: 'rgba(213,168,54,0.6)', lineHeight: 1, marginBottom: '16px' }}>
                  {s.num}
                </div>
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

      {/* Requirements */}
      <div style={{ background: '#fff', padding: '80px 0' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%', fontFamily: 'Inter, sans-serif' }}>
          <h2 style={{ fontSize: '48px', fontWeight: 800, lineHeight: 1, marginBottom: '12px' }}>
            {isEn ? 'WHAT YOU' : '申請'}
          </h2>
          <h2 style={{ fontSize: '48px', fontWeight: 800, lineHeight: 1, marginBottom: '40px' }}>
            {isEn ? "NEED TO PREPARE" : '所需文件'}
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px', marginBottom: '48px' }}>
            {REQUIREMENTS.map((r) => (
              <div key={r.label.en} style={{
                display: 'flex', alignItems: 'flex-start', gap: '16px',
                padding: '20px 24px',
                border: '1px solid #e8e8e8',
                borderRadius: '8px',
                background: '#fafafa',
              }}>
                <span style={{ fontSize: '28px', flexShrink: 0 }}>{r.icon}</span>
                <span style={{ fontSize: '15px', color: '#333', fontWeight: 500, lineHeight: 1.5 }}>
                  {r.label[isEn ? 'en' : 'zh']}
                </span>
              </div>
            ))}
          </div>
          <p style={{ fontSize: '14px', color: '#888', maxWidth: '600px', lineHeight: 1.7 }}>
            {isEn
              ? '* Requirements and deadlines may vary each term. Please contact our admissions office to confirm current requirements before applying.'
              : '* 各學期的要求與截止日期可能有所調整。申請前請聯繫招生辦公室確認最新資訊。'}
          </p>
        </div>
      </div>

      {/* Contact */}
      <div style={{ background: '#f4f6fa', padding: '60px 0' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%', fontFamily: 'Inter, sans-serif' }}>
          <h2 style={{ fontSize: '36px', fontWeight: 800, marginBottom: '32px' }}>
            {isEn ? 'Contact Admissions' : '聯絡招生辦公室'}
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
