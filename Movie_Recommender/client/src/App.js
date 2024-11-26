import React, { useState } from "react";
import axios from "axios";
import "./css/App.css";

function App() {
  const [search, setSearch] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  // Fetch recommendations from Flask backend
  const handleSearch = async () => {
    if (search.trim() === "") return; // Prevent empty search queries
    try {
      const response = await axios.get(`http://localhost:5000/search?q=${search}`);
      setRecommendations(response.data); // Update movie list
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
      <div className="app">
        <div className="search-container">
          <input
              type="text"
              placeholder="Search"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="search-input"
          />
          <button onClick={handleSearch} className="search-button">
            Recommend Movie
          </button>
        </div>
        <div className="recommendations">
          <h3>Recommendations</h3>
          <ul>
            {recommendations.map((movie, index) => (
                <li key={index} className="recommendation-item">
                  <strong>{movie.title}</strong>
                  <br />
                  <span>Genre: {movie.genre}</span>
                  <br />
                  <span>Rating: {movie.rating}</span>
                </li>
            ))}
          </ul>
        </div>
      </div>
  );
}

export default App;
