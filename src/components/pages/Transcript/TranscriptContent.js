import React, { useRef, useState }  from 'react';
import logoSlogan from '../../../img/logo_slogan.png';
import GradeTableG9FS from './GradeTableG9FS.js';
import GradeTableG9SS from './GradeTableG9SS.js';
import GradeTableG10FS from './GradeTableG10FS.js';
import GradeTableG10SS from './GradeTableG10SS.js';
import GradeTableG11FS from './GradeTableG11FS.js';
import GradeTableG11SS from './GradeTableG11SS.js';
import GradeTableG12FS from './GradeTableG12FS.js';
import GradeTableG12SS from './GradeTableG12SS.js';


function TranscriptContent({ language }) {
  
  const [semesterGPAs, setSemesterGPAs] = useState({});
  const [, setIsStaticMode] = useState(false);
  const [cumulativeCredits, setCumulativeCredits] = useState(0);

  const handleTotalsUpdate = (semesterName, gpaData) => {
   const { weightedGPA, unweightedGPA, totalCredits } = gpaData;
   console.log(`Received Weighted GPA for ${semesterName}:`, weightedGPA);
   console.log(`Received Unweighted GPA for ${semesterName}:`, unweightedGPA);
   console.log(`Received Total Credits for ${semesterName}:`, totalCredits);

  setSemesterGPAs((prev) => ({
    ...prev,
    [semesterName]: {
      weightedGPA: parseFloat(weightedGPA) || 0,
      unweightedGPA: parseFloat(unweightedGPA) || 0,
      totalCredits: parseFloat(totalCredits) || 0,
    },
  }));

   setCumulativeCredits((prevCredits) => {
    const updatedCredits = Object.values({
      ...semesterGPAs,
      [semesterName]: { totalCredits: parseFloat(totalCredits) || 0 },
    }).reduce((sum, current) => sum + (current.totalCredits || 0), 0);
    return updatedCredits;
  });
};


const calculateCumulativeGPA = (type = "weightedGPA") => {
  const gpas = Object.values(semesterGPAs)
    .map((gpa) => gpa[type])
    .filter((gpa) => gpa > 0); 
  if (gpas.length === 0) return "-";

  const totalGPA = gpas.reduce((acc, gpa) => acc + gpa, 0);
  return (totalGPA / gpas.length).toFixed(2);
};

  const container = {
    border: 'none',
    padding: '4px',
    textAlign: 'left',
    width: '100%',
    backgroundColor: 'white',
    outline: 'none',
    boxShadow: 'none',
  };

  const title = {
    marginTop: '0',
    marginBottom: '2px',
    fontFamily: 'Times New Roman, Times, serif',
    fontSize: '16pt',
    fontWeight: 'bold',
    textAlign: 'center',
  };

  const mainTitle = {
    marginBottom: '2px',
    fontFamily: 'Times New Roman, Times, serif',
    fontSize: '10pt',
    fontWeight: 'normal',
    textAlign: 'center',
  };

  const columns = {
    width: '100%',
    display: 'flex',
    justifyContent: 'space-between',
    backgroundColor: 'rgba(255, 255, 255, 1)',
    margin: '0 auto',
  };

  const column1 = {
    flex: '1',
    textAlign: 'left',
    padding: '4px',
    boxSizing: 'border-box',
    fontSize: '10pt',
    fontFamily: 'Times New Roman, Times, serif',
    lineHeight: '1.1',
  };

  const column2 = {
    flex: '1',
    textAlign: 'center',
    padding: '4px',
    boxSizing: 'border-box',
    fontSize: '10pt',
    fontFamily: 'Times New Roman, Times, serif',
    lineHeight: '1.1',
  };

  const column3 = {
    flex: '1',
    textAlign: 'right',
    padding: '4px',
    boxSizing: 'border-box',
    fontSize: '10pt',
    fontFamily: 'Times New Roman, Times, serif',
    lineHeight: '1.1',
  };

  const thTd = {
    padding: '1px 3px',
    border: '1px solid black',
    textAlign: 'left',
    fontSize: '8pt',
    width: '25%',
    wordWrap: 'break-word',
    fontFamily: 'Times New Roman, Times, serif',
    lineHeight: '1.1',
  };

  const thTdNarrow = {
    padding: '1px 3px',
    border: '1px solid black',
    textAlign: 'left',
    fontSize: '8pt',
    width: '12%',
    wordWrap: 'break-word',
    fontFamily: 'Times New Roman, Times, serif',
    lineHeight: '1.1',
  };

  const thTdWide = {
    padding: '1px 3px',
    border: '1px solid black',
    textAlign: 'left',
    fontSize: '8pt',
    width: '44%',
    wordWrap: 'break-word',
    fontFamily: 'Times New Roman, Times, serif',
    lineHeight: '1.1',
  };

  const table = {
    width: '100%',
    borderCollapse: 'collapse',
    fontFamily: 'Times New Roman, Times, serif',
    margin: '4px 0',
    tableLayout: 'fixed',
    fontSize: '8pt',
  };

  const labelInputWrapper = {
    display: 'flex',
    alignItems: 'center',
  };

  const input = {
    width: '50%',
    fontSize: '8pt',
    boxSizing: 'border-box',
    border: 'none',
    borderBottom: '2px solid black',
    background: 'none',
    outline: 'none',
    overflowWrap: 'break-word',
    whiteSpace: 'normal',
    wordWrap: 'break-word',
    fontFamily: 'Times New Roman, Times, serif',
    lineHeight: '1',
  };


const formRef = useRef();

const exportToPDF = () => {
  setIsStaticMode(true); // 切換到靜態模式

  setTimeout(() => {
    const element = document.getElementById("content");

    // 創建一個隱藏的 DOM 副本
    const clonedElement = element.cloneNode(true);

    // 同步表單的狀態到克隆的節點
    const originalInputs = element.querySelectorAll("input, select, textarea");
    const clonedInputs = clonedElement.querySelectorAll("input, select, textarea");

    originalInputs.forEach((input, index) => {
      const clonedInput = clonedInputs[index];
      if (input.tagName === "INPUT" || input.tagName === "TEXTAREA") {
        clonedInput.value = input.value; // 同步值
      } else if (input.tagName === "SELECT") {
        Array.from(clonedInput.options).forEach((option) => {
          option.selected = option.value === input.value; // 同步選中項目
        });
      }
    });

    // 替換表單節點為靜態文字
    const clonedInputsForReplacement = clonedElement.querySelectorAll("input, select, textarea");
    clonedInputsForReplacement.forEach((input) => {
      const span = document.createElement("span");
      if (input.tagName === "SELECT") {
        // 獲取選中項目的文本
        const selectedOption = input.options[input.selectedIndex];
        span.textContent = selectedOption ? selectedOption.text : "";
      } else {
        // 使用輸入值或預設值
        span.textContent = input.value || ""; 
      }
      input.parentNode.replaceChild(span, input); // 替換節點
    });

    // 浮水印已包含在 #content 內，clone 時會一併複製
    // 包成 A4 寬度 (190mm)，避免 html2pdf 縮壓導致版面擁擠
    clonedElement.classList.add("transcript-pdf-export");
    const pdfStyles = document.createElement("style");
    pdfStyles.textContent = `
      .transcript-pdf-export #grade-tables-container { margin-top: 2px !important; gap: 4px !important; }
      .transcript-pdf-export table { margin: 1px 0 !important; }
    `;
    clonedElement.appendChild(pdfStyles);

    const pdfWrapper = document.createElement("div");
    pdfWrapper.style.width = "190mm";
    pdfWrapper.style.minWidth = "190mm";
    pdfWrapper.style.maxWidth = "190mm";
    pdfWrapper.style.margin = "0";
    pdfWrapper.style.padding = "0";
    pdfWrapper.style.backgroundColor = "#fff";
    pdfWrapper.style.boxSizing = "border-box";
    pdfWrapper.appendChild(clonedElement);

    const hiddenContainer = document.createElement("div");
    hiddenContainer.style.position = "absolute";
    hiddenContainer.style.top = "-9999px";
    hiddenContainer.style.left = "-9999px";
    hiddenContainer.style.width = "190mm";
    hiddenContainer.appendChild(pdfWrapper);
    document.body.appendChild(hiddenContainer);

    // PDF 選項：單頁、A4、適當邊距
    const options = {
      margin: [8, 8, 8, 8],
      filename: "Transcript.pdf",
      html2canvas: {
        scale: 2,
        useCORS: true,
        logging: false,
        ignoreElements: (el) => el.tagName === "BUTTON",
      },
      jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
    };

    window.html2pdf()
      .set(options)
      .from(pdfWrapper)
      .save()
      .finally(() => {
        document.body.removeChild(hiddenContainer); // 移除隱藏的副本
        setIsStaticMode(false); // 恢復到編輯模式
      });
  }, 0);
};

  const today = new Date();
  const options = { timeZone: "America/Chicago" }; // 指定美國中部的時區
  const usDate = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    ...options,
  }).format(today);

     return (   
        <div style={container}>
         <button
          onClick={exportToPDF}
          style={{
            marginTop: "15px",
            padding: "10px 20px",
            backgroundColor: "rgba(43, 61, 109, 0.8)",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
           }}
          >
         Export to PDF
         </button> 
         
         <div id="content" ref={formRef} style={{ textAlign: 'left', maxWidth: '100%', position: 'relative' }}>
          {/* 浮水印：學校 logo，置中、低透明度，不影響點擊 */}
          <div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              pointerEvents: 'none',
              zIndex: 0,
            }}
            aria-hidden="true"
          >
            <img
              src={logoSlogan}
              alt=""
              style={{
                maxWidth: '70%',
                maxHeight: '70%',
                objectFit: 'contain',
                opacity: 0.14,
              }}
            />
          </div>
          <div style={{ position: 'relative', zIndex: 1 }}>
          <div style={mainTitle}>
           <p style={{ marginBottom: '0' }}>Academic Transcript</p>
          </div>
          <div style={title}>
           <p style={{ marginBottom: '0' }}>Genesis of Ideas International School</p>
          </div>
          <div style={columns}>
           <div style={column1}>
            7901 4th St N STE 300,<br />
            St. Petersburg, FL 33702<br />
           </div>
           <div style={column2}>
            Phone: +1 (813) 501-5756<br />
            <a href="https://genesisideas.school/">https://genesisideas.school/</a><br />
           </div>
           <div style={column3}>
            School Code: 650<br />
            President: Shiyu Zhang, Ph.D.<br />
           </div>
          </div>
              
          <table style={table}>
           <tbody>
            <tr>
              <td style={thTd}>
              <div style={labelInputWrapper}>
                Name:<input type="text" style={input} placeholder="Enter Name" />
              </div>
              </td>

             <td style={thTd}>
               Birth Date: <input type="date" style={input}  /> 
             </td>
             
              <td style={thTd}>
               Gender: 
                <select style={input}>
                 <option value="Female">Female</option>
                 <option value="Male">Male</option>
                </select>
              </td>
                  
              <td style={thTd}>
                Parent/Guardian: <input type="text" style={input} placeholder="Enter Name"/>
              </td>  
            </tr>
                  
            <tr>
              <td style={thTd}>
               Address: <input type="text" style={input} placeholder="Enter Address" />
              </td>
                  
              <td style={thTd}>
               <div style={labelInputWrapper}>
                  City:<input type="text" style={input} placeholder="Enter City" />
               </div>
              </td>
                  
              <td style={thTd}>
                Province: <input type="text" style={input} placeholder="Province" />
              </td>
                  
              <td style={thTd}>
               Zip Code: <input type="text" style={input} placeholder="Enter Zip Code" />
              </td>
          </tr>
                  
          <tr>
            <td style={thTd}>
              Entry Date: <input type="date" style={input} />
            </td>
                  
            <td style={thTd}>
              Withdrawal Date: <input type="date" style={input} />
            </td>
                  
            <td style={thTd}>
              Graduation Date: <input type="date" style={input} />
            </td>
                  
            <td style={thTd}>
              Transcript Date: <input type="date" style={input} />
            </td>
          </tr>
        </tbody>
       </table>
       <div id="grade-tables-container" style={{ marginTop: '4px', width: '100%', display: 'flex', gap: '8px', alignItems: 'flex-start' }}>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <GradeTableG9FS semesterName="Grade 9 - Fall Semester" onTotalsUpdate={handleTotalsUpdate} />
                  <GradeTableG9SS semesterName="Grade 9 - Spring Semester" onTotalsUpdate={handleTotalsUpdate} />
                  <GradeTableG10FS semesterName="Grade 10 - Fall Semester" onTotalsUpdate={handleTotalsUpdate} />
                  <GradeTableG10SS semesterName="Grade 10 - Spring Semester" onTotalsUpdate={handleTotalsUpdate}/>
                </div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <GradeTableG11FS semesterName="Grade 11 - Fall Semester" onTotalsUpdate={handleTotalsUpdate} />
                  <GradeTableG11SS semesterName="Grade 11 - Spring Semester" onTotalsUpdate={handleTotalsUpdate} />
                  <GradeTableG12FS semesterName="Grade 12 - Fall Semester" onTotalsUpdate={handleTotalsUpdate} />
                  <GradeTableG12SS semesterName="Grade 12 - Spring Semester(In Progress)" onTotalsUpdate={handleTotalsUpdate} />
                </div>
       </div>
             

        <table style={table}>
           <tbody>
            <tr>
              <td style={thTdNarrow}>
                Weighted
              </td>
             
              <td style={thTdWide}>
                <strong>Cumulative GPA:</strong>  {calculateCumulativeGPA()}    
              </td>

              <td style={thTdWide}>
                <strong>Cumulative Credits:</strong>  {cumulativeCredits.toFixed(1)}
              </td>
            </tr>
            <tr>
              <td style={thTdNarrow}>
               Unweighted
              </td>
                  
              <td style={thTdWide}>
                <strong>Cumulative GPA:</strong>  {calculateCumulativeGPA("unweightedGPA")}
              </td>
                  
              <td style={thTdWide}>
                <strong>Cumulative Credits:</strong>  {cumulativeCredits.toFixed(1)}
              </td>
             </tr>
           </tbody>
          </table>
          <div style={{ marginTop: "1%", textAlign: "right" }}>
           <table style={{ width: "100%", borderCollapse: "collapse", marginTop: "4px" }}>
            <tbody>
             <tr>
              <td colSpan={3} style={{ textAlign: "right", padding: "4px 0", fontFamily: "Times New Roman, Times, serif", fontSize: "10pt" }}>
               <span style={{ whiteSpace: "nowrap" }}>Official(s) Certifying Transcript:</span>
               <span
                style={{
                  display: "inline-block",
                  height: "1px",
                  width: "50%",
                  backgroundColor: "black",
                  marginLeft: "12px",
                  verticalAlign: "-6px",
                }}
               ></span>
               </td>
              </tr>
              <tr>
               <td colSpan={3} style={{ textAlign: "right", padding: "0", fontFamily: "Times New Roman, Times, serif", fontSize: "10pt" }}>
                Signature
               </td>
              </tr>
              <tr>
               <td colSpan={3} style={{ textAlign: "right", padding: "8px 0", position: "relative" }}>
                <div
                 style={{
                   display: "grid",
                   gridTemplateColumns: "13% 13% 13%",
                   columnGap: "24px",
                   alignItems: "center",
                   justifyContent: "end",
                   fontSize: "10pt",
                   fontFamily: "Times New Roman, Times, serif",
                 }}
                >
                  <span style={{ whiteSpace: "nowrap", textAlign: "center" }}>Shiyu Zhang, Ph.D.</span>
                  <span style={{ whiteSpace: "nowrap", textAlign: "center" }}>President</span>
                  <span style={{ whiteSpace: "nowrap", textAlign: "center" }}>{usDate}</span>
                </div>
                <div
                 style={{
                   position: "absolute",
                   borderBottom: "2px solid black",
                   width: "50%",
                   right: 0,
                   marginTop: "0.25%",
                 }}
                ></div>
                <div
                 style={{
                   display: "grid",
                   gridTemplateColumns: "13% 13% 13%",
                   columnGap: "24px",
                   alignItems: "center",
                   justifyContent: "end",
                   marginTop: "0.5%",
                   fontSize: "10pt",
                   fontFamily: "Times New Roman, Times, serif",
                 }}
                >
                  <span style={{ whiteSpace: "nowrap", textAlign: "center" }}>Printed Name</span>
                  <span style={{ whiteSpace: "nowrap", textAlign: "center" }}>Title</span>
                  <span style={{ whiteSpace: "nowrap", textAlign: "center" }}>Date</span>
                </div>
               </td>
              </tr>
             </tbody>
           </table>
          </div>
          </div>
         </div>
        </div>
    );
}

export default TranscriptContent;




