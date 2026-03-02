import React, {useState}  from 'react';

function GradeTableG12SS({ semesterName, onTotalsUpdate, onSemesterUpdate, isStatic = false}) {
  const [rows, setRows] = useState([
    { name: "", type: "", credits:"" , grade: "", weightedGPA: "-", unweightedGPA: "-" },
    { name: "", type: "", credits:"" , grade: "", weightedGPA: "-", unweightedGPA: "-" },
    { name: "", type: "", credits:"" , grade: "", weightedGPA: "-", unweightedGPA: "-" },
    { name: "", type: "", credits:"" , grade: "", weightedGPA: "-", unweightedGPA: "-" },
    { name: "Semester Totals", type: "", credits:"" , grade: "", weightedGPA: "-", unweightedGPA: "-" },
  ]);


  const gradeToGpa = {
    'A+': { weighted: 4.0, unweighted: 4.0 },
    'A': { weighted: 4.0, unweighted: 4.0 },
    'A-': { weighted: 3.7, unweighted: 3.7 },
    'B+': { weighted: 3.3, unweighted: 3.3 },
    'B': { weighted: 3.0, unweighted: 3.0 },
    'B-': { weighted: 2.7, unweighted: 2.7 },
    'C+': { weighted: 2.3, unweighted: 2.3 },
    'C': { weighted: 2.0, unweighted: 2.0 },
    'C-': { weighted: 1.7, unweighted: 1.7 },
    'D+': { weighted: 1.3, unweighted: 1.3 },
    'D': { weighted: 1.0, unweighted: 1.0 },
    'F': { weighted: 0.0, unweighted: 0.0 },
  };
  
  const calculateTotals = (updatedRows) => {
    let totalWeightedGPA = 0;
    let totalUnweightedGPA = 0;
    let totalCredits = 0;

    updatedRows.forEach((row) => {
    if (row.name !== "Semester Totals") {
      const credits = parseFloat(row.credits) || 0;
      totalCredits += credits;

      if (row.weightedGPA !== "-" && row.unweightedGPA !== "-") {
        totalWeightedGPA += row.weightedGPA * credits;
        totalUnweightedGPA += row.unweightedGPA * credits;
      }
    }
    });

    const weightedGPA = totalCredits > 0 ? (totalWeightedGPA / totalCredits).toFixed(2) : "-";
    const unweightedGPA = totalCredits > 0 ? (totalUnweightedGPA / totalCredits).toFixed(2) : "-";

    return { weightedGPA, unweightedGPA, totalCredits };
  }; 



 const handleGradeChange = (index, field, value) => {
  
  setRows((prevRows) => {
    const newRows = [...prevRows];

    newRows[index][field] = value;

    if (field === "name" && value.trim() === "") {
      newRows[index] = {
        name: "",
        type: "",
        credits: "",
        grade: "",
        weightedGPA: "-",
        unweightedGPA: "-"
      };
    } else if (field === "grade" || field === "credits" || field === "type") {
      const gpa = gradeToGpa[newRows[index].grade?.toUpperCase()] || { weighted: "-", unweighted: "-" };
      const typeHasAP = newRows[index].type?.includes("AP") || false;
      const nameHasAP = newRows[index].name?.includes("AP") || false;

      if (typeHasAP && nameHasAP) {
        newRows[index].unweightedGPA = gpa.unweighted;
        newRows[index].weightedGPA = gpa.unweighted !== "-" ? gpa.unweighted + 1 : "-";
      } else {
        newRows[index].unweightedGPA = gpa.unweighted;
        newRows[index].weightedGPA = gpa.unweighted;
      }
    }

    const totals = calculateTotals(newRows);
    const totalsIndex = newRows.findIndex((row) => row.name === "Semester Totals");
    if (totalsIndex !== -1) {
      if (newRows.some((row) => row.name !== "Semester Totals" && row.name.trim() !== "")) {
        newRows[totalsIndex].weightedGPA = totals.weightedGPA;
        newRows[totalsIndex].unweightedGPA = totals.unweightedGPA;
        newRows[totalsIndex].totalCredits = totals.totalCredits.toFixed(1);
      } else {
        newRows[totalsIndex].weightedGPA = "-";
        newRows[totalsIndex].unweightedGPA = "-";
        newRows[totalsIndex].totalCredits = "";
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
    const newRow = { name: "", type: "", credits: "", grade: "", weightedGPA: "-", unweightedGPA: "-" };
    const totalsIndex = prevRows.findIndex((row) => row.name === "Semester Totals");
    const beforeTotals = prevRows.slice(0, totalsIndex);
    const afterTotals = prevRows.slice(totalsIndex);
    return [...beforeTotals, newRow, ...afterTotals];
  });
};

 const addButtonStyle = {
  border: "none", 
  backgroundColor: "rgba(43, 61, 109, 0.8)",
  color: "white", 
  borderRadius: "50%", 
  width: "20px", 
  height: "20px",
  fontSize: "20px", 
  cursor: "pointer", 
  display: "flex", 
  justifyContent: "center",
  alignItems: "center", 
};


  return (
   <>
    <table style={{ width: "100%", borderCollapse: "collapse", marginBottom: "2px" }}>
      <thead>
        <tr>
          <td colSpan="6" style={{ textAlign: "left", fontWeight: "bold", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>
            Grade 12 - Spring Semester(In Progress)
          </td>
        </tr>
        <tr>
          <th style={{ border: "1px solid black", fontWeight: "bold", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>Course Name</th>
          <th style={{ border: "1px solid black", fontWeight: "bold", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>Type</th>
          <th style={{ border: "1px solid black", fontWeight: "bold", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>Credits</th>
          <th style={{ border: "1px solid black", fontWeight: "bold", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>Grade</th>
          <th style={{ border: "1px solid black", fontWeight: "bold", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>Weighted GPA</th>
          <th style={{ border: "1px solid black", fontWeight: "bold", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>Unweighted GPA</th>
        </tr>
      </thead>
      <tbody>
        {rows.map((row, index) => (
        <tr key={index}>
            <td style={{ border: "1px solid black", fontSize: "6pt", width: "30%", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>
             {row.name === "Semester Totals" ? (
              <span>Semester Totals</span>
              ) : (
              <input
                type="text"
                value={row.name}
                onChange={(e) => handleGradeChange(index, "name", e.target.value) }
                style={{ width: "100%", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", border: isStatic ? "1px solid black" : "none", borderRadius: "4px" }}
                disabled={row.name === "Semester Totals"}
              />
             )}
            </td>
                  
            <td style={{ border: "1px solid black", fontSize: "6pt", width: "15%", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>
             {row.name === "Semester Totals" ? (
               ""
              ) : (
              <select
                value={row.type}
                onChange={(e) => handleGradeChange(index, "type", e.target.value)}
                style={{ width: "100%", fontSize: "6pt", fontFamily: "Times New Roman, Times, serif", border: isStatic ? "1px solid black" : "none", borderRadius: "4px" }}
                disabled={row.name === "Semester Totals"}
              >
                <option value="">-</option>
                <option value="Core">Core</option>
                <option value="Core (AP)">Core (AP)</option>
                <option value="Elective">Elective</option>
              </select>
             )}
            </td>
                
            <td style={{ border: "1px solid black", fontSize: "6pt", width: "10%", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>
             {row.name === "Semester Totals" ? (
              row.totalCredits
              ) : (
                <select
                 value={row.credits}
                 onChange={(e) => handleGradeChange(index, "credits", e.target.value)}
                 style={{
                  width: "100%",
                  fontSize: "6pt",
                  fontFamily: "Times New Roman, Times, serif",
                  border: isStatic ? "1px solid black" : "none",
                  borderRadius: "4px",
                  }}
                  disabled={row.name === "Semester Totals"}
                  >
                   <option value="">-</option>
                   <option value="0.5">0.5</option>
                   <option value="1.0">1.0</option>
                 </select>
              )}
            </td>
                
            <td style={{ border: "1px solid black", fontSize: "6pt", width: "10%", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>
              {row.name === "Semester Totals" ? (
                ""
              ) : (
                <select
                  value={row.grade}
                  onChange={(e) => handleGradeChange(index, "grade", e.target.value)}
                  style={{
                    width: "100%",
                    fontSize: "6pt",
                    fontFamily: "Times New Roman, Times, serif",
                    border: isStatic ? "1px solid black" : "none",
                    borderRadius: "4px",
                  }}
                >
                  <option value="">-</option>
                  <option value="A+">A+</option>
                  <option value="A">A</option>
                  <option value="A-">A-</option>
                  <option value="B+">B+</option>
                  <option value="B">B</option>
                  <option value="B-">B-</option>
                  <option value="C+">C+</option>
                  <option value="C">C</option>
                  <option value="C-">C-</option>
                  <option value="D+">D+</option>
                  <option value="D">D</option>
                  <option value="F">F</option>
                </select>
              )}
            </td>
            <td style={{ border: "1px solid black", fontSize: "6pt", width: "10%", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>{row.weightedGPA}</td>
            <td style={{ border: "1px solid black", fontSize: "6pt", width: "10%", fontFamily: "Times New Roman, Times, serif", padding: "0 2px", lineHeight: "1" }}>{row.unweightedGPA}</td>
          </tr>
        ))}
      </tbody>
    </table>
    <button style={addButtonStyle} onClick={addRow}>
      +
    </button>
   </>
  );
}

export default GradeTableG12SS;
