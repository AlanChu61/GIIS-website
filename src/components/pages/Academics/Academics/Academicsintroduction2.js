import React from 'react';

const AP_COURSES = [
  { code: 'AP Statistics',      icon: '∑', desc: { en: 'Data analysis & inference', zh: '數據分析與統計推論' } },
  { code: 'AP Biology',         icon: '🧬', desc: { en: 'College-level life sciences', zh: '大學程度生命科學' } },
  { code: 'AP Psychology',      icon: '🧠', desc: { en: 'Behavior & mental processes', zh: '行為與心理歷程' } },
  { code: 'AP Human Geography', icon: '🌏', desc: { en: 'Patterns of human society', zh: '人文地理與全球視野' } },
];

const PROGRAMS = [
  {
    id: 'diploma',
    icon: '🎓',
    title: { en: 'US Diploma Program', zh: '美國高中文憑課程' },
    tag: { en: '24 Credits · Florida Accredited', zh: '24 學分 · Florida 認證' },
    body: {
      en: 'GIIS follows the Florida 24-credit graduation framework — the same standard used by accredited US private high schools. Our diploma is designed to be recognized by US colleges during international student admissions review.',
      zh: 'GIIS 遵循 Florida 24 學分畢業框架，與美國認證私立高中標準一致。我們的文憑在美國大學審核國際學生申請時具備完整的學術效力。',
    },
    points: {
      en: ['English Language Arts — 4 credits', 'Mathematics — 4 credits', 'Science — 3 credits', 'Social Studies — 3 credits', 'PE & Health — 1 credit', 'Electives — 8.5 credits'],
      zh: ['英語語言藝術 — 4 學分', '數學 — 4 學分', '自然科學 — 3 學分', '社會科學 — 3 學分', '體育與健康 — 1 學分', '選修課程 — 8.5 學分'],
    },
  },
  {
    id: 'electives',
    icon: '🗂️',
    title: { en: 'Elective Concentration Tracks', zh: '選修方向規劃' },
    tag: { en: 'Tailored to College Major Goals', zh: '依申請方向量身規劃' },
    body: {
      en: 'Beyond core requirements, GIIS offers three elective concentration tracks. Students build a cohesive course history that demonstrates depth and direction — exactly what US admissions officers look for.',
      zh: '在必修科目之外，GIIS 提供三大選修方向。學生可建立一致且有深度的選課紀錄，展現出明確的學術方向——這正是美國大學申請審核最重視的要素。',
    },
    points: {
      en: ['Business & Finance — entrepreneurship, marketing, corporate finance', 'Psychology & Behavioral Science — from intro to AP & capstone', 'Communication & Research — writing, public speaking, media literacy'],
      zh: ['商業與財務 — 創業、行銷、企業財務', '心理學與行為科學 — 從入門到 AP 與研究專題', '溝通與研究方法 — 學術寫作、演說、媒體素養'],
    },
  },
];

