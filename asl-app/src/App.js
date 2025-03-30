import React, { useState, useEffect } from "react";
import VideoPlayer from "./VideoPlayer";
import "./App.css"; // Import the CSS file

function App() {
  const [videoId, setVideoId] = useState(null);

  useEffect(() => {
    const fetchVideoPaths = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/paths");
        const data = await response.json();
        console.log(data); // Log the data to see it

        // Set the first video path as the default videoId
        if (data.video_paths && data.video_paths.length > 0) {
          setVideoId(data.video_paths[0]); // Set the video ID to the first path
        }
      } catch (error) {
        console.error("Error fetching video paths:", error);
      }
    };

    fetchVideoPaths(); // Call the function on component mount
  }, []); // Empty dependency array ensures it runs once when the component mounts

  useEffect(() => {
    // Log videoId after it has been updated
    if (videoId) {
      console.log("Updated videoId:", videoId);
    }
  }, [videoId]); // This useEffect runs when videoId is updated

  return (
    <div className="app">
      <header className="app-header">
        <h1>Welcome to the Video Library</h1>
      </header>
      <main className="app-main">
        {videoId ? <VideoPlayer videoId={videoId} /> : <p>Loading video...</p>}
      </main>
      <footer className="app-footer">
        <p>Enjoy your viewing experience!</p>
      </footer>
    </div>
  );
}

export default App;
