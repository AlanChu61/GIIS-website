import React, { useState } from 'react';

const DEPARTMENTS = [
  {
    id: 'english',
    label: { en: 'English Language Arts', zh: '英文語言藝術' },
    color: '#2b3d6d',
    courses: [
      { name: 'English I', type: 'Core', credits: '1.0', grades: '9' },
      { name: 'English I - Writing', type: 'Core', credits: '1.0', grades: '9' },
      { name: 'English II', type: 'Core', credits: '1.0', grades: '10' },
      { name: 'English II - Literature', type: 'Core', credits: '1.0', grades: '10' },
      { name: 'English III', type: 'Core', credits: '1.0', grades: '11' },
      { name: 'English III - Literature', type: 'Core', credits: '1.0', grades: '11' },
      { name: 'English IV - Writing & Communication', type: 'Core', credits: '1.0', grades: '12' },
      { name: 'English IV - Advanced Composition', type: 'Core', credits: '1.0', grades: '12' },
    ],
  },
  {
    id: 'math',
    label: { en: 'Mathematics', zh: '數學' },
    color: '#d5a836',
    courses: [
      { name: 'Algebra I', type: 'Core', credits: '1.0', grades: '9' },
      { name: 'Geometry', type: 'Core', credits: '1.0', grades: '9' },
      { name: 'Algebra II', type: 'Core', credits: '1.0', grades: '10' },
      { name: 'Pre-Calculus', type: 'Core', credits: '1.0', grades: '10' },
      { name: 'Statistics', type: 'Core', credits: '1.0', grades: '11' },
      { name: 'Trigonometry', type: 'Core', credits: '1.0', grades: '11' },
      { name: 'Calculus', type: 'Core', credits: '1.0', grades: '12' },
      { name: 'AP Statistics', type: 'AP', credits: '1.0', grades: '11–12' },
    ],
  },
  {
    id: 'science',
    label: { en: 'Science', zh: '自然科學' },
    color: '#3a6b4a',
    courses: [
      { name: 'Biology', type: 'Core', credits: '1.0', grades: '9' },
      { name: 'Environmental Science', type: 'Core', credits: '1.0', grades: '9' },
      { name: 'Chemistry', type: 'Core', credits: '1.0', grades: '10' },
      { name: 'Physics Fundamentals', type: 'Core', credits: '1.0', grades: '10' },
      { name: 'Biology Advanced', type: 'Core', credits: '1.0', grades: '11' },
      { name: 'Physics - Mechanics', type: 'Core', credits: '1.0', grades: '11' },
      { name: 'AP Biology', type: 'AP', credits: '1.0', grades: '11–12' },
    ],
  },
  {
    id: 'social',
    label: { en: 'Social Studies & History', zh: '社會科學與歷史' },
    color: '#7a3b3b',
    courses: [
      { name: 'World History', type: 'Core', credits: '0.5', grades: '9' },
      { name: 'Geography', type: 'Core', credits: '0.5', grades: '9' },
      { name: 'U.S. History', type: 'Core', credits: '0.5', grades: '10' },
      { name: 'World Politics', type: 'Core', credits: '0.5', grades: '10' },
      { name: 'Government', type: 'Core', credits: '0.5–1.0', grades: '11' },
      { name: 'Economics', type: 'Core', credits: '0.5–1.0', grades: '11' },
      { name: 'Sociology', type: 'Core', credits: '1.0', grades: '12' },
      { name: 'Economics Seminar', type: 'Core', credits: '1.0', grades: '12' },
      { name: 'AP Human Geography', type: 'AP', credits: '1.0', grades: '11–12' },
      { name: 'AP Psychology', type: 'AP', credits: '1.0', grades: '11–12' },
    ],
  },
  {
    id: 'business',
    label: { en: 'Business & Finance', zh: '商業與財務' },
    color: '#1a5276',
    courses: [
      { name: 'Introduction to Business & Economics', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Business Technology & Digital Literacy', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Entrepreneurship Fundamentals', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Marketing & Communication', type: 'Elective', credits: '0.5', grades: '10' },
      { name: 'Leadership Communication', type: 'Elective', credits: '0.5', grades: '10' },
      { name: 'Digital Marketing', type: 'Elective', credits: '0.5', grades: '11' },
      { name: 'Business Writing', type: 'Elective', credits: '0.5', grades: '11' },
      { name: 'Business Ethics & Critical Thinking', type: 'Elective', credits: '0.5', grades: '11' },
      { name: 'Business Law', type: 'Elective', credits: '1.0', grades: '12' },
      { name: 'Corporate Finance', type: 'Elective', credits: '1.0', grades: '12' },
      { name: 'Economics Advanced', type: 'Core', credits: '1.0', grades: '12' },
    ],
  },
  {
    id: 'psychology',
    label: { en: 'Psychology & Behavioral Science', zh: '心理學與行為科學' },
    color: '#5b2c6f',
    courses: [
      { name: 'Introduction to Psychology', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Human Development', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Psychology Foundations', type: 'Elective', credits: '0.5', grades: '10' },
      { name: 'Social Psychology', type: 'Elective', credits: '0.5', grades: '10' },
      { name: 'Cognitive Psychology', type: 'Elective', credits: '0.5', grades: '11' },
      { name: 'Experimental Psychology', type: 'Elective', credits: '0.5', grades: '11' },
      { name: 'Behavioral Science', type: 'Elective', credits: '0.5', grades: '12' },
      { name: 'Abnormal Psychology', type: 'Elective', credits: '1.0', grades: '12' },
      { name: 'Counseling & Mental Health Studies', type: 'Elective', credits: '1.0', grades: '12' },
      { name: 'Psychology Seminar / Capstone', type: 'Core', credits: '1.0', grades: '12' },
    ],
  },
  {
    id: 'pe',
    label: { en: 'Health & Physical Education', zh: '健康與體育' },
    color: '#1e8449',
    courses: [
      { name: 'Physical Education', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Health & Wellness', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Health and Nutrition', type: 'Elective', credits: '0.5', grades: '9' },
      { name: 'Sports Psychology', type: 'Elective', credits: '0.5', grades: '10' },
      { name: 'Sports Management Basics', type: 'Elective', credits: '0.5', grades: '10' },
      { name: 'Fitness Leadership', type: 'Elective', credits: '0.5', grades: '11' },
      { name: 'Athletic Training', type: 'Elective', credits: '0.5', grades: '12' },
      { name: 'Sports Management & Leadership', type: 'Elective', credits: '1.0', grades: '12' },
    ],
  },
];

const TYPE_BADGE = {
  Core: { bg: '#2b3d6d', label: { en: 'Core', zh: '必修' } },
  AP: { bg: '#8b0000', label: { en: 'AP', zh: 'AP' } },
  Elective: { bg: '#555', label: { en: 'Elective', zh: '選修' } },
};

export default function CourseCatalog({ language }) {
  const isEn = language !== 'zh';
  const [activeId, setActiveId] = useState('english');
  const active = DEPARTMENTS.find((d) => d.id === activeId);

  return (
    <section style={{ padding: '80px 0 60px', fontFamily: 'Inter, sans-serif' }}>
      <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 32px' }}>
        <h2 style={{ fontSize: '48px', fontWeight: 800, marginBottom: '8px', lineHeight: 1 }}>
          {isEn ? 'COURSE' : '課程'}
        </h2>
        <h2 style={{ fontSize: '48px', fontWeight: 800, marginBottom: '32px', lineHeight: 1 }}>
          {isEn ? 'CATALOG' : '目錄'}
        </h2>
        <p style={{ fontSize: '18px', color: '#555', maxWidth: '640px', marginBottom: '48px', lineHeight: 1.6 }}>
          {isEn
            ? 'GIIS offers a US-accredited high school curriculum spanning core academics, AP coursework, and tailored elective tracks in Business, Psychology, and Health & PE — designed to prepare students for top university admissions.'
            : 'GIIS 提供美國認可的高中課程，涵蓋核心學科、AP 進階課程，以及商業、心理學、健康體育等選修方向，全面備戰頂尖大學申請。'}
        </p>

        <div style={{ display: 'flex', gap: '32px', alignItems: 'flex-start', flexWrap: 'wrap' }}>
          {/* Sidebar tabs */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', minWidth: '220px', flexShrink: 0 }}>
            {DEPARTMENTS.map((dept) => (
              <button
                key={dept.id}
                onClick={() => setActiveId(dept.id)}
                style={{
                  textAlign: 'left',
                  padding: '12px 16px',
                  border: 'none',
                  borderLeft: `4px solid ${activeId === dept.id ? dept.color : 'transparent'}`,
                  background: activeId === dept.id ? `${dept.color}18` : 'transparent',
                  color: activeId === dept.id ? dept.color : '#444',
                  fontWeight: activeId === dept.id ? 700 : 400,
                  fontSize: '15px',
                  cursor: 'pointer',
                  borderRadius: '0 4px 4px 0',
                  transition: 'all 0.15s',
                  fontFamily: 'Inter, sans-serif',
                }}
              >
                {dept.label[isEn ? 'en' : 'zh']}
              </button>
            ))}
          </div>

          {/* Course list */}
          {active && (
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{
                borderLeft: `4px solid ${active.color}`,
                paddingLeft: '20px',
                marginBottom: '24px',
              }}>
                <h3 style={{ fontSize: '26px', fontWeight: 700, margin: 0, color: active.color }}>
                  {active.label[isEn ? 'en' : 'zh']}
                </h3>
                <p style={{ fontSize: '13px', color: '#888', margin: '4px 0 0' }}>
                  {active.courses.length} {isEn ? 'courses offered' : '門課程'}
                </p>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '10px' }}>
                {active.courses.map((c) => (
                  <div key={c.name} style={{
                    border: '1px solid #e0e0e0',
                    borderRadius: '6px',
                    padding: '14px 16px',
                    background: '#fff',
                    boxShadow: '0 1px 3px rgba(0,0,0,0.06)',
                  }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '8px' }}>
                      <span style={{ fontSize: '14px', fontWeight: 600, color: '#222', lineHeight: 1.3 }}>{c.name}</span>
                      <span style={{
                        flexShrink: 0,
                        fontSize: '10px',
                        fontWeight: 700,
                        padding: '2px 7px',
                        borderRadius: '10px',
                        background: TYPE_BADGE[c.type]?.bg || '#555',
                        color: '#fff',
                        letterSpacing: '0.5px',
                      }}>
                        {TYPE_BADGE[c.type]?.label[isEn ? 'en' : 'zh'] || c.type}
                      </span>
                    </div>
                    <div style={{ marginTop: '8px', fontSize: '12px', color: '#777', display: 'flex', gap: '12px' }}>
                      <span>{isEn ? 'Grade' : '年級'} {c.grades}</span>
                      <span>{c.credits} {isEn ? 'cr.' : '學分'}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
