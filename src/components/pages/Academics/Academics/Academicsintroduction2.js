import React, { useRef, useState,useEffect} from 'react';
import img from '../../../../img/Academics/Math.jpg';

function Academicsintroduction2({ language }) {

    const courses = [
        { title: 'IGCSE', 
         content: {
           en: 'Challenge yourself with the globally recognized Pearson Edexcel International GCSEs.',
           zh: '接受全球认可的培生爱德思国际普通中等教育证书 (International GCSEs) 挑战吧！'
          },
         content2: {
            en: 'These courses provide a comprehensive curriculum, designed to develop students analytical skills, creativity, and problem-solving abilities across various subjects, preparing them for future academic success.',
            zh: '这些课程提供全面的课程设计，旨在培养学生的分析能力、创造力和解决问题的能力，为未来的学术成功做好准备。'
         }
        },
        {
        title: 'A-Level',
        content: {
            en: 'Our A-Level courses build on the foundation of IGCSE, providing a rigorous academic experience that sharpens critical thinking, enhances subject mastery, and prepares students for the demands of university-level education.',
            zh: '我们的 A-Level 课程以 IGCSE 为基础，提供严谨的学术体验，提升批判性思维、深化学科掌握，并为大学教育的挑战做好准备。'
         },
        content2: {
            en: 'With a broad range of subjects to choose from, students can tailor their studies to suit their academic and career aspirations.',
            zh: '通过多样的学科选择，学生可以根据自己的学术和职业目标量身定制学习计划。'
         }
        },
        {
        title: 'AP',
        content: {
            en: 'Empower yourself with the globally recognized Advanced Placement Program.',
            zh: '通过全球认可的高级课程 (AP) 计划提升自我。'
         },
        content2: {
            en: 'Our AP courses offer college-level studies in high school, preparing students for AP exams and building skills for university and beyond.',
            zh: '我们的 AP 课程在高中阶段提供大学水平的学习，帮助学生准备 AP 考试并为大学及以后的发展奠定基础。'
         }
        }
   ];

    const extendedCourses = [...courses, ...courses, ...courses]; // 將課程清單擴展為三倍以實現無限滾動效果
    const scrollRef = useRef(null);
    const [isDragging, setIsDragging] = useState(false);
    const [startX, setStartX] = useState(0);
    const [scrollLeft, setScrollLeft] = useState(0);
    const childWidth = scrollRef.current
    ? scrollRef.current.scrollWidth / extendedCourses.length
    : 0;
    
    useEffect(() => {
     const scrollWidth = scrollRef.current.scrollWidth;
     const childWidth = scrollWidth / extendedCourses.length;
     scrollRef.current.scrollLeft = childWidth * courses.length;
        
     const scrollElement = scrollRef.current; // 保存 scrollRef.current 的当前值

     const handleScroll = () => {
        if (scrollElement.scrollLeft <= 0) {
            scrollElement.scrollLeft = childWidth * courses.length;
        } else if (scrollElement.scrollLeft >= childWidth * (courses.length * 2)) {
            scrollElement.scrollLeft = childWidth * courses.length;
        }
     };

     scrollElement.addEventListener('scroll', handleScroll);
     return () => {
        scrollElement.removeEventListener('scroll', handleScroll); // 确保清理时使用同一个元素
     };
    }, [extendedCourses.length, courses.length, childWidth]);

    const handleMouseDown = (e) => {
        setIsDragging(true);
        setStartX(e.pageX - scrollRef.current.offsetLeft);
        setScrollLeft(scrollRef.current.scrollLeft);
        e.preventDefault();
    };

    const handleMouseUp = () => {
        if (isDragging) {
            setIsDragging(false);
        }
    };

    const handleMouseMove = (e) => {
        if (!isDragging) return;

        const x = e.pageX - scrollRef.current.offsetLeft;
        const walk = (x - startX) * 1.5;
        scrollRef.current.scrollLeft = scrollLeft - walk;
    };

    const frameStyle = {
        position: 'absolute',
        left: '140%',
        bottom: '-12px',
        display: 'flex',
        overflow: 'hidden', // 隱藏滾動條
        clipPath: 'inset(0)',
        width: '60vh',
        cursor: isDragging ? 'grabbing' : 'grab',
    };

  const courseBoxStyle = {
    minWidth: '50vh', // 水平填充寬度
    height: '570px', // 固定高度
    backgroundColor: 'black',
    color: 'white',
    display: 'flex',
    flexDirection: 'column', // 垂直排列內容
    justifyContent: 'space-between', // 標題與箭頭居上下兩側
    alignItems: 'center',
    padding: '40px', // 增加內邊距
    textAlign: 'center', // 文字居中
    boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.5)',
};

  const titleStyle = {
    position: 'relative',
    fontSize: '3rem',
    fontWeight: 'bold',
    marginBottom: '10px',
};

  const contentStyle = {
    justifyContent: 'center',
    textAlign: 'left',
    fontSize: '1.2rem',
    lineHeight: '1.2',
    marginTop: '25%',
};

  const content2Style = {
    position: 'relative',
    justifyContent: 'center',
    textAlign: 'left',
    fontSize: '1.2rem',
    lineHeight: '1.2',
    marginTop: '10%',
};

   const spaceStyle= {
    backgroundColor: 'white',
    minWidth: '15vh',
    height: '570px',
};
 
   const headlineStyle = {
        marginTop: '100px',
        color: 'rgba(0, 0, 0, 1)',
        width: '100%',
        paddingLeft: '10%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        fontSize: '70px',
        lineHeight: '1',
    };

   const lineStyle = {
       position: 'absolute',
       margin: '10px auto',
       marginLeft: '20%',
       width: '100px',
       height: '3px',
       backgroundColor: 'white',
    };

    const courseintroductionStyle = {
        position: 'relative',
        color: 'rgba(0, 0, 0, 1)',
        width: '48%',
        paddingLeft: '10%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'normal',
        fontSize: '30px',
        lineHeight: '1.5',
        marginTop: '35px',
    };

    const lineStyle2 = {
        position: 'absolute',
        width: '35%', // Adjust width according to your needs
        height: '4px',
        paddingLeft: '10%',
        backgroundColor: 'rgba(0, 0, 0, 1)', 
        marginTop: '35px',
    };

    const yellowSquareStyle = {
        position: 'absolute',
        width: '300px',  // Adjust size as needed
        height: '300px', // Adjust size as needed
        backgroundColor: 'rgba(213, 168, 54, 1)',   
        left: '105%',
        top: language === 'zh' ? '20%' : '50%',
    };

    const headline2Style = {
        marginTop: '150px',
        color: 'rgba(0, 0, 0, 1)',
        width: '100%',
        paddingLeft: '10%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        fontSize: '70px',
        lineHeight: '1',
    };

    const containerStyle = {
        position: 'relative',
        display: 'flex',
        justifyContent: 'center', // 水平居中
        marginTop: '5%', // 與導航欄保持距離
        width: '90%',
        height: '100%',
        paddingLeft: '10%',
        marginBottom: '5%',
    };

    const imageStyle = {
        width: '100%', // 保持容器的寬度
        height: '400px', // 固定高度
        objectFit: 'cover',
        filter: 'blur(6px)',
        zIndex: '100',
    };

     const overlaycontainerStyle = {
        position: 'absolute',
        display: 'flex',
        justifyContent: 'flex-end', 
        bottom: '-10%',
        width: '100%',
        paddingLeft: '15%',
        zIndex: '200',
    };

    const overlayStyle = {
        width: '100%', // 保持容器的寬度
        height: '100px', // 固定高度
        backgroundColor: 'rgba(210, 180, 140, 0.7)', // 半透明棕色
        color: 'white',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        cursor: 'pointer',
    };

    const overlayTextStyle = {
        position: 'absolute',
        fontSize: '150px',
        fontWeight: 'bold',
        fontFamily: 'Inter, sans-serif',
        bottom:'0',
        paddingLeft: '30%',
    };

  const arrowContainerStyle = {
    position: 'absolute',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '70px', // 设置圆框的大小
    height: '70px',
    border: '3px solid white', 
    borderRadius: '50%',  
    marginLeft: '25%',
    marginTop: '1%',
    marginBottom: '5%',
};

