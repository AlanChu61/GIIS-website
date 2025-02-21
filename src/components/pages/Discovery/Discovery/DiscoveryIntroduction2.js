import React from 'react';
import FacultyGraduates from './FacultyGraduates.js';

function DiscoveryIntroduction2({ language }) {

    const headlineStyle = {
        marginTop: '60px',
        color: 'rgba(0, 0, 0, 1)',
        width: '60%',
        paddingLeft: '12%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        fontSize: '55px',
    };
 
    const headlineStyle2 = {
        marginTop: '60px',
        color: 'rgba(0, 0, 0, 1)',
        width: '60%',
        paddingLeft: '12%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        fontSize: '55px',
    };


    const headlineStyle3 = {
        marginTop: '60px',
        color: 'rgba(0, 0, 0, 1)',
        width: '60%',
        paddingLeft: '12%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        fontSize: '55px',
    };

    const container = {
        color: 'rgba(0, 0, 0, 1)',
        width: '90%',
        height: '50%',
        paddingLeft: '12%',
        fontFamily: 'Inter, sans-serif',
        fontSize: '30px',
        wordWrap: 'break-word',
        lineHeight: '1.25',
    };

    const container2 = {
        color: 'rgba(0, 0, 0, 0.8)',
        width: '85%',
        height: '50%',
        paddingLeft: '12%',
        fontFamily: 'Inter, sans-serif',
        fontSize: '25px',
        wordWrap: 'break-word',
    };

    const container3 = {
        marginTop: '40px',
        color: 'rgba(0, 0, 0, 0.8)',
        width: '85%',
        height: '50%',
        paddingLeft: '12%',
        fontFamily: 'Inter, sans-serif',
        fontSize: '25px',
        wordWrap: 'break-word',
    };

    const container4 = {
        marginTop: '40px',
        color: 'rgba(0, 0, 0, 0.8)',
        width: '85%',
        height: '70%',
        paddingLeft: '12%',
        fontFamily: 'Inter, sans-serif',
        fontSize: '25px',
        wordWrap: 'break-word',
        marginBottom: '55px',
    };

    
    return (
      <>
        <div style={headlineStyle}>
          <p>Core values</p>
        </div>

        <div style={container}>
          <p>{language === 'en' ? 'PERSONALIZED LEARNING' : '个人化学习'}</p>  
          <p>{language === 'en' ? 'COMPREHENSIVE DEVELOPMENT' : '全面性发展'}</p>
          <p>{language === 'en' ? 'INTERNATIONAL PERSPECTIVE' : '国际视野'}</p>
        </div>

        <div style={headlineStyle2}>
          <p>Misiion</p>
        </div>

        <div style={container2}>
          {language === 'zh' ? (
                    <p>
                        GIIS的教育理念是启发潜能并培养领袖。我们重视学生的个人发展和全面成长，提供多样化的学习机会。透过提供丰富的资源并鼓励积极探索，我们营造出一个让学生茁壮成长的学习环境。
                    </p>
                ) : (
                    <p>
                        GIIS's educational philosophy is to inspire potential and cultivate leaders. We prioritize individual student development and overall growth, offering a diverse range of learning opportunities. By providing abundant resources and encouraging active exploration, we foster a learning environment where students can thrive.
                    </p>
                )}
        </div>

        <div style={container3}>
          {language === 'zh' ? (
                    <p>
                        透过密切的师生互动，学生们获得个性化的指导与支持。我们也强调领导力、全球视野和创业精神的培养，以装备学生应对未来的挑战。我们相信，在这样一个充满关怀的环境中，学生们将成为具备强烈社会责任感的全球公民。
                    </p>
                ) : (
                    <p>
                        Through close teacher-student interactions, students receive personalized guidance and support. We also emphasize the development of leadership, global vision, and entrepreneurial spirit to equip our students for the challenges of the future. We believe that in this nurturing environment, our students will become global citizens with a strong sense of social responsibility.

                    </p>
                )}
        </div>

        <div style={headlineStyle3}>
          <p>Faculty&Graduates</p>
        </div>
                    
        <div className="container-fluid">
          <div className="card-body">
             <FacultyGraduates />
          </div>
        </div>

        <div style={container4}>
           {language === 'zh' ? (
                    <p>
                        我们的师资和毕业生来自全球顶尖学府。这些世界一流大学的联系，不仅彰显了我们师资的卓越，也展现了我们毕业生的非凡成就。我们致力于汇聚来自这些著名学府的专家与学者，为学生提供最高品质的教育体验。
                    </p>
                ) : (
                    <p>
                        Our faculty and graduates come from leading institutions around the world. This connection to world-class universities not only highlights the excellence of our faculty but also reflects the remarkable achievements of our graduates. We are committed to bringing together experts and scholars from these prestigious institutions to provide our students with the highest-quality educational experience.
                    </p>
                )}
        </div>   
      </>
   );
}

export default DiscoveryIntroduction2;
