import React from 'react';
import ImgSlider from './Homepage/ImgSlider.js';
import Slogan from './Homepage/Slogan';
import Introduction from './Homepage/Introduction';
// import CogniaAccreditation from './Homepage/CogniaAccreditation.js';
import Testimonial from './Homepage/Testimonial.js';
import FacultyGraduates from './Homepage/FacultyGraduates.js';
import ContactForm from './Homepage/ContactForm';

function Homepage({ language }) {
    return (
        <>
            <div className="card mb-1" id="homepage">
                <div className="container">
                    <ImgSlider />
                    <div className="card-body">
                        <Slogan />
                    </div>
                </div>
            </div>

            <div className="card mb-1" id="about">
                <div className="container">
                    <div className="card-body">
                        <Introduction language={language} />
                    </div>
                </div>
            </div>

            {/* <div className="card mb-1" id="accreditation">
                <div className="container">
                    <div className="card-body">
                        <CogniaAccreditation language={language} />
                    </div>
                </div>
            </div> */}

            <div className="card mb-1" id="testimonials">
                <div className="container">
                    <div className="card-body">
                        <Testimonial />
                    </div>
                </div>
            </div>

            <div className="card mb-1" id="faculty">
                <div className="container">
                    <div className="card-body">
                        <FacultyGraduates />
                    </div>
                </div>
            </div>

            <div className="card mb-1" id="contact">
                <div className="container">
                    <div className="card-body">
                        <ContactForm />
                    </div>
                </div>
            </div>
        </>
    );
}

export default Homepage;
