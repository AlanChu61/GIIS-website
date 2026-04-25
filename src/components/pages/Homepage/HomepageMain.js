import React from 'react';
import { Helmet } from 'react-helmet-async';
import Nav from './HomepageHeader/Nav.js';
import ImgSlider from './Homepage/ImgSlider.js';
import Slogan from './Homepage/Slogan';
import Introduction from './Homepage/Introduction';
// import CogniaAccreditation from './Homepage/CogniaAccreditation.js';
import Testimonial from './Homepage/Testimonial.js';
import FacultyGraduates from './Homepage/FacultyGraduates.js';
import ContactForm from './Homepage/ContactForm';

function HomepageMain({ language,toggleLanguage }) {
   const isEn = language === 'en';
   return (
    <>
        <Helmet>
          <title>{isEn ? 'Home' : '首頁'} | Genesis of Ideas International School</title>
          <meta
            name="description"
            content={isEn
              ? 'Genesis of Ideas International School — academics, admissions, student support, and how to reach us.'
              : '創思國際學校（Genesis of Ideas International School）— 課程、入學、學生支援與聯絡方式。'}
          />
        </Helmet>
        <div className="row">
            <Nav language={language} toggleLanguage={toggleLanguage}/>
        </div>

        <div className="card mb-0" id="homepage">
            <div className="container-fluid">
                    <ImgSlider />
                <div className="card-body">
                    <Slogan language={language} />
                </div>
            </div>
        </div>

        <div className="card mb-0" id="about">
            <div className="container-fluid">
                <div className="card-body">
                    <Introduction language={language} />
                </div>
            </div>
        </div>

        {/* <div className="card mb-0" id="accreditation">
            <div className="container-fluid">
                <div className="card-body">
                    <CogniaAccreditation language={language} />
                </div>
            </div>
        </div> */}

        <div className="card mb-0" id="testimonials">
            <div className="container-fluid">
                <div className="card-body">
                    <Testimonial language={language} />
                </div>
            </div>
        </div>

        <div className="card mb-0" id="faculty">
            <div className="container-fluid">
                <div className="card-body">
                    <FacultyGraduates language={language} />
                </div>
            </div>
        </div>

        <div className="card mb-0" id="contact">
            <div className="container-fluid">
                <div className="card-body">
                    <ContactForm language={language} />
                </div>
            </div>
        </div>
    </>
  );
}

export default HomepageMain;
