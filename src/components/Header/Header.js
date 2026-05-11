import React from 'react';
import logo_slogan from '../../img/logo_slogan.png';
import { Link } from 'react-router-dom';
import styles from './Header.module.css';
import { getNavStrings } from '../../i18n/siteStrings';
import { getStudentSession, getParentSession } from '../../api/authStorage';

function Header({ language, toggleLanguage }) {
    const t = getNavStrings(language);
    const isLoggedIn = !!(getStudentSession() || getParentSession());
    const isEn = language !== 'zh';

    return (
        <header className={`${styles.header}`}>
            <div className="row align-items-center">
                <div className="col-10 d-flex align-items-center">
                    <Link to="/">
                        <img src={logo_slogan} alt="Genesis of Ideas International School logo" className={`img-fluid ${styles.logoImage}`} />
                    </Link>
                </div>
                <div className="col-2 d-flex justify-content-center flex-wrap gap-1">
                    {isLoggedIn ? (
                        <Link to="/learn" className={`btn btn-link px-2 ${styles.button}`}>
                            {isEn ? 'My Courses' : '我的课程'}
                        </Link>
                    ) : (
                        <Link to="/login" className={`btn btn-link px-2 ${styles.button}`}>{t.signIn}</Link>
                    )}
                </div>
            </div>
        </header>
    );
}

export default Header;
