import React, { useState, useEffect } from 'react';
import styles from './Nav.module.css'; 
import { Link, useNavigate } from 'react-router-dom';

function Nav({ language , toggleLanguage }) {
    const [isNavSticky, setIsNavSticky] = useState(false);
    const [isCollapsed, setIsCollapsed] = useState(true); 
    const navigate = useNavigate();
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);

    useEffect(() => {
        document.documentElement.lang = language === 'en' ? 'en' : 'zh';
    }, [language]);

    useEffect(() => {
        const handleScroll = () => {
            const currentScrollPosition = window.pageYOffset;
            setIsNavSticky(currentScrollPosition > 150);
        };

        const handleResize = () => {
        setIsMobile(window.innerWidth <= 768);
       };


        window.addEventListener('scroll', handleScroll);
        window.addEventListener('resize', handleResize);
        
        return () => {
            window.removeEventListener('scroll', handleScroll);
            window.addEventListener('resize', handleResize);
        };
    }, []);

    const toggleNavbar = () => {
        setIsCollapsed(!isCollapsed);
    };

    return (
        <nav className={`navbar navbar-expand-lg ${isNavSticky ? 'fixed-top' : ''} ${styles.customBackground}`}>
           <div className={`container-fluid ${styles.navContainer}`}>
             <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarLeftMenu" aria-controls="navbarLeftMenu" aria-expanded={!isCollapsed} aria-label="Toggle navigation" onClick={toggleNavbar}>
              <span className="navbar-toggler-icon"></span>
             </button>

             {isMobile && (
            <>
             <div className={`collapse navbar-collapse ${!isCollapsed ? 'show' : ''} ${styles.leftSlideMenu}`} id="navbarLeftMenu">
              <ul className={styles.leftSlideItems}>
                <p>{language === 'en' ? 'DISCOVERY' : '发现我们'}</p>
                <li onClick={() => navigate("/academics")}>
                    <Link to="/academics" onClick={(e) => e.preventDefault()}>
                        {language === 'en' ? 'ACADEMICS' : '学术'}
                    </Link>
                </li>
                <li onClick={() => navigate("/admission")}>
                    <Link to="/admission" onClick={(e) => e.preventDefault()}>
                        {language === 'en' ? 'ADMISSION' : '入学'}
                    </Link>
                </li>
                <li onClick={() => navigate("/support")}>
                    <Link to="/support" onClick={(e) => e.preventDefault()}>
                        {language === 'en' ? 'STUDENT SUPPORT' : '学生支持'}
                    </Link>
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
                <p className={`${styles.navitem2} ${styles.navText}`}>{language === 'en' ? 'DISCOVERY' : '发现我们'}</p>
    
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
