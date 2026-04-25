import React, { useState } from 'react';
import { Helmet } from 'react-helmet-async';
import { Link, Navigate, useParams } from 'react-router-dom';
import TranscriptContent from '../Transcript/TranscriptContent.js';
import { getAdminSession } from '../../../api/authStorage';

export default function AdminTranscriptPage({ language }) {
  const { studentId } = useParams();
  const session = getAdminSession();
  const [mode, setMode] = useState('view'); // 'view' | 'edit'
  const isEn = language === 'en';
  const copy = {
    back: isEn ? '← Back to student list' : '← 返回學生列表',
    modeLabel: isEn ? 'Mode:' : '模式：',
    view: isEn ? 'View' : '檢視',
    edit: isEn ? 'Edit' : '編輯',
    hintView: isEn ? 'Use View for export/submission.' : '提交／匯出請用「檢視」。',
    hintEdit: isEn ? 'Save only appears in Edit.' : '只有「編輯」才會顯示儲存。',
  };

  if (!session) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div id="content">
      <Helmet>
        <title>Admin — Transcript | Genesis of Ideas International School</title>
      </Helmet>
      <div className="container-fluid py-2">
        <p className="mb-2">
          <Link to="/admin">{copy.back}</Link>
        </p>
        <div className="d-flex flex-wrap gap-2 align-items-center mb-2">
          <span className="small text-muted">{copy.modeLabel}</span>
          <div className="btn-group" role="group" aria-label="Transcript mode">
            <button
              type="button"
              className={`btn btn-sm ${mode === 'view' ? 'btn-primary' : 'btn-outline-primary'}`}
              onClick={() => setMode('view')}
            >
              {copy.view}
            </button>
            <button
              type="button"
              className={`btn btn-sm ${mode === 'edit' ? 'btn-primary' : 'btn-outline-primary'}`}
              onClick={() => setMode('edit')}
            >
              {copy.edit}
            </button>
          </div>
          <span className="small text-muted">
            {mode === 'view' ? copy.hintView : copy.hintEdit}
          </span>
        </div>
        <TranscriptContent
          language={language}
          viewerRole="admin"
          studentId={studentId}
          mode={mode}
        />
      </div>
    </div>
  );
}
