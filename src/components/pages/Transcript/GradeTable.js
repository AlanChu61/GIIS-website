import React, { useState, useEffect } from 'react';

const GRADE_TO_GPA = {
  'A+': { weighted: 4.0, unweighted: 4.0 },
  'A':  { weighted: 4.0, unweighted: 4.0 },
  'A-': { weighted: 3.7, unweighted: 3.7 },
  'B+': { weighted: 3.3, unweighted: 3.3 },
  'B':  { weighted: 3.0, unweighted: 3.0 },
  'B-': { weighted: 2.7, unweighted: 2.7 },
  'C+': { weighted: 2.3, unweighted: 2.3 },
  'C':  { weighted: 2.0, unweighted: 2.0 },
  'C-': { weighted: 1.7, unweighted: 1.7 },
  'D+': { weighted: 1.3, unweighted: 1.3 },
  'D':  { weighted: 1.0, unweighted: 1.0 },
  'F':  { weighted: 0.0, unweighted: 0.0 },
};

const EMPTY_ROW = { name: '', type: '', credits: '', grade: '', weightedGPA: '-', unweightedGPA: '-' };
const TOTALS_ROW = { ...EMPTY_ROW, name: 'Semester Totals' };

const DEFAULT_ROWS = [
  { ...EMPTY_ROW },
  { ...EMPTY_ROW },
  { ...EMPTY_ROW },
  { ...EMPTY_ROW },
  { ...TOTALS_ROW },
];

function calculateTotals(rows) {
  let totalWeighted = 0;
  let totalUnweighted = 0;
  let totalCredits = 0;

  rows.forEach((row) => {
    if (row.name === 'Semester Totals') return;
    const credits = parseFloat(row.credits) || 0;
    totalCredits += credits;
    if (row.weightedGPA !== '-' && row.unweightedGPA !== '-') {
      totalWeighted += row.weightedGPA * credits;
      totalUnweighted += row.unweightedGPA * credits;
    }
  });

  return {
    weightedGPA: totalCredits > 0 ? (totalWeighted / totalCredits).toFixed(2) : '-',
    unweightedGPA: totalCredits > 0 ? (totalUnweighted / totalCredits).toFixed(2) : '-',
    totalCredits,
  };
}

const cellStyle = {
  border: '1px solid black',
  fontSize: '6pt',
  fontFamily: 'Times New Roman, Times, serif',
  padding: '0 2px',
  lineHeight: '1',
};

const inputStyle = (isStatic) => ({
  width: '100%',
  fontSize: '6pt',
  fontFamily: 'Times New Roman, Times, serif',
  border: isStatic ? '1px solid black' : 'none',
  borderRadius: '4px',
});

const addButtonStyle = {
  border: 'none',
  backgroundColor: 'rgba(43, 61, 109, 0.8)',
  color: 'white',
  borderRadius: '50%',
  width: '20px',
  height: '20px',
  fontSize: '20px',
  cursor: 'pointer',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
};

