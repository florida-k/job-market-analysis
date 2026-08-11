import { useState } from "react";
import "./App.css";

function App() {
  const [job, setJob] = useState("");
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleSearch() {
    if (!job.trim()) {
      return;
    }

    setLoading(true);
    setResults(null);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/analysis?job=${encodeURIComponent(job)}`
      );

      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error("Error fetching job data:", error);
    }

    setLoading(false);
  }

  return (
    <div className="app">
      <h1>Job Market Analysis</h1>

      <p>Search for a job title to explore current market trends.</p>

      <div className="search-container">
        <input
          type="text"
          placeholder="Software Engineer"
          value={job}
          onChange={(e) => setJob(e.target.value)}
        />

        <button onClick={handleSearch}>
          Search
        </button>
      </div>

      {loading && <p>Loading job market data...</p>}

      {results && !results.error && (
        <div className="results">
          <h2>{results.job}</h2>

          <div className="summary">
            <div>
              <h3>Jobs Analyzed</h3>
              <p>{results.job_count}</p>
            </div>

            <div>
              <h3>Average Salary</h3>
              <p>
                {results.average_salary
                  ? `$${results.average_salary.toLocaleString()}`
                  : "Not available"}
              </p>
            </div>
          </div>

          <div className="section">
            <h3>Top Companies</h3>

            {Object.entries(results.top_companies).map(
              ([company, count]) => (
                <p key={company}>
                  {company}: {count}
                </p>
              )
            )}
          </div>

          <div className="section">
            <h3>Top Locations</h3>

            {Object.entries(results.top_locations).map(
              ([location, count]) => (
                <p key={location}>
                  {location}: {count}
                </p>
              )
            )}
          </div>

          <div className="section">
            <h3>Top Skills</h3>

            {Object.keys(results.top_skills).length === 0 ? (
              <p>No common skills found.</p>
            ) : (
              Object.entries(results.top_skills).map(
                ([skill, percentage]) => (
                  <p key={skill}>
                    {skill}: {percentage}%
                  </p>
                )
              )
            )}
          </div>
        </div>
      )}

      {results?.error && (
        <p>No jobs found for that search.</p>
      )}
    </div>
  );
}

export default App;