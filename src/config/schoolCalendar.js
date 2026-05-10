/**
 * GIIS Academic Calendar — single source of truth (2022 → present).
 *
 * Read by:
 *   - src/components/pages/SchoolProfile/SchoolProfilePage.js
 *     (Academic Calendar section in the printable profile PDF colleges receive)
 *   - src/components/pages/Parent/ParentDashboardDemo.js
 *     (Quick Links → "School calendar" + UpcomingFromCalendar widget)
 *
 * ─── What "academic calendar" means for an online async school ───
 *
 * GIIS is a fully online, asynchronous school. Students are not required to
 * attend on a fixed schedule — the Learn Portal is open 24/7, year-round.
 * What the calendar below ACTUALLY governs:
 *
 *   • Term start / end dates       — define which transcript a course
 *                                    counts toward (Fall vs Spring).
 *   • Final-exam window            — fixed dates so all students sit the
 *                                    exam on roughly the same week.
 *   • Grade release date           — when graded final exams + course
 *                                    grades become visible in the Portal.
 *   • Transcript issue date        — when the official semester transcript
 *                                    PDF is emailed to parents on file.
 *   • Diploma issue date           — when a graduating senior's diploma
 *                                    becomes VALID for college / employer
 *                                    verification. Same date as the
 *                                    /verify/<studentCode> QR goes live.
 *
 * "Winter break" and "summer break" are operational pauses for ADMIN ONLY
 * (no new course modules released, no advisor sync sessions, final exams
 * not scheduled). The Learn Portal stays OPEN — students who want to push
 * through holidays may continue submitting coursework and module work; it
 * just gets credited to the *next* term.
 *
 * ─── How to add a new academic year (each July) ───
 *
 * Dates are NOT computed by formula — they're hand-set so the admin can
 * absorb real-world drift (Labor Day landing day, religious observances,
 * hurricane makeup days, etc.).
 *
 *   Fall starts        ~3rd Monday of August         (~Aug 17–19)
 *   Fall ends          ~last weekday before Dec 22   (~Dec 18–19)
 *   Fall gradesReleased  fall.ends + 3 days
 *   Fall transcriptIssued  ~Jan 7–10 (after holidays)
 *   Spring starts      ~1st Monday of January        (~Jan 4–6)
 *   Spring ends        ~3rd or 4th Friday of May     (~May 21–23)
 *   Spring gradesReleased  spring.ends + 3 days
 *   Spring transcriptIssued  ~2 weeks after spring.ends (~Jun 10–12)
 *   Graduation ceremonyDate  1st Friday of June      (~Jun 4–6)
 *   Graduation diplomaIssued  same as ceremonyDate
 *   Graduation physicalMailed  ceremonyDate + 7 days
 *
 * Sanity-check: term ends land on weekdays; gradesReleased is strictly
 * after the term ends; graduation falls on a Friday.
 *
 * Florida Statute 1002.42 — private schools must complete ≥170 instructional
 * days. GIIS's two ~18-week semesters = ~180 days. Compliant.
 */

/**
 * Each academic year object:
 *
 *   label              "2025–2026"
 *   startsOn / endsOn  the outermost bookends (used for "today is in this year")
 *   fall, spring       term objects: starts, ends, gradesReleased, transcriptIssued, keyDates[]
 *   winterRecess       admin pause between terms (platform stays open)
 *   summerRecess       admin pause after spring (platform stays open)
 *   graduation         senior class diploma issuance, OR null for years before
 *                      the first cohort graduated
 *   notes              optional string describing anything special about this year
 */
