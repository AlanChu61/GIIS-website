import React, { useState, useEffect } from 'react';
import styles from './Nav.module.css'; 
import { Link, useNavigate } from 'react-router-dom';

function Nav({ language ,toggleLanguage}) {
    const [isNavSticky, setIsNavSticky] = useState(false);
    const [isCollapsed, setIsCollapsed] = useState(true); 
    const navigate = useNavigate();
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 1000);
    const [isLandscape, setIsLandscape] = useState(window.matchMedia('(orientation: landscape)').matches);
    
    
    useEffect(() => {
        document.documentElement.lang = language === 'en' ? 'en' : 'zh';
    }, [language]);

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
                    {language === 'en' ? 'DISCOVERY' : '发现我们'}
                  </li>
                  <li onClick={() => navigate("/academics")}>
                        {language === 'en' ? 'ACADEMICS' : '学术'}
                  </li>
                  <li onClick={() => navigate("/admission")}>
                        {language === 'en' ? 'ADMISSION' : '入学'}
                  </li>
                  <li onClick={() => navigate("/support")}>
                        {language === 'en' ? 'STUDENT SUPPORT' : '学生支持'}
                  </li>
                </ul>
            </div>
           <div className= "justify-content-center" style={{ display:"flex", justifyContent: "flex-end" }}>
             {/* <Link to="/contact" className="btn btn-link px-2">Contact Us</Link> */}
              <a href="https://moodles.genesisideas.school" target="_blank" rel="noopener noreferrer" className={`btn btn-link px-2 ${styles.button}`} >Moodles</a>
              <button className={`btn btn-link px-2 ${styles.button2}`} onClick={toggleLanguage}>
                {language === 'en' ? 'Switch to Chinese' : '切换到英文'}
              </button>
            </div>
          </>
 
             )}

            <div className={`collapse navbar-collapse ${isCollapsed ? '' : ''}`}>
                <ul className={`navbar-nav ${styles.customnavbar}`}>
                    <li className={styles.navitem}>
                        <Link className={styles.navLink} to="/discovery">{language === 'en' ? 'DISCOVERY' : '发现我们'}</Link>
                        <ul className={styles.dropdownMenu}>
                            <li>Meet Our School</li>
                            <li>Our Mission</li>
                            <li>About Our Faculty</li>
                        </ul>
                    </li>
                    <li className={styles.navitem}>
                        <Link className={styles.navLink} to="/academics">{language === 'en' ? 'ACADEMICS' : '学术'}</Link>
                        <ul className={styles.dropdownMenu}>
                            <li>Learning Style</li>
                            <li>Subjects</li>
                            <li>Curriculum Options</li>
                        </ul>
                    </li>
                    <li className={styles.navitem}>
                      <Link className={styles.navLink} to="/admission">{language === 'en' ? 'ADMISSION' : '入学'}</Link>
                        <ul className={styles.dropdownMenu}>
                            <li>Apply Now</li>
                            <li>Tuition & Fee</li>
                            <li>FAQ</li>
                        </ul>
                    </li>
                    <li className={styles.navitem}>
                      <Link className={styles.navLink} to="/support">{language === 'en' ? 'STUDENT SUPPORT' : '学生支持'}</Link>
                        <ul className={styles.dropdownMenu2}>
                            <li>Academic Advising</li>
                            <li>Life Counseling</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
  );
}
export default Nav; 
