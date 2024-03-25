import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { NavigationButton } from "../../components/Buttons/NavigationButton";
import { useParams } from "react-router-dom";
import { GrayButton } from "../../components/Buttons/GrayButton";
export function FoodIntake() {
  const [formData, setFormData] = useState({
    meal_type: "Breakfast",
    intake_date: null,
    profile_id: null,
  });
  const [recipes, setRecipes] = useState([]);
  const [ingredients, setIngredients] = useState([]);
  const { addFoodIntake, user, getIngredient } = useContext(AuthContext);

  const handleSubmit = (e) => {
    e.preventDefault();
    addFoodIntake(formData);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  if (!user) {
    return <h1>Loading...</h1>;
  }

  return (
    <div className="h-full overflow-hidden gap-8 tex-center text-xl m-12 flex flex-col bg-neutral-900 items-center justify-center">
      <form className="flex flex-col gap-4 mb-8" onSubmit={handleSubmit}>
        <h3>Log Your Meal</h3>
        <div className="flex gap-4">
          <label htmlFor="meal_type">Type:</label>
          <select
            name="meal_type"
            className="text-black flex gap-4"
            value={formData.meal_type}
            onChange={handleInputChange}
          >
            <option value="Breakfast">Breakfast</option>
            <option value="Lunch">Lunch</option>
            <option value="Dinner">Dinner</option>
            <option value="Snack">Snack</option>
          </select>
        </div>

        <div className="">
          <GrayButton onClick={handleSubmit}>Log For Today</GrayButton>
        </div>
      </form>

      <div className="">
        <h3 className="text-2xl">Search For Recipes</h3>
        <NavigationButton link="/Recipes" text="Recipes" />
      </div>

      <div className="">
        <h3 className="text-2xl">Save Your Own Recipe</h3>
        <NavigationButton link="/Recipes" text="Create Recipe" />
      </div>

      <div className="">
        <h3 className="text-2xl">Search For Ingredients</h3>
        <NavigationButton link="/Ingredients" text="Search For Ingredients" />
      </div>
    </div>
  );
}