const arrowContainerStyle2 = {
    position: 'absolute',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '100px', // 设置圆框的大小
    height: '100px',
    border: '5px solid white', 
    borderRadius: '50%',      
    marginLeft: '70%',
    marginTop: '-10%',
};

const arrowStyle = {
    fontSize: '2rem',
    fontWeight: 'bold',
    alignItems: 'center',
    cursor: 'pointer',
};

    
const arrowStyle2 = {
    fontSize: '60px',
    color: 'white',            // 设置箭头颜色为黑色
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100%',
    height: '100%',
};

const handleNavigation = () => {
        window.open('https://moodles.genesisideas.school/', '_blank'); // 新分頁開啟網址
    };

    return (
      <>
        <div style={headlineStyle}>
          <p>COURSE</p>
          <p>CATALOG</p>
        </div>
        
        <div style={courseintroductionStyle}>
           {language === 'zh' ? (
                    <p>
                       我们的学校提供多元化的国际课程，包括英国IGCSE、A-Level和美国AP课程，满足学生的学术需求。这些课程为提升学生进入世界顶尖大学的机会奠定了坚实基础。通过深化知识和培养批判性思维能力，我们的学生为在全球学术舞台上取得优异成绩做好了充分准备。
                    </p>
                ) : (
                    <p>
                       Our school offers a diverse range of international programs, including the British IGCSE, A-level, and American AP courses, meeting students' academic needs. These programs provide a strong foundation for boosting university admissions chances to top institutions worldwide. By deepening their knowledge and developing critical thinking skills, our students are well-prepared to excel on the global academic stage.
                    </p>
                )}  
          <div style={lineStyle2}></div> 
          <div style={yellowSquareStyle}></div>

          <div
            ref={scrollRef}
            style={frameStyle}
            onMouseDown={handleMouseDown}
            onMouseMove={handleMouseMove}
            onMouseUp={handleMouseUp}
            onMouseLeave={handleMouseUp}
          >
            {extendedCourses.map((courses, index) => (
              <>
                <div key={index} style={courseBoxStyle}>
                 <div>
                    <h2 style={titleStyle}>{courses.title}</h2>
                    <div style={lineStyle}></div>
                    <p style={contentStyle}>{courses.content[language]}</p>
                    <p style={content2Style}>{courses.content2[language]}</p>
                    <div style={arrowContainerStyle}>
                     <span style={arrowStyle}>→</span>
                    </div>
                 </div>
                </div>
                <div style={spaceStyle}></div>
              </>
             ))}
          </div>
         </div>
            
         <div style={headline2Style}>
           <p>SUBJECTS</p>
         </div>
              
         <div style={containerStyle}>
          <img src={img} alt="Math" style={imageStyle} />
          <div style={overlaycontainerStyle}>
            <div style={overlayStyle} onClick={handleNavigation}>
             <p style={overlayTextStyle}>MATH</p>
              <div style={arrowContainerStyle2}>
               <span style={arrowStyle2}>→</span>
              </div>
            </div>  
          </div>
         </div>
      </>
   );
}

export default Academicsintroduction2;
