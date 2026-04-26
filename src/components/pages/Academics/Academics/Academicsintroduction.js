import React from 'react';

function Academicsintroduction({ language }) {
  const isEn = language !== 'zh';

  const headlineStyle = {
    marginTop: '115px',
    color: 'white',
    width: '100%',
    paddingLeft: '15%',
    fontFamily: 'Inter, sans-serif',
    fontWeight: 'bold',
    fontSize: '70px',
    lineHeight: '1',
  };

  const introductionStyle = {
    marginTop: '70px',
    color: 'rgba(255, 255, 255, 0.7)',
    width: '100%',
    paddingLeft: '15%',
    fontFamily: 'Inter, sans-serif',
    fontWeight: 'bold',
    fontSize: '35px',
    lineHeight: '1',
  };

  const containerheading = {
    marginTop: '70px',
    color: 'rgba(255, 255, 255, 0.8)',
    width: '100%',
    paddingLeft: '15%',
    fontFamily: 'Inter, sans-serif',
    fontWeight: 'normal',
    fontSize: '30px',
    lineHeight: '1',
  };

  const container = {
    marginTop: '30px',
    width: '80%',
    paddingLeft: '16%',
    height: '30%',
    wordWrap: 'break-word',
    color: 'rgba(255, 255, 255, 0.6)',
    fontFamily: 'Arial, sans-serif',
    fontSize: '25px',
  };

  const container2 = {
    marginTop: '30px',
    marginBottom: '100px',
    width: '80%',
    paddingLeft: '16%',
    height: '30%',
    wordWrap: 'break-word',
    color: 'rgba(255, 255, 255, 0.6)',
    fontFamily: 'Arial, sans-serif',
    fontSize: '25px',
  };

  const textStyle = {
    position: 'relative',
    paddingLeft: '25px',
  };

  return (
    <>
      <div style={headlineStyle}>
        <p>{isEn ? 'WHAT MAKES GIIS' : '創思國際學校'}</p>
        <p>{isEn ? 'DIFFERENT?' : '有何不同？'}</p>
      </div>

      <div style={introductionStyle}>
        <p>{isEn ? 'The GIIS Difference' : '我們的與眾不同'}</p>
      </div>

      {/* Point 1: US Accredited Diploma */}
      <div style={containerheading}>
        <p style={textStyle}>
          <span style={{ position: 'absolute', left: '0' }}>•</span>
          {isEn ? 'US-Accredited High School Diploma' : '美國認證高中文憑'}
        </p>
      </div>
      <div style={container}>
        <p>
          {isEn
            ? 'GIIS issues a Florida-accredited US high school diploma following the 24-credit graduation framework — the standard recognized by US colleges and universities for international student admissions.'
            : 'GIIS 提供符合 Florida 24 學分畢業標準的美國認證高中文憑，是美國大學在審核國際學生申請時所認可的學術資歷。'}
        </p>
      </div>

      {/* Point 2: AI & Technology */}
      <div style={containerheading}>
        <p style={textStyle}>
          <span style={{ position: 'absolute', left: '0' }}>•</span>
          {isEn ? 'Immersive Learning with AI and Advanced Technologies' : '人工智慧與先進技術的沉浸式學習'}
        </p>
      </div>
      <div style={container}>
        <p>
          {isEn
            ? 'By integrating AI and cutting-edge technologies into teaching, we create immersive learning experiences that make the curriculum more engaging, adaptive, and interactive.'
            : '透過將 AI 和尖端科技整合到教學中，我們打造身臨其境的學習體驗，讓課程更具吸引力、適應性與互動性。'}
        </p>
      </div>

      {/* Point 3: Personalized Learning */}
      <div style={containerheading}>
        <p style={textStyle}>
          <span style={{ position: 'absolute', left: '0' }}>•</span>
          {isEn ? 'Personalized Learning and Holistic Development' : '個人化學習與全人發展'}
        </p>
      </div>
      <div style={container2}>
        <p>
          {isEn
            ? 'We emphasize personalized instruction with diverse elective tracks — Business & Finance, Psychology, and Communication — tailored to each student\'s college major aspirations and career goals.'
            : '我們以因材施教為核心，提供商業財務、心理學、溝通研究等多元選修方向，依據每位學生的大學申請目標與職涯規劃量身設計。'}
        </p>
      </div>
    </>
  );
}

export default Academicsintroduction;
