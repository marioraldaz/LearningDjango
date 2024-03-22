import React, { useState, useEffect, useContext } from "react";
import { NavigationButton } from "../components/buttons/NavigationButton"; // Import the NavigationButton component

export function Home() {
  const menuItems = [
    { link: "/MyBalance", text: "My Balance" },
    { link: "/recipes", text: "Recipes Page" },
    { link: "/ingredients", text: "Ingredients Page" },
    { link: "/profiles", text: "Profile Page" },
  ];

  return (
    <div className="mb-[650px] flex flex-wrap w-full text-green-600 text-4xl h-32 p-6">
      <div className="video-container pointer-events-none">
        <video autoPlay loop>
          <source src="/brocoli.png" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div className="w-full flex flex-wrap items-center justify-center">
        <h1 className="gradient-text text-center mb-6">
          Living Fast Needs Keeping Track
        </h1>
      </div>
      <div className="grid gap-4">
        {menuItems.map((item, index) => (
          <NavigationButton key={index} link={item.link} text={item.text} />
        ))}
      </div>
    </div>
  );
}
