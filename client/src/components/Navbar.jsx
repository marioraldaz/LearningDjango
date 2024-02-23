import React from "react";
import "./Navbar.css"; // Import your CSS file for styling

export function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <a href="/" className="navbar-logo">
          Your Logo
        </a>
        <ul className="nav-menu">
          <li className="nav-item-left">
            <a href="/" className="nav-links">
              Home
            </a>
          </li>
          <li className="nav-item-left">
            <a href="/about" className="nav-links">
              Ingredients
            </a>
          </li>
          <li className="nav-item-left">
            <a href="/contact" className="nav-links">
              Recipes
            </a>
          </li>
          {/* Add more navigation items as needed */}
        </ul>
      </div>
    </nav>
  );
}
