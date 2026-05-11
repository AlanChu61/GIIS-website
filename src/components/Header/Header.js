import React from 'react';
import logo_slogan from '../../img/logo_slogan.png';
import { Link } from 'react-router-dom';
import styles from './Header.module.css';

function Header() {
    return (
        <header className={`${styles.header}`}>
            <Link to="/">
                <img src={logo_slogan} alt="Genesis of Ideas International School logo" className={`img-fluid ${styles.logoImage}`} />
            </Link>
        </header>
    );
}

export default Header;
