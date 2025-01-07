import React from 'react';
import Nav from './DiscoveryHeader/Nav.js';
import img from '../../../img/Homepage/homepage3.png';
import DiscoveryIntroduction from'./Discovery/discoveryIntroduction.js';
import DiscoveryIntroduction2 from'./Discovery/discoveryIntroduction2.js';

function DiscoveryMain({ language , toggleLanguage }) {

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
        width: '35%',
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
            <Nav language={language} toggleLanguage={toggleLanguage}  />
        </div>
      
        <div style={containerStyle}>
          <img src={img} alt="Discovery" style={imageStyle} />
          <div style={textOverlayStyle}>
            <p style={headline}>{language === 'en' ? 'DISCOVERY' : '发现我们'}</p>
            <p style={paragraph}>{language === 'en' ? 'Take the opportunity to freely explore new knowledge and discover your potential.Continuous learning fuels personal growth and innovation.' : '抓住机会，自由探索新知识，发现你的潜力。持续学习推动个人成长和创新。'}</p>
          </div>
        </div>

       <div className="card mt-0" id="introduction" style={cardStyle}>
         <div className="container">
            <div className="card-body">
               <DiscoveryIntroduction language={language} />
            </div>
         </div>
       </div>

       <div className="card mt-0" id="introduction2">
         <div className="container">
               <DiscoveryIntroduction2 language={language} />
         </div>
       </div>
       
    </>
  );
}

export default DiscoveryMain;

