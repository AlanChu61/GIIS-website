import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { clearAdminSession, getAdminSession } from '../../../api/authStorage';
import { getApiBase } from '../../../config/apiBase';

const API_BASE = getApiBase();

export default function AdminDashboard({ language }) {
  const isEn = language === 'en';
  const copy = {
    title: isEn ? 'Students' : '學生列表',
    subtitle: isEn
      ? 'Full access: roster, profile fields, and grades (open a student to edit the transcript).'
      : '完整權限：學生列表、個資欄位與成績（開啟學生即可編輯成績單）。',
    logout: isEn ? 'Log out' : '登出',
    home: isEn ? 'Site home' : '回到網站',
    newStudent: isEn ? 'New student' : '新增學生',
    loading: isEn ? 'Loading…' : '載入中…',
    thName: isEn ? 'Name' : '姓名',
    thLoginEmail: isEn ? 'Login email' : '登入信箱',
    thBirth: isEn ? 'Birth' : '生日',
    thLocation: isEn ? 'Location' : '地點',
    thGuardian: isEn ? 'Guardian' : '監護人',
    thSemesters: isEn ? 'Semesters' : '學期數',
    thUpdated: isEn ? 'Updated' : '更新時間',
    defaultNewStudentName: isEn ? 'New student' : '新學生',
    createFailed: isEn ? 'Create failed' : '建立失敗',
  };
  const [students, setStudents] = useState([]);
  const [err, setErr] = useState('');
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  const session = getAdminSession();

  useEffect(() => {
    if (!session) {
      navigate('/login', { replace: true });
      return;
    }
    if (!API_BASE) {
      setErr(isEn ? 'Missing REACT_APP_API_URL' : '缺少 REACT_APP_API_URL');
      setLoading(false);
      return;
    }
    (async () => {
      try {
        const r = await fetch(`${API_BASE}/api/students`, {
          credentials: 'include',
        });
        const data = await r.json().catch(() => ({}));
        if (r.status === 401) {
          clearAdminSession();
          navigate('/login', { replace: true });
          return;
        }
        if (!r.ok) throw new Error(data.error || (isEn ? 'Failed to load students' : '載入學生列表失敗'));
        setStudents(data.students || []);
      } catch (e) {
        setErr(e.message);
      } finally {
        setLoading(false);
      }
    })();
  }, [session, navigate, isEn]);

  async function logout() {
    if (API_BASE) {
      await fetch(`${API_BASE}/api/auth/logout`, { method: 'POST', credentials: 'include' }).catch(() => {});
    }
    clearAdminSession();
    navigate('/login', { replace: true });
  }

  async function createStudent() {
    if (!API_BASE || !session) return;
    setErr('');
    try {
      const r = await fetch(`${API_BASE}/api/students`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ name: copy.defaultNewStudentName }),
      });
      const data = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(data.error || copy.createFailed);
      navigate(`/admin/transcript/${data.student.id}`);
    } catch (e) {
      setErr(e.message);
    }
  }

  if (!session) return null;

  return (
    <div className="container py-4">
      <div className="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
        <div>
          <h1 className="h4 mb-0">{copy.title}</h1>
          <p className="text-muted small mb-0 mt-1">
            {copy.subtitle}
          </p>
        </div>
        <div>
          <button type="button" className="btn btn-outline-secondary btn-sm me-2" onClick={logout}>
            {copy.logout}
          </button>
          <Link to="/" className="btn btn-link btn-sm">
            {copy.home}
          </Link>
        </div>
      </div>
      {err && <div className="alert alert-warning py-2">{err}</div>}
      <button type="button" className="btn btn-primary mb-3" onClick={createStudent}>
        {copy.newStudent}
      </button>
      {loading ? (
        <p className="text-muted">{copy.loading}</p>
      ) : (
        <div className="table-responsive shadow-sm rounded border bg-white">
          <table className="table table-sm table-hover align-middle mb-0">
            <thead className="table-light">
              <tr>
                <th scope="col">{copy.thName}</th>
                <th scope="col">{copy.thLoginEmail}</th>
                <th scope="col">{copy.thBirth}</th>
                <th scope="col">{copy.thLocation}</th>
                <th scope="col">{copy.thGuardian}</th>
                <th scope="col" className="text-center">
                  {copy.thSemesters}
                </th>
                <th scope="col">{copy.thUpdated}</th>
                <th scope="col" />
              </tr>
            </thead>
            <tbody>
              {students.map((s) => (
                <tr key={s.id}>
                  <td>
                    <strong>{s.name || '(unnamed)'}</strong>
                    <div className="small text-muted" style={{ fontFamily: 'var(--giis-font-mono, monospace)' }}>
                      {s.id.slice(0, 10)}…
                    </div>
                  </td>
                  <td>{s.loginEmail || '—'}</td>
                  <td>{s.birthDate || '—'}</td>
                  <td>
                    {[s.city, s.province].filter(Boolean).join(', ') || '—'}
                  </td>
                  <td className="small">{s.parentGuardian || '—'}</td>
                  <td className="text-center">{s.semesterCount ?? 0}</td>
                  <td className="small text-nowrap">
                    {s.updatedAt ? new Date(s.updatedAt).toLocaleString() : '—'}
                  </td>
                  <td className="text-end text-nowrap">
                    <Link className="btn btn-sm btn-outline-primary" to={`/admin/transcript/${s.id}`}>
                      {isEn ? 'View & edit' : '檢視／編輯'}
                    </Link>
                  </td>
                </tr>
              ))}
              {students.length === 0 && (
                <tr>
                  <td colSpan={8} className="text-muted text-center py-4">
                    {isEn
                      ? <>No students yet — create one or run <code>node prisma/seed.js</code> in <code>server/</code>.</>
                      : <>目前沒有學生資料 — 你可以先建立一筆，或在 <code>server/</code> 執行 <code>node prisma/seed.js</code>。</>}
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
