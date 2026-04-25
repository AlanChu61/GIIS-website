import React, { useRef , useState } from 'react';
import Slider from 'react-slick';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import styles from './Testimonial.module.css';
import { getTestimonialCopy } from '../../../../i18n/siteStrings';

import student1 from '../../../../img/Homepage/StuPhoto/student1.png';
import student2 from '../../../../img/Homepage/StuPhoto/student2.png';
import student3 from '../../../../img/Homepage/StuPhoto/student3.png';
import student4 from '../../../../img/Homepage/StuPhoto/student4.png';
import student5 from '../../../../img/Homepage/StuPhoto/student5.png';

function Testimonial({ language = 'en' }) {
    const sliderRef = useRef();
    const [selectedTestimonial, setSelectedTestimonial] = useState(null);
    const [isMobile, setIsMobile] = useState(window.innerWidth < 736);
    const ui = getTestimonialCopy(language);
    const en = language === 'en';

    const testimonials = [
        {
            id: 1,
            name: "Li Wei Zhang",
            comment: "Participating in this program has profoundly impacted my career trajectory. The hands-on projects and real-world applications taught here have enabled me to excel in my role as a data scientist at a leading tech firm.",
            commentZh: "参与本项目深刻影响了我的职业路径。这里的实战项目与真实场景训练，使我在顶尖科技公司担任数据科学家时能够脱颖而出。",
            photoUrl: student1
        },
        {
            id: 2,
            name: "Suki Kim",
            comment: "I am profoundly grateful for the comprehensive curriculum that bridged my academic knowledge with practical skills, preparing me superbly for the competitive job market. The mentorship program, in particular, has opened doors for me that I never anticipated.",
            commentZh: "我非常感谢完整的课程体系，将学术知识与实务能力衔接起来，让我为竞争激烈的就业市场做好准备。导师计划更为我打开了意想不到的机会。",
            photoUrl: student2
        },
        {
            id: 3,
            name: "Ananya Rao",
            comment: "My experience at this institution has been nothing short of transformative. The supportive faculty fostered an environment that encouraged exploration and innovation, which helped me develop a critical analytical mindset that is invaluable in my current entrepreneurial ventures.",
            commentZh: "在这所学校的经历令我获益良多。支持性的师资营造了鼓励探索与创新的环境，帮助我建立批判性分析思维，对现今的创业之路弥足珍贵。",
            photoUrl: student3
        },
        {
            id: 4,
            name: "Chen Yu Yan",
            comment: "The knowledge and support I received from the teaching staff were phenomenal. Their expertise in diverse fields provided a well-rounded education and they were always available to provide guidance, ensuring that I was never lost during my studies.",
            commentZh: "教师团队给予的知识与支持非常出色。跨领域的专业素养带来均衡的教育，并随时提供指导，让我在学习过程中始终方向明确。",
            photoUrl: student4
        },
        {
            id: 5,
            name: "Haruto Takahashi",
            comment: "The skills I've developed here, especially in innovative problem-solving and strategic planning, have greatly propelled my career in technology management. The learning environment is unparalleled in its commitment to student success and professional development.",
            commentZh: "我在这里培养的能力，特别是在创新解题与策略规划方面，大幅推进了我在科技管理领域的职涯。学习环境对学生成功与专业发展的投入令人印象深刻。",
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

    const handleClose = () => {
        setSelectedTestimonial(null);
    };

    const textOf = (item) => (en ? item.comment : item.commentZh);

    return (
        <div className={styles.testimonialContainer}>
            <h2>{ui.title}</h2>

           {!isMobile ? (
            <Slider ref={sliderRef} {...settings}>
                {testimonials.map((testimonial, index) => (
                    <div key={index} className={styles.testimonialItem}>
                        <img src={testimonial.photoUrl} alt={testimonial.name} className={styles.testimonialPhoto} loading="lazy" decoding="async" />
                        <h3>{testimonial.name}</h3>
                        <p>{textOf(testimonial)}</p>
                    </div>
                ))}
            </Slider>
             ) : (
              <>
                <p style={{ fontSize:'12px'}}>{ui.mobileHint}</p>
                <div className={styles.staticList} >
                    {testimonials.map((testimonial) => (
                        <div
                            key={testimonial.id}
                            className={styles.listItem}
                            onClick={() => handleClick(testimonial)}
                            onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); handleClick(testimonial); } }}
                            role="button"
                            tabIndex={0}
                        >
                            <img
                                src={testimonial.photoUrl}
                                alt={testimonial.name}
                                className={styles.photo}
                                loading="lazy"
                                decoding="async"
                            />
                             <p className={styles.nameStyle}>{testimonial.name}</p>
                        </div>
                    ))}
                </div>
              </>
            )}
            {selectedTestimonial && (
                <div className={styles.modal} onClick={handleClose} role="presentation">
                    <div className={styles.modalContent} onClick={(e) => e.stopPropagation()} role="dialog" aria-modal="true">
                        <h3 style={{fontWeight:'bold' }}>{selectedTestimonial.name}</h3>
                        <p className={styles.commentStyle}>{textOf(selectedTestimonial)}</p>
                        <button type="button" className={styles.closeButton} onClick={handleClose}>
                            {ui.close}
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Testimonial;
