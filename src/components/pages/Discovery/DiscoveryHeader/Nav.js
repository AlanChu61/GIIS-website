import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; 
import styles from './Nav.module.css'; 

function Nav({ language }) {
    const [isNavSticky, setIsNavSticky] = useState(false);
    const [isCollapsed, setIsCollapsed] = useState(true); 


    useEffect(() => {
        const handleScroll = () => {
            const currentScrollPosition = window.pageYOffset;
            setIsNavSticky(currentScrollPosition > 150);
        };

        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    const toggleNavbar = () => {
        setIsCollapsed(!isCollapsed);
    };

    return (
        <nav className={`navbar navbar-expand-lg ${isNavSticky ? 'fixed-top' : ''} ${styles.customBackground}`}>
            <div className={`container-fluid ${styles.navContainer}`}>
             <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContents" aria-controls="navbarSupportedContents" aria-expanded={!isCollapsed} aria-label="Toggle navigation" onClick={toggleNavbar}>
              <span className="navbar-toggler-icon"></span>
             </button>

             <div className={`collapse navbar-collapse ${!isCollapsed ? 'show' : ''} ${styles.leftSlideMenu}`} id="navbarLeftMenu">
              <ul className={styles.leftSlideItems}>
               <p>{language === 'en' ? 'DISCOVERY' : '发现我们'}</p>
               <li onClick={() => window.location.href = "/academics"}>{language === 'en' ? 'ACADEMICS' : '学术'}</li>
               <li onClick={() => window.location.href = "/admission"}>{language === 'en' ? 'ADMISSION' : '入学'}</li>
               <li onClick={() => window.location.href = "/support"}>{language === 'en' ? 'STUDENT SUPPORT' : '学生支持'}</li>
               </ul>
              </div>
                
              <div className={`collapse navbar-collapse ${isCollapsed ? 'show' : ''}`} id="navbarSupportedContents">
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
                   <ul className={styles.dropdownMenu}>
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