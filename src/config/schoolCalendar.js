/**
 * GIIS Academic Calendar — single source of truth.
 *
 * Read by:
 *   - src/components/pages/SchoolProfile/SchoolProfilePage.js
 *     (Academic Calendar section in the printable profile PDF colleges receive)
 *   - src/components/pages/Parent/ParentDashboardDemo.js
 *     (Quick Links → "School calendar" pulls upcoming events from here)
 *   - any future "weekly digest" email may surface upcoming events
 *
 * Rules:
 *   - All dates are calendar dates in America/New_York time (Florida).
 *     Async students worldwide can read them as deadlines in their local time.
 *   - "Term Closes" = the last day a course's coursework + final exam is accepted
 *     toward that semester's transcript. Anything submitted after closes onto the
 *     NEXT term's transcript.
 *   - "Transcript Issued" = the date semester transcripts are finalized + emailed
 *     to parents on file. Used for college applications.
 *   - "Diploma Issue Date" = when senior diplomas are issued (digital + physical).
 *
 * To add a new academic year, append a new object to ACADEMIC_YEARS preserving
 * the same shape. The site auto-uses whichever year's `startsOn` ≤ today ≤ `endsOn`.
 *
 * Florida private school calendar reference: Florida Statute 1002.42
 * private schools must complete at least 170 instructional days. Our two
 * 18-week semesters total ~180 days, exceeding the requirement.
 *
 * ─── How to add a new academic year (do this every July) ───
 *
 * Calendar dates are NOT computed by formula — they're hand-set per year so
 * the admin can absorb real-world drift (which weekday Labor Day lands on,
 * religious holidays, makeup days, hurricane closures, etc.).
 *
 * Pattern to follow when adding the next academic year:
 *
 *   Fall starts        ~3rd Monday of August         (~Aug 17–19)
 *   Fall ends          ~last weekday before Dec 22   (~Dec 18–19)
 *   Fall gradesReleased  fall.ends + 3 days
 *   Fall transcriptIssued  ~Jan 7–10 (after winter break)
 *   Winter break       ~Dec 22 → ~Jan 4
 *   Spring starts      ~1st Monday of January        (~Jan 4–6)
 *   Spring ends        ~3rd or 4th Friday of May     (~May 21–23)
 *   Spring gradesReleased  spring.ends + 3 days
 *   Spring transcriptIssued  ~2 weeks after spring.ends (~Jun 10–12)
 *   Summer break       spring.ends + 1 day → next fall.starts − 1 day
 *   Graduation ceremonyDate  1st Friday of June      (~Jun 4–6)
 *   Graduation diplomaIssued  same as ceremonyDate
 *   Graduation physicalMailed  ceremonyDate + 7 days
 *
 * Then sanity-check: each fall.ends/spring.ends should land on a weekday;
 * gradesReleased / transcriptIssued must be strictly after their term end;
 * graduation ceremony falls on a Friday (parents travel weekend).
 */

