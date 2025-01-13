import React from 'react';
import styles from './Footer.module.css';

function Footer() {
    
    return (
        <footer className={styles.pageFooter}>
            Copyright&copy; {new Date().getFullYear()} Genesis of Ideas International School. All rights reserved.
        </footer>
    )
}
export default Footer;
