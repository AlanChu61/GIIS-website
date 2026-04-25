import React, { useState, useEffect } from 'react';
import styles from './Nav.module.css';
import { Link, useNavigate } from 'react-router-dom';
import { getNavStrings } from '../../../../i18n/siteStrings';

function Nav({ language ,toggleLanguage}) {
    const t = getNavStrings(language);
    const [isNavSticky, setIsNavSticky] = useState(false);
    const [isCollapsed, setIsCollapsed] = useState(true); 
    const navigate = useNavigate();
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 1000);
    const [isLandscape, setIsLandscape] = useState(window.matchMedia('(orientation: landscape)').matches);
    
    useEffect(() => {
        const handleScroll = () => {
            const currentScrollPosition = window.pageYOffset;
            setIsNavSticky(currentScrollPosition > 150);
        };

        const handleResize = () => {
        setIsMobile(window.innerWidth <= 1000);
       };

        const handleOrientationChange = () => {
         setIsLandscape(window.matchMedia('(orientation: landscape)').matches);
        };


     
        window.addEventListener('scroll', handleScroll);
        window.addEventListener('resize', handleResize);
        window.addEventListener('resize', handleOrientationChange);
       
        return () => {
            window.removeEventListener('scroll', handleScroll);
            window.removeEventListener('resize', handleResize);
            window.removeEventListener('resize', handleOrientationChange);
 
        };
    }, []);

    
    const toggleNavbar = () => {
        setIsCollapsed(!isCollapsed);
    };


   return (
    <nav className={`navbar navbar-expand-lg ${isNavSticky ? 'fixed-top' : ''}  ${styles.customBackground}`}>
        <div className={`container-fluid ${styles.navContainer}`}>
            <button className= "navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarLeftMenu" aria-controls="navbarLeftMenu" aria-expanded={!isCollapsed} aria-label="Toggle navigation" onClick={toggleNavbar}>
                <span className="navbar-toggler-icon"></span>
            </button>

            {isMobile && (
           <>
            <div className={`collapse navbar-collapse ${!isCollapsed ? 'show' : ''} ${isLandscape ? styles.leftSlideMenu2 : styles.leftSlideMenu}`}  id="navbarLeftMenu">
             <ul className={styles.leftSlideItems} >
                  <li onClick={() => navigate("/discovery")} >
                    {t.discovery}
                  </li>
                  <li onClick={() => navigate("/academics")}>
                        {t.academics}
                  </li>
                  <li onClick={() => navigate("/admission")}>
                        {t.admission}
                  </li>
                  <li onClick={() => navigate("/support")}>
                        {t.support}
                  </li>
                </ul>
            </div>
           <div className= "justify-content-center" style={{ display:"flex", justifyContent: "flex-end" }}>
             {/* <Link to="/contact" className="btn btn-link px-2">Contact Us</Link> */}
              <a href="https://moodles.genesisideas.school" target="_blank" rel="noopener noreferrer" className={`btn btn-link px-2 ${styles.button}`} >Moodle</a>
              <button type="button" className={`btn btn-link px-2 ${styles.button2}`} onClick={toggleLanguage} aria-label={t.langToggleAria}>
                {language === 'en' ? '中文' : 'English'}
              </button>
            </div>
          </>
 
             )}

            <div className={`collapse navbar-collapse ${isCollapsed ? '' : ''}`}>
                <ul className={`navbar-nav ${styles.customnavbar}`}>
                    <li className={styles.navitem}>
                        <Link className={styles.navLink} to="/discovery">{t.discovery}</Link>
                        <ul className={styles.dropdownMenu}>
                            {t.dropdownDiscovery.map((item) => (
                              <li key={item}>{item}</li>
                            ))}
                        </ul>
                    </li>
                    <li className={styles.navitem}>
                        <Link className={styles.navLink} to="/academics">{t.academics}</Link>
                        <ul className={styles.dropdownMenu}>
                            {t.dropdownAcademics.map((item) => (
                              <li key={item}>{item}</li>
                            ))}
                        </ul>
                    </li>
                    <li className={styles.navitem}>
                      <Link className={styles.navLink} to="/admission">{t.admission}</Link>
                        <ul className={styles.dropdownMenu}>
                            {t.dropdownAdmission.map((item) => (
                              <li key={item}>{item}</li>
                            ))}
                        </ul>
                    </li>
                    <li className={styles.navitem}>
                      <Link className={styles.navLink} to="/support">{t.support}</Link>
                        <ul className={styles.dropdownMenu2}>
                            {t.dropdownSupport.map((item) => (
                              <li key={item}>{item}</li>
                            ))}
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
  );
}
export default Nav; 