export const ACADEMIC_YEARS = [
  {
    label: '2025–2026',
    startsOn: '2025-08-18', // Fall term starts
    endsOn:   '2026-06-05', // diploma ceremony / year ends
    fall: {
      label: 'Fall Semester',
      starts: '2025-08-18',
      ends:   '2025-12-19',
      gradesReleased: '2025-12-22',     // ~3 days after term closes — when Learn Portal shows final grades
      transcriptIssued: '2026-01-09',   // mid-year transcript (after winter break) — emailed to parents
      keyDates: [
        { date: '2025-09-01', label: 'Labor Day · no new releases' },
        { date: '2025-10-13', label: 'Mid-term progress reports' },
        { date: '2025-11-26', label: 'Thanksgiving break begins (3 days)' },
        { date: '2025-12-08', label: 'Final-exam window opens' },
        { date: '2025-12-19', label: 'Fall semester closes · final exams due' },
      ],
    },
    winterBreak: { starts: '2025-12-22', ends: '2026-01-04' },
    spring: {
      label: 'Spring Semester',
      starts: '2026-01-05',
      ends:   '2026-05-22',
      gradesReleased: '2026-05-25',    // ~3 days after term closes — server/prisma/seed.js gates Spring 2026 grades on this date
      transcriptIssued: '2026-06-12',   // year-end transcript
      keyDates: [
        { date: '2026-01-19', label: 'Martin Luther King Jr. Day · no new releases' },
        { date: '2026-02-16', label: 'Presidents Day · no new releases' },
        { date: '2026-03-16', label: 'Spring break begins (5 days)' },
        { date: '2026-03-23', label: 'Mid-term progress reports' },
        { date: '2026-05-11', label: 'Final-exam window opens' },
        { date: '2026-05-22', label: 'Spring semester closes · final exams due' },
      ],
    },
    summerBreak: { starts: '2026-05-23', ends: '2026-08-16' },
    graduation: {
      ceremonyDate:    '2026-06-05', // virtual ceremony for the Class of 2026
      diplomaIssued:   '2026-06-05', // digital diploma + verification QR live same day
      physicalMailed:  '2026-06-12', // physical signed diploma mailed to graduates
      classLabel:      'Class of 2026',
    },
  },
  {
    label: '2026–2027',
    startsOn: '2026-08-17',
    endsOn:   '2027-06-04',
    fall: {
      label: 'Fall Semester',
      starts: '2026-08-17',
      ends:   '2026-12-18',
      transcriptIssued: '2027-01-08',
      keyDates: [
        { date: '2026-09-07', label: 'Labor Day · no new releases' },
        { date: '2026-10-12', label: 'Mid-term progress reports' },
        { date: '2026-11-25', label: 'Thanksgiving break begins (3 days)' },
        { date: '2026-12-07', label: 'Final-exam window opens' },
        { date: '2026-12-18', label: 'Fall semester closes' },
      ],
    },
    winterBreak: { starts: '2026-12-21', ends: '2027-01-03' },
    spring: {
      label: 'Spring Semester',
      starts: '2027-01-04',
      ends:   '2027-05-21',
      transcriptIssued: '2027-06-11',
      keyDates: [
        { date: '2027-01-18', label: 'Martin Luther King Jr. Day · no new releases' },
        { date: '2027-02-15', label: 'Presidents Day · no new releases' },
        { date: '2027-03-15', label: 'Spring break begins (5 days)' },
        { date: '2027-03-22', label: 'Mid-term progress reports' },
        { date: '2027-05-10', label: 'Final-exam window opens' },
        { date: '2027-05-21', label: 'Spring semester closes' },
      ],
    },
    summerBreak: { starts: '2027-05-22', ends: '2027-08-15' },
    graduation: {
      ceremonyDate:    '2027-06-04',
      diplomaIssued:   '2027-06-04',
      physicalMailed:  '2027-06-11',
      classLabel:      'Class of 2027',
    },
  },
];

/** Returns the academic year object containing `today` (YYYY-MM-DD). */
export function getCurrentAcademicYear(today = new Date().toISOString().slice(0, 10)) {
  return (
    ACADEMIC_YEARS.find((y) => today >= y.startsOn && today <= y.endsOn) ||
    ACADEMIC_YEARS[0]
  );
}

/** Returns the term ('fall' | 'spring' | 'break' | 'summer') for `today`. */
export function getCurrentTerm(today = new Date().toISOString().slice(0, 10)) {
  const yr = getCurrentAcademicYear(today);
  if (today >= yr.fall.starts && today <= yr.fall.ends)         return { name: 'fall',   data: yr.fall };
  if (today >= yr.winterBreak.starts && today <= yr.winterBreak.ends) return { name: 'break',  data: yr.winterBreak };
  if (today >= yr.spring.starts && today <= yr.spring.ends)     return { name: 'spring', data: yr.spring };
  if (today >= yr.summerBreak.starts && today <= yr.summerBreak.ends) return { name: 'summer', data: yr.summerBreak };
  return { name: 'fall', data: yr.fall };
}

/** Format an ISO date as 'May 22, 2026' (en) or '2026年5月22日' (zh). */
export function formatDate(iso, locale = 'en') {
  const [y, m, d] = iso.split('-').map(Number);
  if (locale === 'zh') return `${y} 年 ${m} 月 ${d} 日`;
  const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  return `${months[m-1]} ${d}, ${y}`;
}

/** Get up to N upcoming events across the current academic year, sorted by date. */
export function getUpcomingEvents(today = new Date().toISOString().slice(0, 10), n = 4) {
  const yr = getCurrentAcademicYear(today);
  const all = [
    ...yr.fall.keyDates.map((k) => ({ ...k, term: 'Fall' })),
    { date: yr.fall.transcriptIssued, label: 'Fall transcript issued', term: 'Fall' },
    { date: yr.winterBreak.starts, label: 'Winter break begins', term: 'Break' },
    { date: yr.winterBreak.ends, label: 'Winter break ends',   term: 'Break' },
    ...yr.spring.keyDates.map((k) => ({ ...k, term: 'Spring' })),
    { date: yr.spring.transcriptIssued, label: 'Year-end transcript issued', term: 'Spring' },
    { date: yr.graduation.ceremonyDate, label: `Graduation · ${yr.graduation.classLabel}`, term: 'Graduation' },
    { date: yr.graduation.physicalMailed, label: 'Physical diplomas mailed', term: 'Graduation' },
  ];
  return all.filter((e) => e.date >= today).sort((a, b) => a.date.localeCompare(b.date)).slice(0, n);
}
