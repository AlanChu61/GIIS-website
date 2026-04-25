import React from 'react';

function FacultyGraduates({ language = 'en' }) {
    // Automatically import all files from the logos directory
    const importAll = (r) => {
        let images = {};
        r.keys().forEach((item) => { images[item.replace('./', '')] = r(item); });
        return images;
    };

    const images = importAll(require.context('../../../../img/Homepage/SchoolLogo', false, /\.(png|jpe?g|svg)$/));

    // Convert object to array if needed
    const logos = Object.entries(images).map(([key, value]) => {
        return {
            src: value,
            alt: key.replace(/\..+$/, '')  // Remove file extension from alt text
        };
    });

    return (
        <section className="school-logos">
            <h2>{language === 'zh' ? '教师与毕业生' : 'Faculty & Graduates'}</h2>
            <div className="container">
                <div className="row justify-content-center  g-0">
                    {logos.map((logo, index) => (
                        <div key={index} className="col-3 col-md-2 mb-2 d-flex justify-content-center align-items-center">
                            <img src={logo.src} alt={logo.alt} className="img-fluid" style={{ maxHeight: "100px", padding: "5px"}} loading="lazy" decoding="async" />
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}

export default FacultyGraduates;
