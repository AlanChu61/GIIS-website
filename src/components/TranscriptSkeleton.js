import React from 'react';

const shimmer = {
  background: 'linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%)',
  backgroundSize: '200% 100%',
  animation: 'shimmer 1.4s infinite',
  borderRadius: '4px',
};

const styles = `
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
`;

function Bar({ width = '100%', height = '12px', style = {} }) {
  return <div style={{ ...shimmer, width, height, marginBottom: '6px', ...style }} />;
}

function TranscriptSkeleton() {
  return (
    <>
      <style>{styles}</style>
      <div style={{ padding: '4px', fontFamily: 'Times New Roman, Times, serif' }}>
        {/* Header block */}
        <Bar width="40%" height="10px" style={{ margin: '0 auto 4px' }} />
        <Bar width="60%" height="18px" style={{ margin: '0 auto 8px' }} />
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
          <Bar width="30%" height="10px" />
          <Bar width="30%" height="10px" />
          <Bar width="25%" height="10px" />
        </div>

        {/* Student info table */}
        {[0, 1, 2].map((r) => (
          <div key={r} style={{ display: 'flex', gap: '6px', marginBottom: '4px' }}>
            {[0, 1, 2, 3].map((c) => (
              <Bar key={c} width="25%" height="22px" style={{ marginBottom: 0 }} />
            ))}
          </div>
        ))}

        {/* Grade tables */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '12px' }}>
          {[0, 1].map((col) => (
            <div key={col} style={{ flex: 1 }}>
              {[0, 1, 2, 3].map((sem) => (
                <div key={sem} style={{ marginBottom: '10px' }}>
                  <Bar width="60%" height="8px" style={{ marginBottom: '4px' }} />
                  {[0, 1, 2, 3, 4].map((row) => (
                    <Bar key={row} height="10px" />
                  ))}
                </div>
              ))}
            </div>
          ))}
        </div>

        {/* Cumulative GPA */}
        <Bar height="22px" style={{ marginTop: '8px' }} />
        <Bar height="22px" />
      </div>
    </>
  );
}

export default TranscriptSkeleton;
