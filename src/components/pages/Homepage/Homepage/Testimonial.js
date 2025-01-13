import React, { useRef , useState } from 'react'; // Make sure useRef is included here
import Slider from 'react-slick';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import styles from './Testimonial.module.css';

import student1 from '../../../../img/Homepage/StuPhoto/student1.png';
import student2 from '../../../../img/Homepage/StuPhoto/student2.png';
import student3 from '../../../../img/Homepage/StuPhoto/student3.png';
import student4 from '../../../../img/Homepage/StuPhoto/student4.png';
import student5 from '../../../../img/Homepage/StuPhoto/student5.png';

function Testimonial ()  {
    const sliderRef = useRef();  // useRef is now correctly imported and used
    const [selectedTestimonial, setSelectedTestimonial] = useState(null); // 控制顯示心得分享
    const [isMobile, setIsMobile] = useState(window.innerWidth < 736); // 判斷螢幕寬度

    const testimonials = [
        {
            id: 1,
            name: "Li Wei Zhang",
            comment: "Participating in this program has profoundly impacted my career trajectory. The hands-on projects and real-world applications taught here have enabled me to excel in my role as a data scientist at a leading tech firm.",
            photoUrl: student1
        },
        {
            id: 2,
            name: "Suki Kim",
            comment: "I am profoundly grateful for the comprehensive curriculum that bridged my academic knowledge with practical skills, preparing me superbly for the competitive job market. The mentorship program, in particular, has opened doors for me that I never anticipated.",
            photoUrl: student2
        },
        {
            id: 3,
            name: "Ananya Rao",
            comment: "My experience at this institution has been nothing short of transformative. The supportive faculty fostered an environment that encouraged exploration and innovation, which helped me develop a critical analytical mindset that is invaluable in my current entrepreneurial ventures.",
            photoUrl: student3
        },
        {
            id: 4,
            name: "Chen Yu Yan",
            comment: "The knowledge and support I received from the teaching staff were phenomenal. Their expertise in diverse fields provided a well-rounded education and they were always available to provide guidance, ensuring that I was never lost during my studies.",
            photoUrl: student4
        },
        {
            id: 5,
            name: "Haruto Takahashi",
            comment: "The skills I've developed here, especially in innovative problem-solving and strategic planning, have greatly propelled my career in technology management. The learning environment is unparalleled in its commitment to student success and professional development.",
            photoUrl: student5
        },
    ];

    React.useEffect(() => {
        const handleResize = () => setIsMobile(window.innerWidth < 736);
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);
    
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        easing: "ease-in-out",
    };

    const handleClick = (testimonial) => {
        setSelectedTestimonial(testimonial);
    };

    // 點擊外部區域關閉心得視窗
    const handleClose = () => {
        setSelectedTestimonial(null);
    };
    
    return (
        <div className={styles.testimonialContainer}>
            <h2>Testimonial</h2>

           {!isMobile ? (
            <Slider ref={sliderRef} {...settings}>
                {testimonials.map((testimonial, index) => (
                    <div key={index} className={styles.testimonialItem}>
                        <img src={testimonial.photoUrl} alt={testimonial.name} className={styles.testimonialPhoto} />
                        <h3>{testimonial.name}</h3>
                        <p>{testimonial.comment}</p>
                    </div>
                ))}
            </Slider>
             ) : (
              <>
                <p style={{ fontSize:'12px'}}>Tap the photo to see their testimonial.</p>
                <div className={styles.staticList} >
                    {testimonials.map((testimonial) => (
                        <div
                            key={testimonial.id}
                            className={styles.listItem}
                            onClick={() => handleClick(testimonial)}
                        >
                            <img
                                src={testimonial.photoUrl}
                                alt={testimonial.name}
                                className={styles.photo}
                            />
                             <p className={styles.nameStyle}>{testimonial.name}</p>
                        </div>
                    ))}
                </div> 
              </>
            )}
            {selectedTestimonial && (
                <div className={styles.modal} onClick={handleClose}>
                    <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
                        <h3 style={{fontWeight:'bold' }}>{selectedTestimonial.name}</h3>
                        <p classname={styles.commentStyle}>{selectedTestimonial.comment}</p>
                        <button className={styles.closeButton} onClick={handleClose}>
                            Close
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Testimonial;

