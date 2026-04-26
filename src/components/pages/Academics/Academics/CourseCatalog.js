import React, { useState } from 'react';

// Florida 24-credit graduation framework (industry standard for accredited private schools)
const GRAD_REQUIREMENTS = [
  { area: 'English Language Arts', areaZh: '英語語言藝術', credits: 4, color: '#2b3d6d' },
  { area: 'Mathematics',           areaZh: '數學',         credits: 4, color: '#1a5276' },
  { area: 'Science',               areaZh: '自然科學',     credits: 3, color: '#1e8449' },
  { area: 'Social Studies',        areaZh: '社會科學',     credits: 3, color: '#7a3b3b' },
  { area: 'Health & PE',           areaZh: '健康體育',     credits: 1, color: '#6c757d' },
  { area: 'Electives',             areaZh: '選修課程',     credits: 8.5, color: '#5b2c6f' },
  { area: 'Personal Finance',      areaZh: '個人理財',     credits: 0.5, color: '#555' },
];
const TOTAL_CREDITS = 24;

const DEPARTMENTS = [
  {
    id: 'english',
    label: { en: 'English Language Arts', zh: '英語語言藝術' },
    required: { en: '4 credits required', zh: '必修 4 學分' },
    color: '#2b3d6d',
    note: {
      en: 'Full four-year English sequence covering composition, literature, and analytical writing. Students typically earn 2 credits per year (fall + spring).',
      zh: '四年完整英語課程，涵蓋寫作、文學與分析表達。學生每年修習兩門（秋季＋春季），各 1 學分。',
    },
    courses: [
      { name: 'English I',                          type: 'Core', credits: '1.0', grade: '9',  term: 'Fall' },
      { name: 'English I — Writing',                type: 'Core', credits: '1.0', grade: '9',  term: 'Spring' },
      { name: 'English II',                         type: 'Core', credits: '1.0', grade: '10', term: 'Fall' },
      { name: 'English II — Literature',            type: 'Core', credits: '1.0', grade: '10', term: 'Spring' },
      { name: 'English III',                        type: 'Core', credits: '1.0', grade: '11', term: 'Fall' },
      { name: 'English III — Literature',           type: 'Core', credits: '1.0', grade: '11', term: 'Spring' },
      { name: 'English IV — Writing & Communication', type: 'Core', credits: '1.0', grade: '12', term: 'Fall' },
      { name: 'English IV — Advanced Composition',  type: 'Core', credits: '1.0', grade: '12', term: 'Spring' },
    ],
  },
  {
    id: 'math',
    label: { en: 'Mathematics', zh: '數學' },
    required: { en: '4 credits required', zh: '必修 4 學分' },
    color: '#1a5276',
    note: {
      en: 'Algebra I and Geometry are required in Grade 9. Students progress through Pre-Calculus in Grade 10, then choose advanced tracks (Statistics, Trigonometry, Calculus, or AP Statistics) in Grades 11–12.',
      zh: '9 年級必修代數 I 與幾何，10 年級進入預微積分，11–12 年級可選進階路徑（統計、三角、微積分或 AP 統計）。',
    },
    courses: [
      { name: 'Algebra I',    type: 'Core', credits: '1.0', grade: '9',    term: 'Fall' },
      { name: 'Geometry',     type: 'Core', credits: '1.0', grade: '9',    term: 'Spring' },
      { name: 'Algebra II',   type: 'Core', credits: '1.0', grade: '10',   term: 'Fall' },
      { name: 'Pre-Calculus', type: 'Core', credits: '1.0', grade: '10',   term: 'Spring' },
      { name: 'Statistics',   type: 'Core', credits: '1.0', grade: '11',   term: 'Fall' },
      { name: 'Trigonometry', type: 'Core', credits: '1.0', grade: '11',   term: 'Spring' },
      { name: 'Calculus',     type: 'Core', credits: '1.0', grade: '12',   term: 'Fall' },
      { name: 'AP Statistics', type: 'AP',  credits: '1.0', grade: '11–12', term: 'Fall/Spring' },
    ],
  },
  {
    id: 'science',
    label: { en: 'Science', zh: '自然科學' },
    required: { en: '3 credits required', zh: '必修 3 學分' },
    color: '#1e8449',
    note: {
      en: 'Biology is required in Grade 9. Students complete Chemistry and Physics in Grade 10, with advanced science options available in Grades 11–12 including AP Biology.',
      zh: '9 年級必修生物，10 年級修化學與物理，11–12 年級可選進階科學課程，包含 AP 生物。',
    },
    courses: [
      { name: 'Biology',              type: 'Core', credits: '1.0', grade: '9',    term: 'Fall' },
      { name: 'Environmental Science', type: 'Core', credits: '1.0', grade: '9',   term: 'Spring' },
      { name: 'Chemistry',            type: 'Core', credits: '1.0', grade: '10',   term: 'Fall' },
      { name: 'Physics Fundamentals', type: 'Core', credits: '1.0', grade: '10',   term: 'Spring' },
      { name: 'Biology — Advanced',   type: 'Core', credits: '1.0', grade: '11',   term: 'Fall' },
      { name: 'Physics — Mechanics',  type: 'Core', credits: '1.0', grade: '11',   term: 'Spring' },
      { name: 'AP Biology',           type: 'AP',   credits: '1.0', grade: '11–12', term: 'Fall/Spring' },
    ],
  },
  {
    id: 'social',
    label: { en: 'Social Studies', zh: '社會科學與歷史' },
    required: { en: '3 credits required', zh: '必修 3 學分' },
    color: '#7a3b3b',
    note: {
      en: 'Covers U.S. and world history, geography, government, and economics — all required for Florida accreditation. AP Human Geography and AP Psychology are available for advanced study.',
      zh: '涵蓋美國與世界歷史、地理、政府與經濟學，均為 Florida 認證要求科目。進階學生可選修 AP 人文地理及 AP 心理學。',
    },
    courses: [
      { name: 'World History',                  type: 'Core', credits: '0.5', grade: '9',    term: 'Fall' },
      { name: 'Geography',                      type: 'Core', credits: '0.5', grade: '9',    term: 'Spring' },
      { name: 'U.S. History',                   type: 'Core', credits: '0.5', grade: '10',   term: 'Fall' },
      { name: 'World Politics',                 type: 'Core', credits: '0.5', grade: '10',   term: 'Spring' },
      { name: 'Government',                     type: 'Core', credits: '1.0', grade: '11',   term: 'Spring' },
      { name: 'Economics',                      type: 'Core', credits: '1.0', grade: '11',   term: 'Fall/Spring' },
      { name: 'Economics Seminar',              type: 'Core', credits: '1.0', grade: '12',   term: 'Fall' },
      { name: 'Sociology',                      type: 'Core', credits: '1.0', grade: '12',   term: 'Spring' },
      { name: 'AP Human Geography',             type: 'AP',   credits: '1.0', grade: '11–12', term: 'Spring' },
      { name: 'AP Psychology',                  type: 'AP',   credits: '1.0', grade: '11',   term: 'Fall' },
    ],
  },
  {
    id: 'pe',
    label: { en: 'Health & Physical Education', zh: '健康與體育' },
    required: { en: '1 credit required', zh: '必修 1 學分' },
    color: '#5a6e3f',
    note: {
      en: 'Florida requires 1 credit in Physical Education with integrated health content. Students with an interest in sports or wellness may take additional electives in this area.',
      zh: 'Florida 要求修習 1 學分體育（含健康教育）。有興趣的學生可進一步選修運動心理、運動管理等選修課。',
    },
    courses: [
      { name: 'Physical Education',         type: 'Core',    credits: '0.5', grade: '9',  term: 'Fall' },
      { name: 'Health & Wellness',          type: 'Core',    credits: '0.5', grade: '9',  term: 'Spring' },
      { name: 'Health and Nutrition',       type: 'Core',    credits: '0.5', grade: '9',  term: 'Spring' },
      { name: 'Sports Psychology',          type: 'Elective', credits: '0.5', grade: '10', term: 'Fall' },
      { name: 'Fitness Leadership',         type: 'Elective', credits: '0.5', grade: '11', term: 'Fall' },
      { name: 'Athletic Training',          type: 'Elective', credits: '0.5', grade: '12', term: 'Fall' },
      { name: 'Sports Management & Leadership', type: 'Elective', credits: '1.0', grade: '12', term: 'Spring' },
    ],
  },
  {
    id: 'business',
    label: { en: 'Electives — Business & Finance', zh: '選修：商業與財務' },
    required: { en: 'Elective credits', zh: '選修學分' },
    color: '#8b5e00',
    note: {
      en: 'Business electives form a popular concentration track at GIIS, covering entrepreneurship, marketing, finance, and organizational management — directly relevant to business and economics majors.',
      zh: '商業選修是 GIIS 的熱門方向，涵蓋創業、行銷、財務與組織管理，對申請商學院的學生尤為有利。',
    },
    courses: [
      { name: 'Introduction to Business & Economics', type: 'Elective', credits: '0.5', grade: '9',  term: 'Fall' },
      { name: 'Business Technology & Digital Literacy', type: 'Elective', credits: '0.5', grade: '9', term: 'Fall' },
      { name: 'Entrepreneurship Fundamentals',        type: 'Elective', credits: '0.5', grade: '9',  term: 'Spring' },
      { name: 'Marketing & Communication',            type: 'Elective', credits: '0.5', grade: '10', term: 'Fall' },
      { name: 'Leadership Communication',             type: 'Elective', credits: '0.5', grade: '10', term: 'Spring' },
      { name: 'Digital Marketing',                    type: 'Elective', credits: '0.5', grade: '11', term: 'Fall' },
      { name: 'Business Writing',                     type: 'Elective', credits: '0.5', grade: '11', term: 'Fall' },
      { name: 'Business Ethics & Critical Thinking',  type: 'Elective', credits: '0.5', grade: '11', term: 'Spring' },
      { name: 'Organizational Behavior',              type: 'Elective', credits: '0.5', grade: '12', term: 'Fall' },
      { name: 'Business Strategy & Writing',          type: 'Elective', credits: '0.5', grade: '12', term: 'Fall' },
      { name: 'Business Law',                         type: 'Elective', credits: '1.0', grade: '12', term: 'Spring' },
      { name: 'Corporate Finance',                    type: 'Elective', credits: '1.0', grade: '12', term: 'Spring' },
      { name: 'Personal Finance / Applied Economics', type: 'Elective', credits: '1.0', grade: '12', term: 'Spring' },
    ],
  },
  {
    id: 'psychology',
    label: { en: 'Electives — Psychology & Behavioral Science', zh: '選修：心理學與行為科學' },
    required: { en: 'Elective credits', zh: '選修學分' },
    color: '#5b2c6f',
    note: {
      en: 'Psychology is offered as an elective track from Grade 9 and as AP Psychology in Grade 11. Students can build a full concentration through cognitive, social, and applied psychology courses.',
      zh: '心理學從 9 年級開始提供選修，11 年級可選 AP 心理學。學生可透過認知、社會與應用心理學課程建立完整的學習方向。',
    },
    courses: [
      { name: 'Introduction to Psychology',        type: 'Elective', credits: '0.5', grade: '9',    term: 'Fall' },
      { name: 'Human Development',                 type: 'Elective', credits: '0.5', grade: '9',    term: 'Spring' },
      { name: 'Psychology Foundations',            type: 'Elective', credits: '0.5', grade: '10',   term: 'Fall' },
      { name: 'Social Psychology',                 type: 'Elective', credits: '0.5', grade: '10',   term: 'Spring' },
      { name: 'AP Psychology',                     type: 'AP',       credits: '1.0', grade: '11',   term: 'Fall' },
      { name: 'Cognitive Psychology',              type: 'Elective', credits: '0.5', grade: '11',   term: 'Spring' },
      { name: 'Experimental Psychology',           type: 'Elective', credits: '0.5', grade: '11',   term: 'Spring' },
      { name: 'Psychology Seminar / Capstone',     type: 'Core',     credits: '1.0', grade: '12',   term: 'Fall' },
      { name: 'Behavioral Science',                type: 'Elective', credits: '0.5', grade: '12',   term: 'Fall' },
      { name: 'Abnormal Psychology',               type: 'Elective', credits: '1.0', grade: '12',   term: 'Spring' },
      { name: 'Counseling & Mental Health Studies', type: 'Elective', credits: '1.0', grade: '12',  term: 'Spring' },
      { name: 'Media Psychology',                  type: 'Elective', credits: '1.0', grade: '12',   term: 'Spring' },
    ],
  },
  {
    id: 'communication',
    label: { en: 'Electives — Communication & Research', zh: '選修：溝通與研究方法' },
    required: { en: 'Elective credits', zh: '選修學分' },
    color: '#2e6b6b',
    note: {
      en: 'Develops academic writing, public speaking, media literacy, and research skills — competencies valued by all US college admissions offices.',
      zh: '培養學術寫作、公開演說、媒體素養與研究能力，是所有美國大學申請均重視的核心素養。',
    },
    courses: [
      { name: 'Business Media Literacy',              type: 'Elective', credits: '0.5', grade: '9',  term: 'Spring' },
      { name: 'Introduction to Communication',        type: 'Elective', credits: '0.5', grade: '10', term: 'Fall' },
      { name: 'Public Speaking',                      type: 'Elective', credits: '0.5', grade: '10', term: 'Spring' },
      { name: 'Media & Society',                      type: 'Elective', credits: '0.5', grade: '11', term: 'Fall' },
      { name: 'Academic Writing',                     type: 'Elective', credits: '0.5', grade: '11', term: 'Fall' },
      { name: 'Business Research Methods',            type: 'Elective', credits: '0.5', grade: '11', term: 'Spring' },
      { name: 'Research Methods in Social Science',   type: 'Elective', credits: '1.0', grade: '11', term: 'Spring' },
      { name: 'Ethics & Critical Thinking',           type: 'Elective', credits: '0.5', grade: '11', term: 'Spring' },
      { name: 'College Research & Writing',           type: 'Elective', credits: '0.5', grade: '12', term: 'Fall' },
      { name: 'Digital Media & Society',              type: 'Elective', credits: '1.0', grade: '12', term: 'Spring' },
    ],
  },
];

