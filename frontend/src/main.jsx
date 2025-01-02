import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router } from "react-router-dom";
import "./index.css";
import App from "./App.jsx";
import Navbar from "./components/Navbar";


createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Router>
      <Navbar />
      <App />
    </Router>
  </StrictMode>
);
