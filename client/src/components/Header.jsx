import { NavLink } from "react-router-dom";
import { NavElem } from "./NavElem";
import React, { useState, useContext, useEffect } from "react";
import { useClickOutside } from "../utils/useClickOutside";
import AuthContext from "../context/AuthContext";

export function Header() {
  const { user } = useContext(AuthContext);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const ref = useClickOutside(() => {
    if (isMenuOpen) {
      toggleMenu();
    }
  });

  const links = [
    { id: 1, route: "/", text: "Home" },
    { id: 2, route: "/Ingredients", text: "Ingredients" },
    { id: 3, route: "/Recipes", text: "Recipes" },
    { id: 4, route: "/MyBalance", text: "MyBalance" },
    { id: 5, route: "/NutriExpert", text: "NutriExpert" },
  ];
  return (
    <nav className="max-w-full relative z-[1] h-24 flex flex-nowrap border-green-600 border-b-2 xl:pr-[40px] items-center">
      <NavLink to="/" className="flex-grow">
        <img
          src="/nutribestPNG.png"
          alt="Logo"
          className="h-28 w-[300px] mr-auto"
        />
      </NavLink>

      <div className="hidden xl:flex xl:flex-row flex-nowrap ml-auto space-x-12 items-center">
        {links.map((link) => (
          <NavElem key={link.id} route={link.route} text={link.text} />
        ))}
      </div>

      <NavLink
        to={!user ? "/Login" : "/profile"}
        className="ml-8  h-[80px] items-center hover:text-green-400 hover:bg-neutral-800 p-[15px] transform hover:scale-105 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 text-center"
      >
        <img src="/profile2.svg" alt="Logo" className="h-full" />
      </NavLink>
      <img
        src="/menu.png"
        alt="menu"
        ref={ref}
        onClick={toggleMenu}
        className="xl:hidden flex h-[120px] w-[150px] cursor-pointer hover:bg-neutral-800 p-[5px] transform hover:scale-105 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 "
      />

      {/* Mobile Menu */}
      {isMenuOpen && (
        <div className="absolute right-[7px] top-[140px] w-[200px] bg-neutral-800 shadow-lg rounded-lg z-50 xl:hidden">
          <div className="flex flex-col items-center py-4">
            {links.map((link) => (
              <NavElem key={link.id} route={link.route} text={link.text} />
            ))}
          </div>
        </div>
      )}
    </nav>
  );
}