const TYPE_BADGE = {
  Core:    { bg: '#2b3d6d', label: { en: 'Core',    zh: '必修' } },
  AP:      { bg: '#8b0000', label: { en: 'AP',       zh: 'AP'  } },
  Elective:{ bg: '#5a5a5a', label: { en: 'Elective', zh: '選修' } },
};

function RequirementBar({ language }) {
  const isEn = language !== 'zh';
  const total = TOTAL_CREDITS;

  return (
    <div style={{ marginBottom: '48px' }}>
      <h3 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '12px', color: '#222' }}>
        {isEn ? `Graduation Requirements — ${total} Credits Total` : `畢業要求 — 共 ${total} 學分`}
      </h3>
      <p style={{ fontSize: '13px', color: '#666', marginBottom: '16px' }}>
        {isEn
          ? 'GIIS follows the Florida 24-credit accreditation framework, the standard for US-accredited private high schools recognized by US colleges and universities.'
          : 'GIIS 遵循 Florida 24 學分認證框架，此為美國各大學認可的美國私立高中標準學制。'}
      </p>
      {/* Visual credit bar */}
      <div style={{ display: 'flex', height: '12px', borderRadius: '6px', overflow: 'hidden', marginBottom: '12px' }}>
        {GRAD_REQUIREMENTS.map((r) => (
          <div
            key={r.area}
            title={`${r.area}: ${r.credits} cr`}
            style={{
              flex: r.credits,
              backgroundColor: r.color,
              minWidth: '2px',
            }}
          />
        ))}
      </div>
      {/* Legend */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px 20px' }}>
        {GRAD_REQUIREMENTS.map((r) => (
          <div key={r.area} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '13px' }}>
            <span style={{ width: '12px', height: '12px', borderRadius: '2px', backgroundColor: r.color, flexShrink: 0 }} />
            <span style={{ color: '#444' }}>
              {isEn ? r.area : r.areaZh}
              <span style={{ color: '#888', marginLeft: '4px' }}>({r.credits} cr)</span>
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default function CourseCatalog({ language }) {
  const isEn = language !== 'zh';
  const [activeId, setActiveId] = useState('english');
  const active = DEPARTMENTS.find((d) => d.id === activeId);

  return (
    <section style={{ padding: '80px 0 60px', fontFamily: 'Inter, sans-serif' }}>
      <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 32px' }}>
        <h2 style={{ fontSize: '48px', fontWeight: 800, marginBottom: '4px', lineHeight: 1 }}>
          {isEn ? 'COURSE' : '課程'}
        </h2>
        <h2 style={{ fontSize: '48px', fontWeight: 800, marginBottom: '32px', lineHeight: 1 }}>
          {isEn ? 'CATALOG' : '目錄'}
        </h2>

        <RequirementBar language={language} />

        <div style={{ display: 'flex', gap: '32px', alignItems: 'flex-start', flexWrap: 'wrap' }}>
          {/* Sidebar */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '2px', minWidth: '230px', flexShrink: 0 }}>
            {/* Required */}
            <p style={{ fontSize: '11px', fontWeight: 700, color: '#999', letterSpacing: '1px', margin: '0 0 4px 16px', textTransform: 'uppercase' }}>
              {isEn ? 'Required' : '必修'}
            </p>
            {DEPARTMENTS.filter((d) => ['english','math','science','social','pe'].includes(d.id)).map((dept) => (
              <button key={dept.id} onClick={() => setActiveId(dept.id)} style={tabStyle(dept, activeId)}>
                {dept.label[isEn ? 'en' : 'zh']}
              </button>
            ))}
            {/* Electives */}
            <p style={{ fontSize: '11px', fontWeight: 700, color: '#999', letterSpacing: '1px', margin: '12px 0 4px 16px', textTransform: 'uppercase' }}>
              {isEn ? 'Elective Tracks' : '選修方向'}
            </p>
            {DEPARTMENTS.filter((d) => ['business','psychology','communication'].includes(d.id)).map((dept) => (
              <button key={dept.id} onClick={() => setActiveId(dept.id)} style={tabStyle(dept, activeId)}>
                {dept.label[isEn ? 'en' : 'zh']}
              </button>
            ))}
          </div>

          {/* Course list */}
          {active && (
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ borderLeft: `4px solid ${active.color}`, paddingLeft: '20px', marginBottom: '16px' }}>
                <div style={{ display: 'flex', alignItems: 'baseline', gap: '12px', flexWrap: 'wrap' }}>
                  <h3 style={{ fontSize: '24px', fontWeight: 700, margin: 0, color: active.color }}>
                    {active.label[isEn ? 'en' : 'zh']}
                  </h3>
                  <span style={{ fontSize: '13px', color: '#888', fontWeight: 500 }}>
                    {active.required[isEn ? 'en' : 'zh']}
                  </span>
                </div>
                <p style={{ fontSize: '13px', color: '#666', margin: '8px 0 0', lineHeight: 1.6 }}>
                  {active.note[isEn ? 'en' : 'zh']}
                </p>
              </div>

              {/* Grade grouping */}
              {['9','10','11','12','11–12'].map((grade) => {
                const coursesInGrade = active.courses.filter((c) => c.grade === grade);
                if (coursesInGrade.length === 0) return null;
                const gradeLabel = grade.includes('–')
                  ? (isEn ? `Grade ${grade}` : `${grade} 年級`)
                  : (isEn ? `Grade ${grade}` : `${grade} 年級`);
                return (
                  <div key={grade} style={{ marginBottom: '20px' }}>
                    <p style={{ fontSize: '11px', fontWeight: 700, color: '#aaa', letterSpacing: '1px', textTransform: 'uppercase', margin: '0 0 8px' }}>
                      {gradeLabel}
                    </p>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '8px' }}>
                      {coursesInGrade.map((c) => (
                        <div key={c.name} style={{
                          border: '1px solid #e8e8e8',
                          borderRadius: '6px',
                          padding: '12px 14px',
                          background: '#fff',
                          boxShadow: '0 1px 3px rgba(0,0,0,0.05)',
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
                              letterSpacing: '0.4px',
                            }}>
                              {TYPE_BADGE[c.type]?.label[isEn ? 'en' : 'zh'] || c.type}
                            </span>
                          </div>
                          <div style={{ marginTop: '6px', fontSize: '12px', color: '#888', display: 'flex', gap: '10px' }}>
                            <span>{c.credits} {isEn ? 'cr' : '學分'}</span>
                            <span>{c.term}</span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

function tabStyle(dept, activeId) {
  const isActive = activeId === dept.id;
  return {
    textAlign: 'left',
    padding: '10px 16px',
    border: 'none',
    borderLeft: `4px solid ${isActive ? dept.color : 'transparent'}`,
    background: isActive ? `${dept.color}18` : 'transparent',
    color: isActive ? dept.color : '#555',
    fontWeight: isActive ? 700 : 400,
    fontSize: '14px',
    cursor: 'pointer',
    borderRadius: '0 4px 4px 0',
    transition: 'all 0.15s',
    fontFamily: 'Inter, sans-serif',
    width: '100%',
  };
}
