import React from 'react';
import { Helmet } from 'react-helmet-async';

const SCHOOL_PHONE = '+1 (813) 501-5756';
const SCHOOL_SITE = 'https://genesisideas.school/';

function AdmissionMain({ language }) {
  const en = language === 'en';
  return (
    <section className="py-5">
      <Helmet>
        <title>{en ? 'Admission' : '入学'} | Genesis of Ideas International School</title>
        <meta
          name="description"
          content={en
            ? 'How to apply to Genesis of Ideas International School — requirements, timeline, and next steps.'
            : '创思国际学校入学申请、时间安排与后续步骤。'}
        />
      </Helmet>
      <div className="container col-lg-8">
        <h1 className="mb-4">{en ? 'Admission' : '入学申请'}</h1>
        <p className="lead">
          {en
            ? 'Thank you for your interest in Genesis of Ideas International School. Below is an overview of how to apply and what to expect. For the latest deadlines and forms, please contact our admissions office.'
            : '感谢您对创思国际学校（Genesis of Ideas International School）的关注。以下为申请流程概览。最新截止日期与申请表请直接联系招生办公室。'}
        </p>

        <h2 className="h4 mt-4">{en ? 'Application process' : '申请流程'}</h2>
        <ol className="mb-4">
          {en ? (
            <>
              <li>Submit an inquiry or application through our website or by email.</li>
              <li>Provide academic records and any required supporting documents.</li>
              <li>Complete an interview or placement discussion if requested.</li>
              <li>Receive an admissions decision and enrollment instructions.</li>
            </>
          ) : (
            <>
              <li>通过官网或电子邮件提交咨询或申请。</li>
              <li>提交成绩单及所需证明文件。</li>
              <li>视情况完成面谈或学业评估。</li>
              <li>收到录取结果与注册指引。</li>
            </>
          )}
        </ol>

        <h2 className="h4 mt-4">{en ? 'Contact admissions' : '联系招生'}</h2>
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
            ? 'Dates and requirements may change each term; please confirm with the school before applying.'
            : '每学期的日期与要求可能调整，报名前请与学校确认。'}
        </p>
      </div>
    </section>
  );
}

export default AdmissionMain;
