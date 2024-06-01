import React, { useContext, useState } from "react";
import { NavigationButton } from "../Buttons/NavigationButton.jsx";
import { GrayButton } from "../Buttons/GrayButton.jsx";
import { CardsList } from "../Lists/CardsList.jsx";
import { AuthContext } from "../../context/AuthContext";
import { FoodIntakeSaved } from "../../sweetalert/foodIntakeSaved.js";

export function IntakeForm({ recipes: recipe }) {
  const [formData, setFormData] = useState({
    meal_type: "Breakfast",
    intake_date: null,
    profile_id: null,
    amount: 1, // Initial amount set to 1
  });
  const [showPopUp, setShowPopUp] = useState(false);
  const { addFoodIntake } = useContext(AuthContext);

  if (!recipe || !recipe[0] || !formData) {
    return <h1>loading</h1>;
  }

  recipe = recipe[0];

  if (recipe.nutrition?.weight_per_serving.length == 1) {
    recipe.nutrition.weight_per_serving =
      recipe.nutrition.weight_per_serving[0];
  }
  const handleSubmit = (e) => {
    e.preventDefault();
    const details = {
      content_type: "recipe",
      food_id: recipe.id,
      amount: formData.amount.toString(), // Convert amount to string
    };

    addFoodIntake(formData.meal_type, [details]);
    setShowPopUp(true);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  function calculateGrams(weight, percent) {
    weight = parseInt(weight);
    const decimal = percent / 100;
    const grams = decimal * weight * formData.amount;
    return grams.toFixed(2);
  }
  const handleAmountChange = (e) => {
    const { value } = e.target;
    setFormData({ ...formData, amount: parseInt(value) }); // Parse amount to integer
  };

  return (
    <>
      {showPopUp && FoodIntakeSaved()}
      <form className="flex flex-col gap-4 mb-8" onSubmit={handleSubmit}>
        <h3 className="text-3xl gradient-text text-center mb-4">
          Log Your Meal
        </h3>
        <div className="flex flex-col items-center justify-center">
          <CardsList products={[recipe]} />
          <section className="flex flex-col gap-4 border border-white p-2 w-full">
            <div className="">
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
              Serving:{"   "}
              {recipe.nutrition?.weight_per_serving.amount
                ? recipe.nutrition.weight_per_serving.amount +
                  recipe.nutrition.weight_per_serving.unit
                : "Not specified"}
            </span>
            <div className="flex">
              <label htmlFor="amount">Number of servings:</label>
              <input
                type="number"
                name="amount"
                value={formData.amount}
                onChange={handleAmountChange}
                className="ml-2 w-12 border border-gray-300 rounded px-2 text-black"
                min="1"
              />
            </div>
            <span className="text-white">
              Total weight:{"   "}
              {formData.amount * recipe.nutrition?.weight_per_serving?.amount}g
            </span>
            <span className="text-white">
              Total carbohydrates:{"   "}
              {calculateGrams(
                recipe.nutrition?.weight_per_serving.amount,
                recipe.nutrition?.percent_carbs
              )}
              g
            </span>
            <span className="text-white">
              Total Fat:{"   "}
              {calculateGrams(
                recipe.nutrition?.weight_per_serving.amount,
                recipe.nutrition?.percent_fat
              )}
              g
            </span>
            <span className="text-white">
              Total Protein:{"   "}
              {calculateGrams(
                recipe.nutrition?.weight_per_serving.amount,
                recipe.nutrition?.percent_protein
              )}
              g
            </span>
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
