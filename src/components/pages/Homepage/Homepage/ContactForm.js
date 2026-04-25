import React from "react";

function ContactForm({ language = 'en' }) {
    const isEn = language === 'en';
    return (
        <div className="container">
            <div className="row justify-content-center">
                <div className="col-md-8 col-lg-6">
                    <h2 id="contact" className="text-center">
                        {isEn ? 'Contact Us' : '联系我们'}
                    </h2>
                    <div className="form-group">
                        <form name="contact" method="post" data-netlify="true">
                            <input type="hidden" name="form-name" value="contact" />
                            <p hidden>
                                <label>
                                    {isEn ? 'Do not fill this out if you are human: ' : '不要填写这个字段如果你是人类: '}
                                    <input name="bot-field" />
                                </label>
                            </p>
                            <div className="mb-3">
                                <label htmlFor="studentName" className="form-label">{isEn ? 'Student name' : '学生姓名'}</label>
                                <input type="text" id="studentName" name="studentName" className="form-control" required />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="parentWeChat" className="form-label">{isEn ? 'Parent WeChat ID' : '家长微信号'}</label>
                                <input type="text" id="parentWeChat" name="parentWeChat" className="form-control" required />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="email" className="form-label">{isEn ? 'Contact email' : '联系邮箱'}</label>
                                <input type="email" id="email" name="email" className="form-control" required />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="course" className="form-label">{isEn ? 'Courses enrolled' : '所学课程'}</label>
                                <input type="text" id="course" name="course" className="form-control" required />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="grade" className="form-label">{isEn ? 'Grade applying for' : '学生入学年级'}</label>
                                <select id="grade" name="grade" className="form-select" required>
                                    <option value="9">9</option>
                                    <option value="10">10</option>
                                    <option value="11">11</option>
                                    <option value="12">12</option>
                                </select>
                            </div>
                            <div className="mb-3">
                                <label htmlFor="message" className="form-label">{isEn ? 'Message' : '留言'}</label>
                                <textarea
                                    id="message"
                                    name="message"
                                    className="form-control"
                                    placeholder={isEn ? 'Enter your message' : '请在此输入您的留言'}
                                    required
                                />
                            </div>
                            <div className="text-center">
                                <button type="submit" className="btn btn-primary">{isEn ? 'Submit' : '提交'}</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ContactForm;
