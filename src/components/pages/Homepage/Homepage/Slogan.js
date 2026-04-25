
import React,{ useEffect, useState } from 'react';
import { getHomeSlogan } from '../../../../i18n/siteStrings';

function Slogan({ language = 'en' }) {
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 736);
    const t = getHomeSlogan(language);

    useEffect(() => {
        const handleResize = () => setIsMobile(window.innerWidth <= 736);
        window.addEventListener('resize', handleResize);

        return () => window.removeEventListener('resize', handleResize);
    }, []);

    const cardStyle = isMobile
        ? {
              width: '100%',
              height: '100px',
              backgroundColor: 'rgba(213, 168, 54, 1)',
              justifyContent: 'flex-start',
              alignItems: 'center',
          }
        : {
              width: '100%',
              height: 'auto',
              padding: '4rem',
              backgroundColor: 'rgba(213, 168, 54, 1)',
              margin: '0 auto',
          };

    const paragraphStyle = isMobile
        ? { fontSize: '17px',
            fontFamily: 'Lato, sans-serif',
            display: 'flex',
            textAlign: 'left',
            lineHeight: '1.3',
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
                    <div
                        className="text-white text-center p-3 my-3 rounded"
                        style={cardStyle}
                    >
                        <p className="lead" style={paragraphStyle}>
                            {t.line}
                        </p>
                    </div>
                    <button
                        type="button"
                        className="btn btn-light mt-3"
                        style={buttonStyle}
                    >
                        {t.cta}
                    </button>
                </>
            ) : (
                <>
                    <div
                        className="text-white text-center p-3 my-3 rounded"
                        style={cardStyle}
                    >
                        <p className="lead" style={paragraphStyle}>
                            {t.line}
                        </p>
                        <button
                            type="button"
                            className="btn btn-light"
                            style={buttonStyle}
                        >
                            {t.cta}
                        </button>
                    </div>
                </>
            )}
        </>
    );
}

export default Slogan;
