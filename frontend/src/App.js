import axios from 'axios';
import { useState } from 'react';
import './App.css';

function App() {

  const limits = Array.from({ length: 30 }, (_, i) => i + 3);
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

  const [limit, setLimit] = useState(10);
  const [stat, setStat] = useState("Pass Yards");
  const [ascend, setAscend] = useState("DESC");
  const [imageUrl, setImageUrl] = useState("http://localhost:5000/graphs/Pass Yards10DESC.png");

  const submit = async(e) => {
    e.preventDefault();
    let submission = {
      "stat": stat,
      "limit": parseInt(limit),
      "ascending": ascend
    }
    const response = await axios.post("http://localhost:5000/submit", submission, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    let url = "http://localhost:5000/" + response.data["image"];
    setImageUrl(url)
  }

  const handleStatDropDown = event => {
    setStat(event.target.value);
  }

  const handleLimitDropDown = event => {
    setLimit(event.target.value);
  }

  const handleAscendDropDown = event => {
    setAscend(event.target.value);
  }
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
        <img src={imageUrl} />
      </div>
    </div>
  );
}

export default App;
