import React from "react";
export function Navbar() {
  return (
    <nav className=" h-36 w-full">
      <div className="pb-8 border-b-2 border-green-500 pt-8 w-full flex  justify-between pr-8 items-center h-full">
        <a href="/">
          <img
            className=" h-22 w-16"
            style={{ width: "180px", height: "180px" }}
            src="/public/svg-logo.svg"
          />
        </a>
        <div className="w-66">
          <span className="">Hello again Mario!</span>
        </div>
        <ul className="nav-menu flex space-x-10">
          <li className="nav-item-left">
            <a href="/" className="nav-links">
              Home
            </a>
          </li>
          <li className="nav-item-left">
            <a href="/Ingredients" className="nav-links">
              Ingredients
            </a>
          </li>
          <li className="nav-item-left">
            <a href="/Recipes" className="nav-links">
              Recipes
            </a>
          </li>
          <li className="nav-item-left">
            <a href="/MyBalance" className="nav-links">
              My Balance
            </a>
          </li>
          {/* Add more navigation items as needed */}
        </ul>
      </div>
    </nav>
  );
}
