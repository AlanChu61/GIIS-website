import React from 'react';
import { Link } from 'react-router-dom';

/**
 * LessonPreview — homepage "Watch a real lesson" section.
 *
 * Embeds one full GIIS-produced lesson directly on the marketing surface so a
 * prospective parent never has to click through to YouTube to judge teaching
 * quality. The 80-second DemoEmbed sells the experience; LessonPreview sells
 * the actual product.
 *
 * Default lesson: Algebra I — Module 4 (One-Step & Two-Step Equations). Chosen
 * because the boba-shop hook is concrete, math is what Chinese parents
 * implicitly trust, and the pilot has been the most-viewed sample.
 *
 * Props (all optional — defaults shown below):
 *   language       'en' | 'zh'  — required
 *   youtubeId      YouTube video ID (default: Algebra I M4)
 *   course         course name shown in pill (default: 'Algebra I')
 *   moduleNumber   integer (default: 4)
 *   moduleTitle    {en, zh}     — title of the lesson
 *   description    {en, zh}     — one-line "why this lesson is representative"
 */
function LessonPreview({
  language,
  youtubeId = 'AMF3Wj4cycs',
  course = 'Algebra I',
  moduleNumber = 4,
  moduleTitle = {
    en: 'Solving One-Step and Two-Step Equations',
    zh: '解一步与两步方程',
  },
  description = {
    en: 'Same teacher voice, same pacing, same difficulty as every other lesson on the platform. Not a trailer — the full ~6-minute lesson, including the pause-and-try moment.',
    zh: '与平台上每节课同一位老师、同一节奏、同一难度。这不是预告片，而是约 6 分钟的完整课程，包含课中暂停练习。',
  },
}) {
  const isEn = language !== 'zh';

  return (
    <section style={{
      background: '#f4f6fb',
      padding: '80px 0',
      fontFamily: 'Inter, sans-serif',
    }}>
      <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '0 6%' }}>

        {/* Eyebrow + heading */}
        <div style={{ textAlign: 'center', marginBottom: '36px' }}>
          <p style={{
            color: '#2b3d6d',
            fontSize: '12px',
            fontWeight: 700,
            letterSpacing: '2.5px',
            textTransform: 'uppercase',
            margin: '0 0 12px',
          }}>
            {isEn ? 'Watch a real lesson' : '看一节真实课'}
          </p>
          <h2 style={{
            fontSize: 'clamp(28px, 4vw, 46px)',
            fontWeight: 800,
            color: '#1a1a2e',
            lineHeight: 1.1,
            margin: '0 0 14px',
            letterSpacing: '-0.01em',
          }}>
            {isEn
              ? 'This is what your child will actually learn'
              : '这就是你的孩子真正会学到的'}
          </h2>
          <p style={{
            fontSize: 'clamp(14px, 1.4vw, 16px)',
            color: '#5c6578',
            maxWidth: '640px',
            margin: '0 auto',
            lineHeight: 1.65,
          }}>
            {isEn ? description.en : description.zh}
          </p>
        </div>

        {/* Lesson card — pill metadata + 16:9 embed */}
        <div style={{
          maxWidth: '900px',
          margin: '0 auto',
          background: '#fff',
          borderRadius: '14px',
          padding: '24px 24px 28px',
          boxShadow: '0 24px 60px -12px rgba(26, 26, 46, 0.18), 0 8px 20px -8px rgba(26, 26, 46, 0.10)',
          border: '1px solid #e0e6f0',
        }}>
          {/* Metadata pill row */}
          <div style={{
            display: 'flex',
            flexWrap: 'wrap',
            alignItems: 'center',
            gap: '10px',
            marginBottom: '18px',
          }}>
            <span style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              background: '#1a1a2e',
              color: '#d5a836',
              fontSize: '11px',
              fontWeight: 800,
              letterSpacing: '1.5px',
              textTransform: 'uppercase',
              padding: '5px 11px',
              borderRadius: '999px',
            }}>
              <span style={{
                display: 'inline-block',
                width: '6px',
                height: '6px',
                borderRadius: '50%',
                background: '#d5a836',
              }} />
              {course}
            </span>
            <span style={{
              fontSize: '12px',
              fontWeight: 700,
              color: '#5c6578',
              letterSpacing: '0.5px',
            }}>
              {isEn ? `Module ${moduleNumber}` : `第 ${moduleNumber} 模块`}
            </span>
            <span style={{ color: '#cfd5e0', fontWeight: 700 }}>·</span>
            <span style={{
              fontSize: '14px',
              fontWeight: 600,
              color: '#1a1a2e',
            }}>
              {isEn ? moduleTitle.en : moduleTitle.zh}
            </span>
          </div>

          {/* 16:9 YouTube embed */}
          <div style={{
            position: 'relative',
            width: '100%',
            aspectRatio: '16 / 9',
            borderRadius: '10px',
            overflow: 'hidden',
            background: '#000',
          }}>
            <iframe
              src={`https://www.youtube.com/embed/${youtubeId}?rel=0&modestbranding=1`}
              title={`${course} — ${isEn ? moduleTitle.en : moduleTitle.zh}`}
              loading="lazy"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                height: '100%',
                border: 'none',
              }}
            />
          </div>

          {/* English disclosure — set correct expectation */}
          <p style={{
            fontSize: '12px',
            color: '#7a8294',
            margin: '14px 0 0',
            textAlign: 'center',
            lineHeight: 1.5,
          }}>
            {isEn
              ? 'Lessons are taught in English with English captions. This is by design — students need English exposure for AP exams and US college applications.'
              : '课程为英文授课，配英文字幕。这是刻意设计——学生需要充分的英文输入，才能应对 AP 考试与美国大学申请。'}
          </p>
        </div>

        {/* CTA underneath the card */}
        <div style={{
          display: 'flex',
          gap: '14px',
          justifyContent: 'center',
          flexWrap: 'wrap',
          marginTop: '32px',
        }}>
          <Link
            to="/academics"
            style={{
              padding: '13px 28px',
              borderRadius: '10px',
              background: '#2b3d6d',
              color: '#fff',
              fontWeight: 700,
              fontSize: '14px',
              textDecoration: 'none',
              boxShadow: '0 4px 14px rgba(43, 61, 109, 0.25)',
              transition: 'transform 0.15s, box-shadow 0.15s',
            }}
            onMouseEnter={e => {
              e.currentTarget.style.transform = 'translateY(-1px)';
              e.currentTarget.style.boxShadow = '0 6px 18px rgba(43, 61, 109, 0.35)';
            }}
            onMouseLeave={e => {
              e.currentTarget.style.transform = 'none';
              e.currentTarget.style.boxShadow = '0 4px 14px rgba(43, 61, 109, 0.25)';
            }}
          >
            {isEn ? 'Browse all 40+ courses →' : '浏览全部 40+ 门课程 →'}
          </Link>
          <a
            href="https://www.youtube.com/@GenesisOfIdeasInternational"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              padding: '13px 28px',
              borderRadius: '10px',
              border: '2px solid #d4d8e0',
              color: '#2b3d6d',
              fontWeight: 700,
              fontSize: '14px',
              textDecoration: 'none',
              transition: 'border-color 0.15s, background 0.15s',
            }}
            onMouseEnter={e => {
              e.currentTarget.style.borderColor = '#2b3d6d';
              e.currentTarget.style.background = '#fff';
            }}
            onMouseLeave={e => {
              e.currentTarget.style.borderColor = '#d4d8e0';
              e.currentTarget.style.background = 'transparent';
            }}
          >
            {isEn ? 'See more lessons on YouTube →' : '在 YouTube 看更多课程 →'}
          </a>
        </div>
      </div>
    </section>
  );
}

export default LessonPreview;
