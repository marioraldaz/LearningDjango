import React, { useState } from "react";
import { GrayButton } from "../Buttons/GrayButton";

export function RecipeNutrition({ recipe }) {
  const nutrition = recipe.nutrition;
  const [flavonoids, setFlavonoids] = useState(false);
  const [selectedIngredient, setSelectedIngredient] = useState(null);
  const [showNutrients, setShowNutrients] = useState(false);
  const handleIngredientClick = (ingredient) => {
    setSelectedIngredient(ingredient);
  };

  console.log(nutrition);
  return (
    <div className="w-full h-full text-white bg-neutral-900 p-4 rounded-xl grid grid-auto-rows gap-8">
      <div className="w-min">
        <ul className="w-[300px]">
          <li>Carbs Percentage: {nutrition.percent_carbs} </li>
          <li>Fat Percentage: {nutrition.percent_fat}</li>
          <li>Protein Percentage: {nutrition.percent_protein}</li>
        </ul>
        <h3>
          Weight Per Serving:{" "}
          {nutrition.weight_per_serving[0]?.amount ||
            nutrition.weight_per_serving?.amount}{" "}
          {nutrition.weight_per_serving?.unit}
        </h3>
      </div>

      <div className="flex flex-col w-full gap-4">
        <div className="flex flex-col gap-4 w-full">
          <div
            className={`w-[250px] h-[60px] col-span-2 rounded-lg ${
              flavonoids ? "border" : ""
            }`}
          >
            <GrayButton
              onClick={() => {
                setFlavonoids(!flavonoids);
                showNutrients ? setShowNutrients(false) : "";
              }}
            >
              {flavonoids ? "Hide Flavonoids" : "Show Flavonoids"}
            </GrayButton>
          </div>
          <div
            className={`w-[250px] h-[60px] col-span-2 rounded-lg ${
              showNutrients ? "border" : ""
            }`}
          >
            <GrayButton
              on
              onClick={() => {
                setShowNutrients(!showNutrients);
                flavonoids ? setFlavonoids(false) : "";
              }}
            >
              {!showNutrients
                ? "Show Recipe Nutrients"
                : "Hide Recipe Nutrients"}
            </GrayButton>
          </div>
        </div>
        {flavonoids && (
          <div className="flex flex-col col-span-1 gap-4 border rounded-lg p-4 ">
            <h3 className="text-2xl mb-2">Flavonoids</h3>
            <ul className="flex flex-wrap overflow-y-scroll h-[300px]">
              {nutrition.flavonoids.map((elem) => (
                <ul
                  key={elem.name}
                  className="flex flex-row gap-4 w-full border p-4  odd:bg-rgb-rgb(0, 0, 0) even:bg-yellow-500 even:text-black"
                >
                  {console.log(elem)}
                  <li className="w-1/2">Name: {elem.name}</li>
                  <li>
                    Amount: {elem.amount} {elem.unit}
                  </li>
                </ul>
              ))}
            </ul>
          </div>
        )}

        {showNutrients && (
          <div className="flex flex-col col-span-1 gap-4 border rounded-lg p-4">
            <h3 className="text-2xl mb-2">Recipe Nutrients</h3>

            <ul className="overflow-y-scroll h-[300px]">
              {nutrition.nutrients.map((nutrient) => (
                <li
                  key={nutrient.name}
                  className="flex flex-row gap-4 w-full border p-4  odd:bg-rgb-rgb(0, 0, 0) even:bg-yellow-500 even:text-black"
                >
                  <li className="w-1/2">
                    {nutrient.name}: Amount: {nutrient.amount} {nutrient.unit}{" "}
                  </li>
                  <li>
                    Percentage Of Daily Needs: {nutrient.percentOfDailyNeeds}
                  </li>
                  {"%"}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
      <div className="flex flex-wrap gap-4 border p-4 rounded-xl  h-[300px] overflow-y-scroll">
        <h3 className="text-2xl">Ingredients</h3>
        {console.log(nutrition)}
        {recipe.extendedIngredients.map((ingredient) => (
          <ul key={ingredient.name} className="w-full flex gap-2 border-b">
            <li>Name: {ingredient.name}</li>
            <li>
              Amount: {ingredient.amount} {ingredient.unit}
            </li>
            <div className="ml-auto w-[300px] border rounded-lg mb-2">
              <GrayButton onClick={() => handleIngredientClick(ingredient)}>
                Show <span className="capitalize">{ingredient.name}</span>{" "}
                Nutrients
              </GrayButton>
            </div>
          </ul>
        ))}
      </div>

      {selectedIngredient && (
        <div className="border rounded-lg p-2">
          <h3 className="text-2xl mb-2 capitalize">
            {selectedIngredient.name} nutrients:
          </h3>
          <ul className="h-[350px] overflow-y-scroll ">
            {selectedIngredient.nutrients?.map((nutrient) => (
              <li key={nutrient.name} className=" border p-4">
                {nutrient.name}: Amount: {nutrient.amount} {nutrient.unit}{" "}
                Percentage Of Daily Needs: {nutrient.percentOfDailyNeeds}
              </li>
            ))}
          </ul>
        </div>
      )}

      <div className="w-full border rounded-lg p-2">
        <h3 className="text-2xl mb-4">Properties</h3>
        {nutrition.properties.map((elem) => (
          <ul key={elem.amount} className="flex gap-4">
            <li>{elem.name}:</li>
            <li>
              {elem.amount} {elem.unit}
            </li>
          </ul>
        ))}
      </div>
    </div>
  );
}
