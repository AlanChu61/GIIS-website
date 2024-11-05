import React from 'react';

function Academicsintroduction({ language }) {

    const headlineStyle = {
        marginTop: '115px',
        color: 'white',
        width: '100%',
        paddingLeft: '15%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        fontSize: '70px',
        lineHeight: '1',
    };

    const introductionStyle = {
        marginTop: '70px',
        color: 'rgba(255, 255, 255, 0.8)',
        width: '100%',
        paddingLeft: '15%',
        fontFamily: 'Inter, sans-serif',
        fontWeight: 'bold',
        fontSize: '35px',
        lineHeight: '1',
    };

    return (
      <>
        <div style={headlineStyle}>
          <p>WHAT MAKES GIIS</p>
          <p>DIFFERENT? </p>
        </div>

        <div style={introductionStyle}>
          <p>The GIIS Differnce</p>     
        </div>
      </>
   );
}

export default Academicsintroduction;
