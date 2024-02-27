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
            to="/"
            className="hover:text-green-400 hover:bg-neutral-800 p-[15px] transform hover:scale-110 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 text-center"
          >
            <span className="text-4xl">Home</span>
          </NavLink>

          <NavLink
            to="/Ingredients"
            activeClassName="active"
            className="hover:text-green-400 hover:bg-neutral-800 p-[15px] transform hover:scale-110 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 text-center"
          >
            <span className="text-4xl h-full">Ingredients</span>
          </NavLink>
          <NavLink
            to="/Recipes"
            className="hover:text-green-400 hover:bg-neutral-800 p-[15px] transform hover:scale-110 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 text-center"
          >
            <span className="text-4xl">Recipes</span>
          </NavLink>
          <NavLink
            to="/MyBalance"
            className="hover:text-green-400 hover:bg-neutral-800 p-[15px] transform hover:scale-110 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 text-center"
          >
            <span className="text-4xl">My Balance</span>
          </NavLink>
          <NavLink
            to="/Profile"
            className="hover:text-green-400 hover:bg-neutral-800 p-[15px] transform hover:scale-110 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 text-center"
          >
            <img
              src="/profile2.svg" // Correct the path to the logo image
              alt="Logo"
              className="h-16 w-auto " // Adjusted size for the logo
            />
          </NavLink>
        </div>
        <div className="md:hidden">{/* Mobile menu icon */}</div>
      </div>
    </nav>
  );
}
