import React from 'react';
import { Helmet } from 'react-helmet-async';

const SCHOOL_PHONE = '+1 (813) 501-5756';
const SCHOOL_SITE = 'https://genesisideas.school/';

function SupportMain({ language }) {
  const en = language === 'en';
  return (
    <section className="py-5">
      <Helmet>
        <title>{en ? 'Student support' : '学生支持'} | Genesis of Ideas International School</title>
        <meta
          name="description"
          content={en
            ? 'Student support at Genesis of Ideas International School — advising, wellbeing, and academic resources.'
            : '创思国际学校学生支持服务：学业辅导、身心健康与资源说明。'}
        />
      </Helmet>
      <div className="container col-lg-8">
        <h1 className="mb-4">{en ? 'Student support' : '学生支持'}</h1>
        <p className="lead">
          {en
            ? 'We are committed to helping every learner succeed. Our team connects students and families with academic guidance and wellbeing resources in a fully online environment.'
            : '我们致力于协助每位学生成长。团队为线上学习环境中的学生与家庭提供学业指导与身心健康相关资源。'}
        </p>

        <h2 className="h4 mt-4">{en ? 'What we offer' : '服务内容'}</h2>
        <ul className="mb-4">
          {en ? (
            <>
              <li>Academic advising and course planning</li>
              <li>Check-ins for progress and goal-setting</li>
              <li>Referrals and resources for wellbeing and study skills</li>
            </>
          ) : (
            <>
              <li>学业咨询与选课规划</li>
              <li>学习进度与目标追踪</li>
              <li>身心健康与学习技巧相关资源转介</li>
            </>
          )}
        </ul>

        <h2 className="h4 mt-4">{en ? 'Contact' : '联系方式'}</h2>
        <p className="mb-1">
          {en ? 'Phone: ' : '电话：'}
          <a href={`tel:${SCHOOL_PHONE.replace(/\s/g, '')}`}>{SCHOOL_PHONE}</a>
        </p>
        <p className="mb-0">
          {en ? 'Website: ' : '网站：'}
          <a href={SCHOOL_SITE} target="_blank" rel="noopener noreferrer">{SCHOOL_SITE}</a>
        </p>
        <p className="text-muted small mt-3">
          {en
            ? 'For Moodle access, use the Moodle link in the site header.'
            : 'Moodle 学习平台入口请使用网站顶部的 Moodle 链接。'}
        </p>
      </div>
    </section>
  );
}

export default SupportMain;
