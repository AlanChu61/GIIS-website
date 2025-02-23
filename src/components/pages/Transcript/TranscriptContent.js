import React, { useRef, useState }  from 'react';
import logoSlogan from '../../../img/logo_slogan.png';
import GradeTableG9FS from './GradeTableG9FS.js';
import GradeTableG9SS from './GradeTableG9SS.js';
import GradeTableG10FS from './GradeTableG10FS.js';
import GradeTableG10SS from './GradeTableG10SS.js';
import GradeTableG11FS from './GradeTableG11FS.js';
import GradeTableG11SS from './GradeTableG11SS.js';
import GradeTableG12FS from './GradeTableG12FS.js';


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
     padding: '10px',
     textAlign: 'center',
     width: '100%',
     backgroundColor: 'white',
     outline: 'none',
     boxShadow: 'none', 
  }

  const title = {
     marginTop: '5%',
     fontFamily: 'Times New Roman, Times, serif',
     fontSize: '25px',
  }

 const columns ={
     width: '100%',
     display: 'flex',
     justifyContent: 'space-between',
     backgroundColor: 'rgba(255, 255, 255, 1)', 
     margin: '0 auto',
   }

  const column1 ={
     flex: '1',
     textAlign: 'left',
     padding: '10px',
     boxSizing: 'border-box',
     fontSize: '12px',
     fontFamily: 'Times New Roman, Times, serif',
     lineHeight: '1.2',
   }

   const column2 ={
     flex: '1',
     textAlign: 'center',
     padding: '10px',
     boxSizing: 'border-box',
     fontSize: '12px',
     fontFamily: 'Times New Roman, Times, serif',
     lineHeight: '1.2',
   }

    const column3 ={
     flex: '1',
     textAlign: 'right',
     padding: '10px',
     boxSizing: 'border-box',
     fontSize: '12px',
     fontFamily: 'Times New Roman, Times, serif',
     lineHeight: '1.2',
   }
  
   const thTd ={
     padding: '2px',
     border: '1px solid black',
     textAlign: 'left',
     fontSize: '10px',
     width: '25%',
     wordWrap: 'break-word',
     fontFamily: 'Times New Roman, Times, serif',
   }

   const table ={
     width: '100%',
     borderCollapse: 'collapse',
     fontFamily: 'Times New Roman, Times, serif',
     margin: '0 auto',
     tableLayout: 'fixed', 
     fontSize: '10px',
    }

   const table2 ={
     width: '100%',
     borderCollapse: 'collapse',
     fontFamily: 'Times New Roman, Times, serif',
     margin: '0 auto',
     tableLayout: 'fixed', 
     fontSize: '8px',

    }

   const table3 ={
     flex: '1',
     width: '95%',
     borderCollapse: 'collapse',
     fontFamily: 'Times New Roman, Times, serif',
     margin: '0 auto',
     fontSize: '8px',
   }


    const labelInputWrapper ={
     display: 'flex',
     alignItems: 'center', 
   }

    const input ={
     width: '50%',
     fontSize: '10px',
     boxSizing: 'border-box',
     border: 'none', 
     borderBottom: '2px solid black',
     background: 'none',
     outline: 'none',
     overflowWrap: 'break-word',
     whiteSpace: 'normal',
     wordWrap: 'break-word',
     fontFamily: 'Times New Roman, Times, serif',
     lineHeight: '1.2',
   }


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

    // 添加浮水印層（圖片）
    const watermark = new Image();
    watermark.src = logoSlogan; 
    watermark.style.position = "absolute";
    watermark.style.top = "43%";
    watermark.style.left = "10%";
    watermark.style.width = "80%"; // 覆蓋整個內容寬度
    watermark.style.height = "10%"; // 覆蓋整個內容高度
    watermark.style.zIndex = "-0.5"; // 確保浮水印在內容下層
    watermark.style.opacity = "0.2"; // 浮水印透明度
    watermark.style.pointerEvents = "none"; // 防止浮水印影響互動

    // 將浮水印圖片添加到克隆的節點
    clonedElement.style.position = "relative"; // 確保父容器支持絕對定位
    clonedElement.appendChild(watermark);

    // 將副本添加到隱藏區域
    const hiddenContainer = document.createElement("div");
    hiddenContainer.style.position = "absolute";
    hiddenContainer.style.top = "-9999px";
    hiddenContainer.style.left = "-9999px";
    hiddenContainer.appendChild(clonedElement);
    document.body.appendChild(hiddenContainer);

    // 設置 PDF 生成選項
    const options = {
      margin: 0,
      filename: "Transcript.pdf",
      html2canvas: {
        scale: 5, // 高解析度
        ignoreElements: (el) => el.tagName === "BUTTON", // 忽略按鈕
      },
      jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
    };

    window.html2pdf()
      .set(options)
      .from(clonedElement)
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
         
         <div id="content" ref={formRef}>
          <div style={title}>
           <p style={{marginBottom:"0"}}>Genesis of Ideas International School</p>
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
                State: <input type="text" style={input} placeholder="Enter State" />
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
       <table style={table2}>
         <tbody>
           <tr>
             <td style={thTd}>
                <table style={table3}>
                 <div>
                  <GradeTableG9FS semesterName="Grade 9 - Fall Semester" onTotalsUpdate={handleTotalsUpdate} />
                 </div>
                </table>

                <table style={table3}>
                 <div>
                   <GradeTableG9SS semesterName="Grade 9 - Spring Semester" onTotalsUpdate={handleTotalsUpdate} />
                 </div>
                </table>
                  
                <table style={table3}>
                 <div>
                   <GradeTableG10FS semesterName="Grade 10 - Fall Semester" onTotalsUpdate={handleTotalsUpdate} />
                 </div>
                </table>

                <table style={table3}>
                 <div>
                   <GradeTableG10SS semesterName="Grade 10 - Spring Semester" onTotalsUpdate={handleTotalsUpdate}/>
                 </div>
                </table>
              </td>

              <td style={{ ...thTd, verticalAlign: "top" }}>
                <table style={table3}>
                  <div>
                   <GradeTableG11FS semesterName="Grade 11 - Fall Semester" onTotalsUpdate={handleTotalsUpdate} />
                 </div>
                </table>

                  
                <table style={table3}>
                  <div>
                   <GradeTableG11SS semesterName="Grade 11 - Spring Semester" onTotalsUpdate={handleTotalsUpdate} />
                 </div>
                </table>

                  
                <table style={table3}>
                  <div>
                   <GradeTableG12FS semesterName="Grade 12 - SprFall Semester" onTotalsUpdate={handleTotalsUpdate} />
                 </div>
                </table>
              </td>
             </tr>
            </tbody>
        </table>
             

        <table style={table}>
           <tbody>
            <tr>
              <td style={thTd}>
                Weighted
              </td>
             
              <td style={thTd}>
                <strong>Cumulative GPA:</strong>  {calculateCumulativeGPA()}    
              </td>

              <td style={thTd}>
                <strong>Cumulative Credits:</strong>  {cumulativeCredits.toFixed(1)}
              </td>
            </tr>
            <tr>
              <td style={thTd}>
               Unweighted
              </td>
                  
              <td style={thTd}>
                <strong>Cumulative GPA:</strong>  {calculateCumulativeGPA("unweightedGPA")}
              </td>
                  
              <td style={thTd}>
                <strong>Cumulative Credits:</strong>  {cumulativeCredits.toFixed(1)}
              </td>
             </tr>
           </tbody>
          </table>
          <div style={{ marginTop: "3%", textAlign: "center" }}>
           <table style={{ width: "100%", borderCollapse: "collapse", marginTop: "10px" }}>
            <tbody>
             <tr>
              <td colSpan={3} style={{ textAlign: "right", padding: "10px 0",fontFamily: "Times New Roman, Times, serif", fontSize: "16px"  }}>
               <span style={{ whiteSpace: "nowrap" }}>Official(s) Certifying Transcript:</span>
               <span
                style={{
                display: "inline-block",
                height: "1px",
                width: "50%", // 調整橫槓寬度，減小到 30%
                backgroundColor: "black",
                marginLeft: "20px", // 增加文字與橫槓間距
                verticalAlign: "-8px",  // 讓橫槓底部和文字底部貼齊
                }}
                ></span>
               </td>
              </tr>
              <tr>              
               <td colSpan={3} style={{ textAlign: "right",padding: "20px 0", position: "relative" }}>
                <div
                 style={{
                  display: "grid",
                  gridTemplateColumns: "13% 13% 13%", // 定義三個列
                  columnGap: "35px", // 每列之間固定 20px 的間距
                  alignItems: "center", // 垂直居中
                  justifyContent: "end",
                  fontSize: "14px",
                 }}
                 >
                  <span style={{ whiteSpace: "nowrap",fontFamily: "Times New Roman, Times, serif", textAlign: "center" }}>Shiyu Zhang, Ph.D.</span>
                  <span style={{ whiteSpace: "nowrap",fontFamily: "Times New Roman, Times, serif", textAlign: "center" }}>President</span>
                  <span style={{ whiteSpace: "nowrap",fontFamily: "Times New Roman, Times, serif", textAlign: "center" }}>{usDate}</span>
                </div>
                   
                <div
                 style={{
                  position: "absolute",
                  borderBottom: "2px solid black",
                  width: "50%",
                  right: 0,
                  marginTop: "0.5%", 
                  }}
                 ></div>

                 <div
                  style={{
                   display: "grid",
                   gridTemplateColumns: "13% 13% 13%", // 定義三個列
                   columnGap: "35px", // 每列之間固定 20px 的間距
                   alignItems: "center", // 垂直居中
                   justifyContent: "end",
                   marginTop: "1%",
                   fontSize: "14px",
                  }}
                  >
                   <span style={{ whiteSpace: "nowrap", fontFamily: "Times New Roman, Times, serif",textAlign: "center" }}>Printed Name</span>
                   <span style={{ whiteSpace: "nowrap",fontFamily: "Times New Roman, Times, serif",textAlign: "center" }}>Title</span>
                   <span style={{ whiteSpace: "nowrap",fontFamily: "Times New Roman, Times, serif" , textAlign: "center" }}>Date</span>
                 </div>
               </td>
              </tr>
             </tbody>
           </table>         
          </div>
         </div>
        </div>
    );
}

export default TranscriptContent;




