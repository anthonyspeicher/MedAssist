import { useState } from 'react';
import './App.css';

export default function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("No file selected.");

    const formData = new FormData();
    formData.append("file", file);

    setResult(null);
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/analyze/", {
        method: "POST",
        body: formData,
      });

      setResult(await res.json());

    } catch (error) {
      console.error("Error: ", error);
      alert("Failed to connect to backend.");
    } finally {
      setLoading(false);
    }
  };


  return (
    <div style={{backgroundColor: "black", color: "green", minHeight: "100vh", padding: "2rem", fontFamily: "monospace"}}>
      <h1>MedAssist AI</h1>
      <input type="file" accept="image/*" onChange={(event) => setFile(event.target.files[0])} style={{marginTop: "1rem"}}/>

      <button onClick={handleUpload} disabled={!file || loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      {result && (
        <div>
          <h2>Results</h2>

          <p>
            {JSON.stringify(result, null, 2)}
          </p>
        </div>
      )}
    </div>
  );
}
