import React, { useRef } from "react";
import { RecipeBalance } from "./RecipeBalance.jsx";

export const Scrollable = ({ recipes }) => {
  const containerRef = useRef(null);
  let isDragging = false;
  let startX;
  let scrollLeft;

  const handleMouseDown = (e) => {
    isDragging = true;
    startX = e.pageX - containerRef.current.offsetLeft;
    scrollLeft = containerRef.current.scrollLeft;
  };

  const handleMouseLeave = () => {
    isDragging = false;
  };

  const handleMouseUp = () => {
    isDragging = false;
  };

  const handleMouseMove = (e) => {
    console.log("MOVING");
    if (!isDragging) return;
    e.preventDefault();
    const x = e.pageX - containerRef.current.offsetLeft;
    const walk = (x - startX) * 3; // Multiply by 3 for faster scrolling
    containerRef.current.scrollLeft = scrollLeft - walk;
  };

  return (
    <div
      ref={containerRef}
      onMouseDown={handleMouseDown}
      onMouseLeave={handleMouseLeave}
      onMouseUp={handleMouseUp}
      onMouseMove={handleMouseMove}
      className="m-8 flex gap-8 overflow-x-auto w-full items-center bg-neutral-700 p-4 rounded-lg cursor-grab active:cursor-grabbing"
      style={{ cursor: "grab" }}
    >
      {Object.entries(recipes).map(([index, intake]) => (
        <div key={index} className="mb-4 min-w-[1300px] flex-1  flex flex-col">
          <h4 className="text-xl mb-2">{intake["meal_type"]}</h4>
          <RecipeBalance
            meal={intake["details"][0]["recipe"]}
            intake={intake}
            key={index}
          />
        </div>
      ))}
    </div>
  );
};
