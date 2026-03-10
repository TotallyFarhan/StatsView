import { useState } from 'react';
import './App.css';

function App() {
  // Array from 3 to 32 for the minimum and maximum Quarterbacks allowed in a graph
  const limits = Array.from({ length: 30 }, (_, i) => i + 3);
  // Array containing all the possible stats to create a graph with
  const stats = [
    "Age",
    "Games Played",
    "Completions",
    "Attempts",
    "Completion Percentage",
    "Pass Yards",
    "Touchdowns",
    "Interceptions",
    "First Downs Passing",
    "Success Rate",
    "Longest Pass",
    "Yards/Attempt",
    "Yards/Completion",
    "Rate",
    "QBR",
    "Sacks",
    "4Q Comebacks",
    "Game Winning Drives"
  ];

  const [limit, setLimit] = useState(10); // State variable to hold the limit from the form on the website
  const [stat, setStat] = useState("Pass Yards"); // State variable to hold the stat from the form on the website
  const [ascend, setAscend] = useState("DESC"); // State variable to hold the choice of ascending or descending from the form on the website
  const [imageUrl, setImageUrl] = useState("/starter.png"); // State variable to hold the image path of the graph
  const [submittedStat, setSubmittedStat] = useState(stat); // State variable to hold the submitted stat
  const [submittedLimit, setSubmittedLimit] = useState(limit); // State variable to hold the submitted limit
  const [submittedAscend, setSubmittedAscend] = useState(ascend); // State variable to hold the submitted choice of ascending or descending
  const [loading, setLoading] = useState(false) // State variable to handle loading animation while waiting for graph to show up

  // Function to handle form submission
  const submit = async (e) => {
    e.preventDefault();

    setLoading(true);

    // JSON Object of the users form submission data
    let submission = {
      "stat": stat,
      "limit": parseInt(limit),
      "ascending": ascend
    }
    // Uses axios to send a POST request to the backend the JSON object of the form submission data
    const response = await fetch("https://statsview.onrender.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(submission)
    });

    // Grab buffer from response object sent by flask
    const blob = await response.blob();
    const imageUrl = URL.createObjectURL(blob);
    setImageUrl(imageUrl); // Update Image URL with buffer passed in

    setSubmittedAscend(ascend); // Updates the submitted choice of ascending or descending
    setSubmittedLimit(limit); // Updates the submitted limit
    setSubmittedStat(stat); // Updates the submitted stat

    setLoading(false);
  }

  // Function to handle when the user changes their form choice for stat
  const handleStatDropDown = event => {
    setStat(event.target.value);
  }
  // Function to handle when the user changes their form choice for limit
  const handleLimitDropDown = event => {
    setLimit(event.target.value);
  }
  // Function to handle when the user changes their form choice for ascending or descending
  const handleAscendDropDown = event => {
    setAscend(event.target.value);
  }

  // HTML containing the form and the image of the graph
  return (
    <div className="container">
      <div className="formContainer">
        <h1>🏈 StatsView 🏈</h1>
        <div className="form-group">
          <label for="stat-select">Select Statistic:</label>
          <select id="stat-select" onChange={handleStatDropDown} defaultValue={stat}>
            {stats.map(stat => (
              <option key={stat} value={stat}>{stat}</option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label for="limit-select">Select Limit:</label>
          <select id="limit-select" onChange={handleLimitDropDown} defaultValue={limit}>
            {limits.map(limit => (
              <option key={limit} value={limit}>{limit}</option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label for="ascend-select">Ascending or Descending:</label>
          <select id="ascend-select" onChange={handleAscendDropDown} defaultValue={ascend}>
            <option value="ASC">Ascending</option>
            <option value="DESC">Descending</option>
          </select>
        </div>
        <button id="submit-button" onClick={submit}>Submit</button>
      </div>
      <div className="result">

        {loading ? (
          <div className="spinner"></div>
        ) : (
          <>
            <h1>{submittedAscend === "DESC" ? "Top" : "Bottom"} {submittedLimit} QBs in {submittedStat}</h1>
            <img src={imageUrl} alt="Quarterback statistics graph" />
          </>
        )}
      </div>
    </div>
  );
}

export default App;