export default function Academicsintroduction2({ language }) {
  const isEn = language !== 'zh';

  return (
    <>
      {/* ── Section 1: OUR PROGRAMS ─────────────────────────────── */}
      <div style={{ padding: '80px 0 60px', fontFamily: 'Inter, sans-serif' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%' }}>
          <h2 style={{ fontSize: '70px', fontWeight: 800, lineHeight: 1, marginBottom: '16px' }}>
            {isEn ? 'OUR' : '課程'}
          </h2>
          <h2 style={{ fontSize: '70px', fontWeight: 800, lineHeight: 1, marginBottom: '40px' }}>
            {isEn ? 'PROGRAMS' : '架構'}
          </h2>
          <p style={{ fontSize: '20px', color: '#555', maxWidth: '640px', lineHeight: 1.7, marginBottom: '56px' }}>
            {isEn
              ? 'GIIS offers a US-accredited high school diploma program built on the Florida 24-credit framework, with elective tracks designed specifically for Chinese students targeting US university admissions.'
              : 'GIIS 提供以 Florida 24 學分框架為基礎的美國認證高中文憑課程，並為目標申請美國大學的中國學生設計了專屬的選修方向。'}
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '24px' }}>
            {PROGRAMS.map((prog) => (
              <div key={prog.id} style={{
                border: '1px solid #e0e0e0',
                borderRadius: '12px',
                padding: '32px',
                background: '#fff',
                boxShadow: '0 2px 12px rgba(0,0,0,0.07)',
              }}>
                <div style={{ fontSize: '36px', marginBottom: '16px' }}>{prog.icon}</div>
                <span style={{
                  display: 'inline-block',
                  fontSize: '11px',
                  fontWeight: 700,
                  letterSpacing: '1px',
                  padding: '4px 10px',
                  borderRadius: '20px',
                  background: '#2b3d6d',
                  color: '#fff',
                  marginBottom: '12px',
                }}>
                  {prog.tag[isEn ? 'en' : 'zh']}
                </span>
                <h3 style={{ fontSize: '22px', fontWeight: 700, marginBottom: '12px', color: '#111' }}>
                  {prog.title[isEn ? 'en' : 'zh']}
                </h3>
                <p style={{ fontSize: '15px', color: '#666', lineHeight: 1.7, marginBottom: '20px' }}>
                  {prog.body[isEn ? 'en' : 'zh']}
                </p>
                <ul style={{ paddingLeft: '16px', margin: 0 }}>
                  {prog.points[isEn ? 'en' : 'zh'].map((pt) => (
                    <li key={pt} style={{ fontSize: '14px', color: '#444', marginBottom: '6px', lineHeight: 1.5 }}>
                      {pt}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* ── Section 2: AP COURSES ────────────────────────────────── */}
      <div style={{ background: '#2b3d6d', padding: '80px 0', fontFamily: 'Inter, sans-serif' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 10%' }}>
          <h2 style={{ fontSize: '60px', fontWeight: 800, color: '#fff', lineHeight: 1, marginBottom: '12px' }}>
            {isEn ? 'AP COURSES' : 'AP 進階課程'}
          </h2>
          <p style={{ fontSize: '18px', color: 'rgba(255,255,255,0.7)', maxWidth: '580px', lineHeight: 1.7, marginBottom: '48px' }}>
            {isEn
              ? 'AP (Advanced Placement) courses are college-level classes offered in high school. Strong AP performance — especially exam scores of 4 or 5 — is one of the most effective signals of academic readiness for competitive US universities.'
              : 'AP（Advanced Placement）是高中階段提供的大學程度課程。優異的 AP 成績（尤其是 4 或 5 分）是向美國頂尖大學展示學術能力最有效的指標之一。'}
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px' }}>
            {AP_COURSES.map((ap) => (
              <div key={ap.code} style={{
                background: 'rgba(255,255,255,0.08)',
                border: '1px solid rgba(255,255,255,0.15)',
                borderRadius: '10px',
                padding: '28px 24px',
                borderTop: '4px solid rgba(213,168,54,1)',
              }}>
                <div style={{ fontSize: '32px', marginBottom: '12px' }}>{ap.icon}</div>
                <h4 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', marginBottom: '8px' }}>{ap.code}</h4>
                <p style={{ fontSize: '14px', color: 'rgba(255,255,255,0.6)', margin: 0, lineHeight: 1.5 }}>
                  {ap.desc[isEn ? 'en' : 'zh']}
                </p>
              </div>
            ))}
          </div>

          <p style={{ fontSize: '13px', color: 'rgba(255,255,255,0.45)', marginTop: '32px' }}>
            {isEn
              ? 'AP exams are administered by the College Board each May. GIIS prepares students throughout the year with coursework aligned to the official AP curriculum framework.'
              : 'AP 考試由 College Board 每年五月舉辦。GIIS 全年以對應官方 AP 課綱的課程為學生備考。'}
          </p>
        </div>
      </div>
    </>
  );
}
