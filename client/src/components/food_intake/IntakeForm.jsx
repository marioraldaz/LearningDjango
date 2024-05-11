import React, { useContext, useState } from "react";
import { NavigationButton } from "../Buttons/NavigationButton.jsx";
import { GrayButton } from "../Buttons/GrayButton.jsx";
import { CardsList } from "../Lists/CardsList.jsx";
import { AuthContext } from "../../context/AuthContext";

export function IntakeForm({ recipes }) {
  const [formData, setFormData] = useState({
    meal_type: "Breakfast",
    intake_date: null,
    profile_id: null,
    amount: 1, // Initial amount set to 1
  });

  const { addFoodIntake } = useContext(AuthContext);

  const handleSubmit = (e) => {
    e.preventDefault();

    const details = recipes.map((recipe) => ({
      content_type: "recipe",
      food_id: recipe.id,
      amount: formData.amount.toString(), // Convert amount to string
    }));

    addFoodIntake(formData.meal_type, details);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleAmountChange = (e) => {
    const { value } = e.target;
    setFormData({ ...formData, amount: parseInt(value) }); // Parse amount to integer
  };

  return (
    <>
      <form className="flex flex-col gap-4 mb-8" onSubmit={handleSubmit}>
        <h3 className="text-3xl gradient-text text-center mt-8 mb-4">
          Log Your Meal
        </h3>
        <div className="grid grid-cols-2">
          <CardsList products={recipes} />
          <section className="flex flex-col gap-4 ml-16 mt-12">
            <div>
              <label htmlFor="meal_type">Log for:</label>
              <select
                name="meal_type"
                className="text-black ml-2"
                value={formData.meal_type}
                onChange={handleInputChange}
              >
                <option value="Breakfast">Breakfast</option>
                <option value="Lunch">Lunch</option>
                <option value="Dinner">Dinner</option>
                <option value="Snack">Snack</option>
              </select>
            </div>
            <span className="">
              Serving: {recipes.serving ? recipes.serving : "Not specified"}
            </span>
            <div className="flex">
              <label htmlFor="amount">Number of servings:</label>
              <input
                type="number"
                name="amount"
                value={formData.amount}
                onChange={handleAmountChange}
                className="ml-2 w-12 border border-gray-300 rounded px-2 text-black"
              />
            </div>
          </section>
        </div>

        <div>
          <GrayButton type="submit">Log For Today</GrayButton>
        </div>
      </form>

      <section className="flex flex-col gap-4">
        <div>
          <h3 className="text-2xl">Search For Recipes</h3>
          <NavigationButton link="/Recipes" text="Recipes" />
        </div>

        <div>
          <h3 className="text-2xl">Save Your Own Recipe</h3>
          <NavigationButton link="/Recipes" text="Create Recipe" />
        </div>

        <div>
          <h3 className="text-2xl">Search For Ingredients</h3>
          <NavigationButton link="/Ingredients" text="Search For Ingredients" />
        </div>
      </section>
    </>
  );
}
