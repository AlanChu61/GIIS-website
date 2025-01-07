import React from 'react';
import Nav from './HomepageHeader/Nav.js';
import ImgSlider from './Homepage/ImgSlider.js';
import Slogan from './Homepage/Slogan';
import Introduction from './Homepage/Introduction';
import CogniaAccreditation from './Homepage/CogniaAccreditation.js';
import Testimonial from './Homepage/Testimonial.js';
import FacultyGraduates from './Homepage/FacultyGraduates.js';
import ContactForm from './Homepage/ContactForm';

function HomepageMain({ language,toggleLanguage }) {
   return (
    <>
        <div className="row">
            <Nav language={language} toggleLanguage={toggleLanguage}/>
        </div>

        <div className="card mb-0" id="homepage">
            <div className="container-fluid">
                <ImgSlider />
                <div className="card-body">
                    <Slogan />
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

        <div className="card mb-0" id="accreditation">
            <div className="container-fluid">
                <div className="card-body">
                    <CogniaAccreditation language={language} />
                </div>
            </div>
        </div>

        <div className="card mb-0" id="testimonials">
            <div className="container-fluid">
                <div className="card-body">
                    <Testimonial />
                </div>
            </div>
        </div>

        <div className="card mb-0" id="faculty">
            <div className="container-fluid">
                <div className="card-body">
                    <FacultyGraduates />
                </div>
            </div>
        </div>

        <div className="card mb-0" id="contact">
            <div className="container-fluid">
                <div className="card-body">
                    <ContactForm />
                </div>
            </div>
        </div>
    </>
  );
}

export default HomepageMain;