function GradeTable({ semesterName, onTotalsUpdate, isStatic = false, initialRows = null, onRowsChange = null }) {
  const [rows, setRows] = useState(DEFAULT_ROWS.map((r) => ({ ...r })));

  useEffect(() => {
    if (initialRows && Array.isArray(initialRows)) {
      setRows(initialRows);
    }
  }, [initialRows]);

  useEffect(() => {
    if (onRowsChange) {
      onRowsChange(semesterName, rows);
    }
  }, [rows, semesterName, onRowsChange]);

  const handleChange = (index, field, value) => {
    setRows((prevRows) => {
      const newRows = prevRows.map((r) => ({ ...r }));

      if (field === 'name' && value.trim() === '') {
        newRows[index] = { ...EMPTY_ROW };
      } else {
        newRows[index][field] = value;

        if (field === 'grade' || field === 'credits' || field === 'type') {
          const gpa = GRADE_TO_GPA[newRows[index].grade?.toUpperCase()] || { weighted: '-', unweighted: '-' };
          const typeHasAP = newRows[index].type?.includes('AP') || false;
          const nameHasAP = newRows[index].name?.includes('AP') || false;

          newRows[index].unweightedGPA = gpa.unweighted;
          newRows[index].weightedGPA =
            typeHasAP && nameHasAP && gpa.unweighted !== '-'
              ? gpa.unweighted + 1
              : gpa.unweighted;
        }
      }

      const totals = calculateTotals(newRows);
      const totalsIdx = newRows.findIndex((r) => r.name === 'Semester Totals');
      if (totalsIdx !== -1) {
        const hasContent = newRows.some((r) => r.name !== 'Semester Totals' && r.name.trim() !== '');
        if (hasContent) {
          newRows[totalsIdx].weightedGPA = totals.weightedGPA;
          newRows[totalsIdx].unweightedGPA = totals.unweightedGPA;
          newRows[totalsIdx].totalCredits = totals.totalCredits.toFixed(1);
        } else {
          newRows[totalsIdx].weightedGPA = '-';
          newRows[totalsIdx].unweightedGPA = '-';
          newRows[totalsIdx].totalCredits = '';
        }
      }

      if (onTotalsUpdate) {
        onTotalsUpdate(semesterName, {
          weightedGPA: totals.weightedGPA,
          unweightedGPA: totals.unweightedGPA,
          totalCredits: totals.totalCredits,
        });
      }

      return newRows;
    });
  };

  const addRow = () => {
    setRows((prevRows) => {
      const totalsIdx = prevRows.findIndex((r) => r.name === 'Semester Totals');
      const before = prevRows.slice(0, totalsIdx);
      const after = prevRows.slice(totalsIdx);
      return [...before, { ...EMPTY_ROW }, ...after];
    });
  };

  return (
    <>
      <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '2px' }}>
        <thead>
          <tr>
            <td
              colSpan="6"
              style={{ textAlign: 'left', fontWeight: 'bold', fontSize: '6pt', fontFamily: 'Times New Roman, Times, serif', padding: '0 2px', lineHeight: '1' }}
            >
              {semesterName}
            </td>
          </tr>
          <tr>
            {['Course Name', 'Type', 'Credits', 'Grade', 'Weighted GPA', 'Unweighted GPA'].map((h) => (
              <th key={h} style={{ ...cellStyle, fontWeight: 'bold' }}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, index) => (
            <tr key={index}>
              <td style={{ ...cellStyle, width: '30%' }}>
                {row.name === 'Semester Totals' ? (
                  <span>Semester Totals</span>
                ) : (
                  <input
                    type="text"
                    value={row.name}
                    onChange={(e) => handleChange(index, 'name', e.target.value)}
                    style={inputStyle(isStatic)}
                    disabled={false}
                  />
                )}
              </td>

              <td style={{ ...cellStyle, width: '15%' }}>
                {row.name === 'Semester Totals' ? '' : (
                  <select
                    value={row.type}
                    onChange={(e) => handleChange(index, 'type', e.target.value)}
                    style={inputStyle(isStatic)}
                  >
                    <option value="">-</option>
                    <option value="Core">Core</option>
                    <option value="Core (AP)">Core (AP)</option>
                    <option value="Elective">Elective</option>
                  </select>
                )}
              </td>

              <td style={{ ...cellStyle, width: '10%' }}>
                {row.name === 'Semester Totals' ? row.totalCredits : (
                  <select
                    value={row.credits}
                    onChange={(e) => handleChange(index, 'credits', e.target.value)}
                    style={inputStyle(isStatic)}
                  >
                    <option value="">-</option>
                    <option value="0.5">0.5</option>
                    <option value="1.0">1.0</option>
                  </select>
                )}
              </td>

              <td style={{ ...cellStyle, width: '10%' }}>
                {row.name === 'Semester Totals' ? '' : (
                  <select
                    value={row.grade}
                    onChange={(e) => handleChange(index, 'grade', e.target.value)}
                    style={inputStyle(isStatic)}
                  >
                    <option value="">-</option>
                    {['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F'].map((g) => (
                      <option key={g} value={g}>{g}</option>
                    ))}
                  </select>
                )}
              </td>

              <td style={{ ...cellStyle, width: '10%' }}>{row.weightedGPA}</td>
              <td style={{ ...cellStyle, width: '10%' }}>{row.unweightedGPA}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button style={addButtonStyle} onClick={addRow}>+</button>
    </>
  );
}

export default GradeTable;
