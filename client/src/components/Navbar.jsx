import React from "react";
import { NavLink } from "react-router-dom";

export function Navbar() {
  return (
    <nav className="w-full h-32 border-green-600 border-b-2">
      <div className="w-full flex h-full text-white">
        <NavLink to="/" className="flex">
          <img
            src="/nutribestPNG.png" // Correct the path to the logo image
            alt="Logo"
            className="h-36 w-auto" // Adjusted size for the logo
          />
        </NavLink>

        <div className="flex ml-auto space-x-12 mr-16 items-center">
          <NavLink
            to="/home"
            className={(navData) =>
              navData.isActive ? "active-style" : "text-white"
            }
          >
            <span className="text-4xl">Home</span>
          </NavLink>

          <NavLink
            to="/Ingredients"
            className={(navData) =>
              navData.isActive ? "active-style" : "text-white"
            }
          >
            <span className="text-4xl">Ingredients</span>
          </NavLink>
          <NavLink
            to="/Recipes"
            className={(navData) =>
              navData.isActive ? "active-style" : "text-white"
            }
          >
            <span className="text-4xl">Recipes</span>
          </NavLink>
          <NavLink
            to="/MyBalance"
            className={(navData) =>
              navData.isActive ? "active-style" : "text-white"
            }
          >
            <span className="text-4xl">My Balance</span>
          </NavLink>
          <NavLink
            to="/"
            className="flex flex-column items-center
          h-full"
          >
            <img
              src="/profile2.svg" // Correct the path to the logo image
              alt="Logo"
              className="h-16 w-auto ml-12" // Adjusted size for the logo
            />
          </NavLink>
        </div>
        <div className="md:hidden">{/* Mobile menu icon */}</div>
      </div>
    </nav>
  );
}