export const ACADEMIC_YEARS = [
  {
    label: '2022–2023',
    startsOn: '2022-08-22',
    endsOn:   '2023-08-20',
    fall: {
      label: 'Fall Semester',
      starts: '2022-08-22',
      ends:   '2022-12-16',
      gradesReleased:   '2022-12-19',
      transcriptIssued: '2023-01-09',
      keyDates: [
        { date: '2022-12-05', label: 'Final-exam window opens' },
        { date: '2022-12-16', label: 'Fall semester closes · final exams due' },
      ],
    },
    winterRecess: { starts: '2022-12-19', ends: '2023-01-04' },
    spring: {
      label: 'Spring Semester',
      starts: '2023-01-09',
      ends:   '2023-05-19',
      gradesReleased:   '2023-05-22',
      transcriptIssued: '2023-06-09',
      keyDates: [
        { date: '2023-05-08', label: 'Final-exam window opens' },
        { date: '2023-05-19', label: 'Spring semester closes · final exams due' },
      ],
    },
    summerRecess: { starts: '2023-05-22', ends: '2023-08-20' },
    graduation: null,  // founding year — no senior cohort yet
    notes: 'Founding academic year. Class of 2026 entered as Grade 9.',
  },
  {
    label: '2023–2024',
    startsOn: '2023-08-21',
    endsOn:   '2024-08-18',
    fall: {
      label: 'Fall Semester',
      starts: '2023-08-21',
      ends:   '2023-12-15',
      gradesReleased:   '2023-12-18',
      transcriptIssued: '2024-01-08',
      keyDates: [
        { date: '2023-12-04', label: 'Final-exam window opens' },
        { date: '2023-12-15', label: 'Fall semester closes · final exams due' },
      ],
    },
    winterRecess: { starts: '2023-12-18', ends: '2024-01-07' },
    spring: {
      label: 'Spring Semester',
      starts: '2024-01-08',
      ends:   '2024-05-17',
      gradesReleased:   '2024-05-20',
      transcriptIssued: '2024-06-07',
      keyDates: [
        { date: '2024-05-06', label: 'Final-exam window opens' },
        { date: '2024-05-17', label: 'Spring semester closes · final exams due' },
      ],
    },
    summerRecess: { starts: '2024-05-20', ends: '2024-08-18' },
    graduation: null,  // Class of 2026 was in Grade 10
    notes: 'School completed formal Florida DOE registration (F.S. 1002.42) in 2024.',
  },
  {
    label: '2024–2025',
    startsOn: '2024-08-19',
    endsOn:   '2025-08-17',
    fall: {
      label: 'Fall Semester',
      starts: '2024-08-19',
      ends:   '2024-12-20',
      gradesReleased:   '2024-12-23',
      transcriptIssued: '2025-01-08',
      keyDates: [
        { date: '2024-12-09', label: 'Final-exam window opens' },
        { date: '2024-12-20', label: 'Fall semester closes · final exams due' },
      ],
    },
    winterRecess: { starts: '2024-12-23', ends: '2025-01-05' },
    spring: {
      label: 'Spring Semester',
      starts: '2025-01-06',
      ends:   '2025-05-23',
      gradesReleased:   '2025-05-27',
      transcriptIssued: '2025-06-13',
      keyDates: [
        { date: '2025-05-12', label: 'Final-exam window opens' },
        { date: '2025-05-23', label: 'Spring semester closes · final exams due' },
      ],
    },
    summerRecess: { starts: '2025-05-27', ends: '2025-08-17' },
    graduation: null,  // Class of 2026 was in Grade 11
    notes: 'First full year operating as a Florida DOE-registered private school.',
  },
  {
    label: '2025–2026',
    startsOn: '2025-08-18',
    endsOn:   '2026-08-16',
    fall: {
      label: 'Fall Semester',
      starts: '2025-08-18',
      ends:   '2025-12-19',
      gradesReleased:   '2025-12-22',
      transcriptIssued: '2026-01-09',
      keyDates: [
        { date: '2025-12-08', label: 'Final-exam window opens' },
        { date: '2025-12-19', label: 'Fall semester closes · final exams due' },
      ],
    },
    winterRecess: { starts: '2025-12-22', ends: '2026-01-04' },
    spring: {
      label: 'Spring Semester',
      starts: '2026-01-05',
      ends:   '2026-05-22',
      gradesReleased:   '2026-05-25',  // server/prisma/seed.js gates Spring 2026 grades on this date
      transcriptIssued: '2026-06-12',
      keyDates: [
        { date: '2026-05-11', label: 'Final-exam window opens' },
        { date: '2026-05-22', label: 'Spring semester closes · final exams due' },
      ],
    },
    summerRecess: { starts: '2026-05-25', ends: '2026-08-16' },
    graduation: {
      ceremonyDate:   '2026-06-05',   // virtual ceremony
      diplomaIssued:  '2026-06-05',   // diploma valid from this date · /verify QR live
      physicalMailed: '2026-06-12',   // signed paper diploma mailed
      classLabel:     'Class of 2026',
    },
    notes: 'First graduating class. Four seniors expected to graduate on June 5, 2026.',
  },
  {
    label: '2026–2027',
    startsOn: '2026-08-17',
    endsOn:   '2027-08-15',
    fall: {
      label: 'Fall Semester',
      starts: '2026-08-17',
      ends:   '2026-12-18',
      gradesReleased:   '2026-12-21',
      transcriptIssued: '2027-01-08',
      keyDates: [
        { date: '2026-12-07', label: 'Final-exam window opens' },
        { date: '2026-12-18', label: 'Fall semester closes · final exams due' },
      ],
    },
    winterRecess: { starts: '2026-12-21', ends: '2027-01-03' },
    spring: {
      label: 'Spring Semester',
      starts: '2027-01-04',
      ends:   '2027-05-21',
      gradesReleased:   '2027-05-24',
      transcriptIssued: '2027-06-11',
      keyDates: [
        { date: '2027-05-10', label: 'Final-exam window opens' },
        { date: '2027-05-21', label: 'Spring semester closes · final exams due' },
      ],
    },
    summerRecess: { starts: '2027-05-24', ends: '2027-08-15' },
    graduation: {
      ceremonyDate:   '2027-06-04',
      diplomaIssued:  '2027-06-04',
      physicalMailed: '2027-06-11',
      classLabel:     'Class of 2027',
    },
    notes: null,
  },
];

