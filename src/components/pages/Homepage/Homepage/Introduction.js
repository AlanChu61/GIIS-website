import React from 'react';

function Introduction({ language }) {
    return (
        <div className="container">
            <h2>{language === 'zh' ? '学校介绍' : 'School Introduction'}</h2>
            <div>
                {language === 'zh' ? (
                    <p>
                        我们的学校是一所全线上、全球化的现代化学府，致力于提供世界一流的教育，吸引了全球各地的精英学生。我们的教育模式打破了传统教育的地域限制，学生可以在任何时间、任何地点，接受顶尖的教育资源。
                        我们提供双学位课程，学生可以同时获得不同学校的学位，增强他们的学术和职业竞争力。通过这种方式，学生不仅能深入理解所学专业，还能跨学科学习，培养多元化的知识体系和跨领域的思维能力。
                        我们将人工智能和最新的前沿科技深度融合到教学中，创造沉浸式的学习体验。这些先进的技术工具不仅丰富了教学内容，还使得学习过程更加生动有趣。我们的在线平台提供了互动式的学习体验，使学生能够随时随地与教师和同学交流，获得实时反馈。
                        我们非常注重学生的个人发展，致力于培养学生的兴趣和特长。通过个性化的教学方法和丰富多样的课程设置，我们帮助每一位学生发现自己的潜能，激发他们的学习热情。我们提供广泛的选修课和课外活动，涵盖艺术、科学、技术、经济等多个领域，让学生在全面发展的同时，找到自己的兴趣所在。
                        此外，我们还注重学生的综合素质培养，开设领导力培训、创新创业课程等，帮助学生在未来的职业生涯中脱颖而出。我们的目标是培养具备国际视野、创新思维和社会责任感的未来领导者。
                    </p>
                ) : (
                    <p>
                        Our school is a fully online, globalized modern institution dedicated to providing world-class education, attracting elite students from around the world. Our educational model breaks the geographical constraints of traditional education, allowing students to access top-notch educational resources anytime, anywhere.
                        We offer dual degree programs, enabling students to earn degrees from different schools simultaneously, enhancing their academic and career competitiveness. This approach allows students to gain a deep understanding of their chosen fields while also engaging in interdisciplinary studies, fostering a diverse knowledge base and cross-disciplinary thinking skills.
                        We deeply integrate artificial intelligence and the latest cutting-edge technologies into our teaching, creating immersive learning experiences. These advanced technological tools enrich the teaching content and make the learning process more engaging and enjoyable. Our online platform provides an interactive learning experience, allowing students to communicate with teachers and classmates anytime, anywhere, and receive real-time feedback.
                        We place great emphasis on the personal development of our students, aiming to cultivate their interests and talents. Through personalized teaching methods and a diverse range of courses, we help each student discover their potential and ignite their passion for learning. We offer a wide variety of elective courses and extracurricular activities across multiple fields such as arts, science, technology, and economics, enabling students to develop comprehensively while finding their own interests.
                        Additionally, we focus on the holistic development of our students by offering leadership training, innovation, and entrepreneurship courses, helping them stand out in their future careers. Our goal is to nurture future leaders with a global perspective, innovative thinking, and a sense of social responsibility.
                    </p>
                )}
            </div>
        </div >
    );
}

export default Introduction;
