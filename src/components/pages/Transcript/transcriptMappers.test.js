import { courseApiToGradeRows, gradeRowsToApiCourses, TRANSCRIPT_SEMESTER_KEYS } from './transcriptMappers';

describe('TRANSCRIPT_SEMESTER_KEYS', () => {
  test('has exactly 8 semesters in grade order', () => {
    expect(TRANSCRIPT_SEMESTER_KEYS).toHaveLength(8);
    expect(TRANSCRIPT_SEMESTER_KEYS[0]).toContain('Grade 9');
    expect(TRANSCRIPT_SEMESTER_KEYS[7]).toContain('Grade 12');
  });
});

describe('courseApiToGradeRows', () => {
  test('null/empty input returns 4 blank rows + totals', () => {
    const rows = courseApiToGradeRows(null);
    expect(rows).toHaveLength(5); // 4 blank + 1 totals
    expect(rows[4].name).toBe('Semester Totals');
  });

  test('maps API fields to grade row shape', () => {
    const api = [{
      courseName: 'Math',
      courseType: 'Core',
      credits: 1.0,
      letterGrade: 'A',
      weightedGpa: 4.0,
      unweightedGpa: 4.0,
    }];
    const rows = courseApiToGradeRows(api);
    const mathRow = rows.find(r => r.name === 'Math');
    expect(mathRow).toBeDefined();
    expect(mathRow.type).toBe('Core');
    expect(mathRow.credits).toBe('1');
    expect(mathRow.grade).toBe('A');
    expect(mathRow.weightedGPA).toBe(4.0);
    expect(mathRow.unweightedGPA).toBe(4.0);
  });

  test('pads to at least 4 data rows', () => {
    const rows = courseApiToGradeRows([{ courseName: 'Math', credits: 1.0, letterGrade: 'A', weightedGpa: 4.0, unweightedGpa: 4.0 }]);
    const dataRows = rows.filter(r => r.name !== 'Semester Totals');
    expect(dataRows.length).toBeGreaterThanOrEqual(4);
  });

  test('Semester Totals row has correct credit sum', () => {
    const api = [
      { courseName: 'Math', credits: 1.0, letterGrade: 'A', weightedGpa: 4.0, unweightedGpa: 4.0 },
      { courseName: 'English', credits: 1.0, letterGrade: 'B', weightedGpa: 3.0, unweightedGpa: 3.0 },
    ];
    const rows = courseApiToGradeRows(api);
    const totals = rows.find(r => r.name === 'Semester Totals');
    expect(totals.totalCredits).toBe('2.0');
    expect(totals.weightedGPA).toBe('3.50');
  });

  test('normalizes "-" and null GPA values', () => {
    const api = [{ courseName: 'PE', credits: 0.5, letterGrade: '', weightedGpa: null, unweightedGpa: null }];
    const rows = courseApiToGradeRows(api);
    const peRow = rows.find(r => r.name === 'PE');
    expect(peRow.weightedGPA).toBe('-');
    expect(peRow.unweightedGPA).toBe('-');
  });
});

describe('gradeRowsToApiCourses', () => {
  test('strips Semester Totals row', () => {
    const rows = [
      { name: 'Math', type: 'Core', credits: '1.0', grade: 'A', weightedGPA: 4.0, unweightedGPA: 4.0 },
      { name: 'Semester Totals', type: '', credits: '', grade: '', weightedGPA: '3.50', unweightedGPA: '3.50' },
    ];
    const api = gradeRowsToApiCourses(rows);
    expect(api).toHaveLength(1);
    expect(api[0].courseName).toBe('Math');
  });

  test('strips empty-name rows', () => {
    const rows = [
      { name: '', type: '', credits: '', grade: '', weightedGPA: '-', unweightedGPA: '-' },
      { name: 'Math', type: 'Core', credits: '1.0', grade: 'A' },
    ];
    const api = gradeRowsToApiCourses(rows);
    expect(api).toHaveLength(1);
  });

  test('maps row fields to API shape', () => {
    const rows = [{ name: 'Physics', type: 'Core (AP)', credits: '1.0', grade: 'B+' }];
    const api = gradeRowsToApiCourses(rows);
    expect(api[0]).toEqual({
      courseName: 'Physics',
      courseType: 'Core (AP)',
      credits: '1.0',
      letterGrade: 'B+',
    });
  });
});