/** Returns the academic year object containing `today` (YYYY-MM-DD). */
export function getCurrentAcademicYear(today = new Date().toISOString().slice(0, 10)) {
  return (
    ACADEMIC_YEARS.find((y) => today >= y.startsOn && today <= y.endsOn) ||
    ACADEMIC_YEARS[ACADEMIC_YEARS.length - 1]
  );
}

/** Returns the term ('fall' | 'spring' | 'winter-recess' | 'summer-recess') for `today`. */
export function getCurrentTerm(today = new Date().toISOString().slice(0, 10)) {
  const yr = getCurrentAcademicYear(today);
  if (today >= yr.fall.starts && today <= yr.fall.ends)               return { name: 'fall',   data: yr.fall };
  if (today >= yr.winterRecess.starts && today <= yr.winterRecess.ends) return { name: 'winter-recess', data: yr.winterRecess };
  if (today >= yr.spring.starts && today <= yr.spring.ends)            return { name: 'spring', data: yr.spring };
  if (today >= yr.summerRecess.starts && today <= yr.summerRecess.ends) return { name: 'summer-recess', data: yr.summerRecess };
  return { name: 'fall', data: yr.fall };
}

/** Format an ISO date as 'May 22, 2026' (en) or '2026年5月22日' (zh). */
export function formatDate(iso, locale = 'en') {
  if (!iso) return '';
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
    { date: yr.fall.gradesReleased,   label: 'Fall grades released',          term: 'Fall' },
    { date: yr.fall.transcriptIssued, label: 'Fall transcript issued',        term: 'Fall' },
    ...yr.spring.keyDates.map((k) => ({ ...k, term: 'Spring' })),
    { date: yr.spring.gradesReleased,   label: 'Spring grades released',      term: 'Spring' },
    { date: yr.spring.transcriptIssued, label: 'Year-end transcript issued',  term: 'Spring' },
  ];
  if (yr.graduation) {
    all.push(
      { date: yr.graduation.ceremonyDate,   label: `Graduation · ${yr.graduation.classLabel}`,    term: 'Graduation' },
      { date: yr.graduation.physicalMailed, label: 'Physical diplomas mailed',                    term: 'Graduation' },
    );
  }
  return all.filter((e) => e.date >= today).sort((a, b) => a.date.localeCompare(b.date)).slice(0, n);
}

/** Years that had a graduating class — for the public-facing "Class of XXXX" history. */
export function getGraduatingYears() {
  return ACADEMIC_YEARS.filter((y) => y.graduation);
}
