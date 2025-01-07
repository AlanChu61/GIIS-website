import React from 'react';
import logo_slogan from '../../img/logo_slogan.png';
import { Link } from 'react-router-dom';
import styles from './Header.module.css'; // Custom styles for specific adjustments

function Header({ language,toggleLanguage }) {

    return (
        <header className={`${styles.header}`}>
            {/* First row for logo and buttons */}
            <div className="row align-items-center">
                <div className="col-10 d-flex align-items-center">
                    <Link to="/">
                        <img src={logo_slogan} alt='Excel High School Logo' className={`img-fluid ${styles.logoImage}`} />
                    </Link>
                </div>
                <div className= "col-2 d-flex justify-content-center" >
                    {/* <Link to="/contact" className="btn btn-link px-2">Contact Us</Link> */}
                    <a href="https://moodles.genesisideas.school" target="_blank" rel="noopener noreferrer" className={`btn btn-link px-2 ${styles.button}`} >Moodles</a>
                    <button className={`btn btn-link px-2 ${styles.button2}`} onClick={toggleLanguage}>
                        {language === 'en' ? 'Switch to Chinese' : '切换到英文'}
                    </button>
                </div>
            </div> 
        </header>
    );
}

export default Header;
