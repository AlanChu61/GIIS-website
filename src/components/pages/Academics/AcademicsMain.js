import React from 'react';
import Nav from './AcademicsHeader/Nav.js';
import img from '../../../img/Homepage/homepage8.png';
import AcademicsIntroduction from'./Academics/Academicsintroduction.js';

function AcademicsMain({ language }) {

   const containerStyle = {
        position: 'relative',
        display: 'flex',
        justifyContent: 'center', // 水平居中
        marginTop: '0', // 與導航欄保持距離
        width: '100%',
    };

    const imageStyle = {
        width: '100%', // 保持容器的寬度
        height: '400px', // 固定高度
        objectFit: 'cover'
    };

     const textOverlayStyle = {
        position: 'absolute',
        bottom: '-70px', // 固定在圖片底部
        backgroundColor: 'rgba(0, 0, 0, 0.8)', // 半透明黑色背景
        color: 'white',
        width: '45%',
        zIndex: '20', 
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        padding: '10px',
    };

     const headline = {
        fontSize:'35px', 
        textAlign: 'center',
        paddingTop: '10px',
    };
     const paragraph = {
        fontSize:'20px', 
        textAlign: 'center',
    };
 
     const cardStyle = {
        position: 'relative', // 需要設置 position 來使 z-index 生效
        zIndex: '10', // 調整層級
        marginTop: '0', // 保持一些間距
        backgroundColor: 'rgba(43, 61, 109, 1)',
        borderBottom: '20px solid rgba(213, 168, 54, 1)',
    };
   
   return (
    <>
        <div className="row">
            <Nav language={language} />
        </div>
      
        <div style={containerStyle}>
          <img src={img} alt="Academics" style={imageStyle} />
          <div style={textOverlayStyle}>
            <p style={headline}>{language === 'en' ? 'ACADEMICS' : '学术'}</p>
            <p style={paragraph}>{language === 'en' ? 'Genesis of Ideas International School is dedicated to providing students a dynamic learning environment and empowering them with the critical thinking and problem-solving skills.' : 'Genesis of Ideas International School 致力于为学生提供充满活力的学习环境，并赋予他们批判性思维和解决问题的能力。'}</p>
          </div>
        </div>

        <div className="card mt-0" id="introduction2" style={cardStyle}>
         <div className="container">
           <div className="card-body">
            <AcademicsIntroduction language={language} />
           </div>
         </div>
       </div>

    </>
 );
}   
   
export default AcademicsMain;
