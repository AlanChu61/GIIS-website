import React, {useState}  from 'react';

function GradeTableG9FS({ semesterName, onTotalsUpdate, onSemesterUpdate, isStatic = false}) {
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
      const credits = parseFloat(row.credits) || 0; // 檢查 Credits 是否有效，無效時設為 0
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

    // 更新欄位值
    newRows[index][field] = value;

    // 如果欄位是成績、課程名稱、學分或類型，重新計算 GPA
    if (field === "grade" || field === "name" || field === "credits" || field === "type") {
      const gpa = gradeToGpa[newRows[index].grade?.toUpperCase()] || { weighted: "-", unweighted: "-" };

      // 判斷 Type 和 Course name 是否包含 "AP"
      const typeHasAP = newRows[index].type?.includes("AP") || false;
      const nameHasAP = newRows[index].name?.includes("AP") || false;

      if (typeHasAP && nameHasAP) {
        // 當 Type 和 Course name 都包含 "AP"
        newRows[index].unweightedGPA = gpa.unweighted;
        newRows[index].weightedGPA =
          gpa.unweighted !== "-" ? gpa.unweighted + 1 : "-";
      } else {
        // 當 Type 或 Course name 中有任意一個不包含 "AP"
        newRows[index].unweightedGPA = gpa.unweighted;
        newRows[index].weightedGPA = gpa.unweighted;
      }
    }

    // 計算學期總 GPA
    const totals = calculateTotals(newRows);
    const totalsIndex = newRows.findIndex((row) => row.name === "Semester Totals");
    if (totalsIndex !== -1) {
      newRows[totalsIndex].weightedGPA = totals.weightedGPA;
      newRows[totalsIndex].unweightedGPA = totals.unweightedGPA;
      newRows[totalsIndex].totalCredits = totals.totalCredits.toFixed(1);
    }

    // 將兩個 GPA 傳遞給父元件
    if (onTotalsUpdate) {
      onTotalsUpdate(semesterName, {
        weightedGPA: totals.weightedGPA,
        unweightedGPA: totals.unweightedGPA,
        totalCredits: totals.totalCredits, // 傳遞學分
      });
    }

    return newRows;
  });
};

  const addRow = () => {
  setRows((prevRows) => {
    const newRow = { name: "", type: "", credits: "", grade: "", weightedGPA: "-", unweightedGPA: "-" };

    // 確保新增行在 "Semester Totals" 之前
    const totalsIndex = prevRows.findIndex((row) => row.name === "Semester Totals");
    const beforeTotals = prevRows.slice(0, totalsIndex);
    const afterTotals = prevRows.slice(totalsIndex);

    return [...beforeTotals, newRow, ...afterTotals];
  });
};

 const addButtonStyle = {
  border: "none", // 移除按鈕的外框
  backgroundColor: "#007bff", // 按鈕背景顏色
  color: "white", // 按鈕文字顏色
  borderRadius: "50%", // 讓按鈕變成圓形
  width: "40px", // 設定按鈕寬度
  height: "40px", // 設定按鈕高度
  fontSize: "20px", // 文字大小
  cursor: "pointer", // 滑鼠移上去顯示為可點擊的樣式
  display: "flex", // 讓內容居中對齊
};


  return (
   <>
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr>
          <td colSpan="6" style={{ textAlign: "left", fontWeight: "bold", fontSize: "12px" , fontFamily: "Times New Roman, Times, serif"}}>
            Grade 9 - Fall Semester
          </td>
        </tr>
        <tr>
          <th style={{ border: "1px solid black", fontSize: "10px" , fontFamily: "Times New Roman, Times, serif"}}>Course Name</th>
          <th style={{ border: "1px solid black", fontSize: "10px", fontFamily: "Times New Roman, Times, serif" }}>Type</th>
          <th style={{ border: "1px solid black", fontSize: "10px", fontFamily: "Times New Roman, Times, serif" }}>Credits</th>
          <th style={{ border: "1px solid black", fontSize: "10px", fontFamily: "Times New Roman, Times, serif" }}>Grade</th>
          <th style={{ border: "1px solid black", fontSize: "10px", fontFamily: "Times New Roman, Times, serif" }}>Weighted GPA</th>
          <th style={{ border: "1px solid black", fontSize: "10px", fontFamily: "Times New Roman, Times, serif" }}>Unweighted GPA</th>
        </tr>
      </thead>
      <tbody>
        {rows.map((row, index) => (
        <tr key={index}>
            <td style={{ border: "1px solid black", fontSize: "8px", width: "30%", fontFamily: "Times New Roman, Times, serif" }}>
             {row.name === "Semester Totals" ? (
              <span>Semester Totals</span>
              ) : (
              <input
                type="text"
                value={row.name}
                onChange={(e) => handleGradeChange(index, "name", e.target.value) }
                style={{ width: "100%", border: isStatic ? "1px solid black" : "none", borderRadius: "4px" }}
                disabled={row.name === "Semester Totals"}
              />
             )}
            </td>
                  
            <td style={{ border: "1px solid black", fontSize: "8px", width: "15%", fontFamily: "Times New Roman, Times, serif" }}>
             {row.name === "Semester Totals" ? (
               ""
              ) : (
              <select
                value={row.type}
                onChange={(e) => handleGradeChange(index, "type", e.target.value)}
                style={{ width: "100%", border: isStatic ? "1px solid black" : "none", borderRadius: "4px" }}
                disabled={row.name === "Semester Totals"}
              >
                <option value="">-</option>
                <option value="Core">Core</option>
                <option value="Core (AP)">Core (AP)</option>
                <option value="Elective">Elective</option>
              </select>
             )}
            </td>
                
            <td style={{ border: "1px solid black", fontSize: "8px", width: "10%" , fontFamily: "Times New Roman, Times, serif"}}>
             {row.name === "Semester Totals" ? (
              row.totalCredits // 顯示加總結果
              ) : (
                <select
                 value={row.credits}
                 onChange={(e) => handleGradeChange(index, "credits", e.target.value)}
                 style={{
                  width: "100%",
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
                
            <td style={{ border: "1px solid black", fontSize: "8px", width: "10%", fontFamily: "Times New Roman, Times, serif" }}>
              {row.name === "Semester Totals" ? (
                ""
              ) : (
                <select
                  value={row.grade}
                  onChange={(e) => handleGradeChange(index, "grade", e.target.value)}
                  style={{
                    width: "100%",
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
            <td style={{ border: "1px solid black", fontSize: "8px", width: "10%", fontFamily: "Times New Roman, Times, serif" }}>{row.weightedGPA}</td>
            <td style={{ border: "1px solid black", fontSize: "8px", width: "10%", fontFamily: "Times New Roman, Times, serif" }}>{row.unweightedGPA}</td>
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

export default GradeTableG9FS;

