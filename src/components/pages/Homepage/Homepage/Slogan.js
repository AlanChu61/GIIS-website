
import React,{ useEffect, useState } from 'react';

function Slogan() {
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 736);

    useEffect(() => {
        const handleResize = () => setIsMobile(window.innerWidth <= 736);
        window.addEventListener('resize', handleResize);

        return () => window.removeEventListener('resize', handleResize);
    }, []);

    const cardStyle = isMobile
        ? {
              width: '100%', // 小於736px時的寬度
              height: '100px', // 高度可以自適應內容
              backgroundColor: 'rgba(213, 168, 54, 1)',
              justifyContent: 'flex-start',
              alignItems: 'center', 
          }
        : {
              width: '100%', // 大於736px時的寬度
              height: 'auto',
              padding: '4rem',
              backgroundColor: 'rgba(213, 168, 54, 1)',
              margin: '0 auto', // 居中
          };

    const paragraphStyle = isMobile
        ? { fontSize: '17px', 
            fontFamily: 'Lato, sans-serif',
            display: 'flex',
            textAlign: 'left',
            lineHeight: '1.3', // 調整行高
        }
        : { fontSize: '1.5rem', fontFamily: '"Lato", sans-serif' };
        

    const buttonStyle = isMobile
        ? { display: 'flex',
            justifyContent: 'center',
            fontSize: '0.9rem', 
          }
        : {
            fontSize: '1rem', 
            marginTop: '1.5rem' 
          };

    return (
        <>
            {isMobile ? (
                <>
                    {/* 小於 736px 時的結構 */}
                    <div
                        className="text-white text-center p-3 my-3 rounded"
                        style={cardStyle}
                    >
                        <p className="lead" style={paragraphStyle}>
                            Empowering the next generation of innovators and thinkers
                        </p>
                    </div>
                    <button
                        className="btn btn-light mt-3"
                        style={buttonStyle}
                    >
                        Learn More
                    </button>
                </>
            ) : (
                <>
                    {/* 大於 736px 時的結構 */}
                    <div
                        className="text-white text-center p-3 my-3 rounded"
                        style={cardStyle}
                    >
                        <p className="lead" style={paragraphStyle}>
                            Empowering the next generation of innovators and thinkers
                        </p>
                        <button
                            className="btn btn-light"
                            style={buttonStyle}
                        >
                            Learn More
                        </button>
                    </div>
                </>
            )}
        </>
    );
}

export default Slogan;
