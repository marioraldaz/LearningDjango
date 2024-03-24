import React from "react";
import { NavLink } from "react-router-dom";

export function MealLogForm() {
  return (
    <div>
      <form className="">
        <h3>Log Your Meal</h3>
        <div className="">
          <label for="type">Type:</label>
          <select className="">
            <option value="breakfast">Breakfast</option>
            <option value="lunch">Lunch</option>
            <option value="dinner">Dinner</option>
            <option value="snack">Snack</option>
          </select>
        </div>
        <div className="">
          <h3 className="text-2xl">Search For Recipes</h3>
          <NavigationButton link={"/Recipes"}>Recipes</NavigationButton>
        </div>

        <div className="">
          <h3 className="text-2xl">Search For Ingredients</h3>
          <NavigationButton
            link={"/Ingredients"}
            text={"Search For Ingredients"}
          />
        </div>
      </form>
    </div>
  );
}
