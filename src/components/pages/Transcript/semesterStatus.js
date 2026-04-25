/**
 * Semester status logic.
 *
 * All status is computed from graduationYear + a reference date.
 * - For the live admin/student view: referenceDate = today
 * - For official PDF export: referenceDate = transcriptDate
 *
 * US academic calendar cutoffs used here:
 *   Fall semester:   Sep 1 – Dec 20
 *   Spring semester: Jan 10 – May 25
 */

export const SEMESTER_STATUS = {
  COMPLETED: 'completed',
  IN_PROGRESS: 'in_progress',
  UPCOMING: 'upcoming',
};

/**
 * Returns the school year end-year for a given date.
 * School year 2025-2026 ends in 2026 → if month >= Sep, next year.
 */
function schoolYearEndYear(date) {
  const month = date.getMonth() + 1; // 1-12
  return month >= 9 ? date.getFullYear() + 1 : date.getFullYear();
}

/**
 * Computes the current grade (9-12) for a student.
 * Returns null if graduationYear is not set or student is outside 9-12.
 */
export function computeCurrentGrade(graduationYear, referenceDate = new Date()) {
  if (!graduationYear) return null;
  const grade = 12 - (graduationYear - schoolYearEndYear(referenceDate));
  if (grade < 9 || grade > 12) return null;
  return grade;
}

/**
 * Returns the calendar year when a given (grade, term) semester occurs.
 *   Spring of grade G ends in: graduationYear - (12 - G)
 *   Fall   of grade G ends in: graduationYear - (12 - G) - 1
 */
function semesterCalendarYear(grade, term, graduationYear) {
  const springYear = graduationYear - (12 - grade);
  return term === 'spring' ? springYear : springYear - 1;
}

/**
 * Returns 'completed' | 'in_progress' | 'upcoming' for a single semester.
 *
 * @param {number} grade         9 | 10 | 11 | 12
 * @param {'fall'|'spring'} term
 * @param {number} graduationYear
 * @param {Date}   referenceDate
 */
export function getSemesterStatus(grade, term, graduationYear, referenceDate = new Date()) {
  if (!graduationYear) return SEMESTER_STATUS.UPCOMING;

  const calYear = semesterCalendarYear(grade, term, graduationYear);
  const month = referenceDate.getMonth() + 1;
  const year = referenceDate.getFullYear();

  if (term === 'spring') {
    // Spring runs Jan 10 – May 25 of calYear
    if (year > calYear) return SEMESTER_STATUS.COMPLETED;
    if (year === calYear && month > 5) return SEMESTER_STATUS.COMPLETED;
    if (year === calYear && month >= 1) return SEMESTER_STATUS.IN_PROGRESS;
    return SEMESTER_STATUS.UPCOMING;
  } else {
    // Fall runs Sep 1 – Dec 20 of calYear
    if (year > calYear) return SEMESTER_STATUS.COMPLETED;
    if (year === calYear && month >= 9) return SEMESTER_STATUS.IN_PROGRESS;
    return SEMESTER_STATUS.UPCOMING;
  }
}

/**
 * Maps a TRANSCRIPT_SEMESTER_KEYS entry to { grade, term }.
 * e.g. 'Grade 11 - Fall Semester' → { grade: 11, term: 'fall' }
 */
export function parseSemesterKey(key) {
  const m = key.match(/Grade (\d+) - (Fall|Spring) Semester/);
  if (!m) return null;
  return { grade: parseInt(m[1], 10), term: m[2].toLowerCase() };
}

/**
 * Returns status for every semester key given a graduationYear and referenceDate.
 * Result: { [key]: 'completed' | 'in_progress' | 'upcoming' }
 */
export function getAllSemesterStatuses(semesterKeys, graduationYear, referenceDate = new Date()) {
  const result = {};
  for (const key of semesterKeys) {
    const parsed = parseSemesterKey(key);
    if (!parsed) {
      result[key] = SEMESTER_STATUS.UPCOMING;
    } else {
      result[key] = getSemesterStatus(parsed.grade, parsed.term, graduationYear, referenceDate);
    }
  }
  return result;
}
