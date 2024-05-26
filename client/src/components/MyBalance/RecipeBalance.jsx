import React, { useEffect, useState } from "react";
import { CardsList } from "../Lists/CardsList.jsx";
import { RecipeNutrition } from "../Recipes/RecipeNutrition.jsx";
import { NutritionForm } from "./NutritionForm.jsx";
import { GrayButton } from "../Buttons/GrayButton.jsx";
export function RecipeBalance({ meal, intake }) {
  const [showUpdateNutrition, setShowUpdateNutrition] = useState(false);
  const [hasNutrition, setHasNutrition] = useState(false);
  useEffect(() => {
    typeof meal.nutrition === "object"
      ? setHasNutrition(true)
      : setHasNutrition(false);
  }, []);

  const toggleShowUpdateNutrition = () => {
    setShowUpdateNutrition(!showUpdateNutrition);
  };
  return (
    <div className="flex flex-col xl:flex-row w-full border h-full border-black mt-4 p-4 overflow-auto ">
      <div className="w-min">
        <CardsList products={[meal]} />
      </div>
      <div className=" flex items-center justify-center">
        {!hasNutrition && !showUpdateNutrition && (
          <div className="m-4 p-4 text-xl  h-1/3">
            <GrayButton onClick={toggleShowUpdateNutrition}>
              Recipe has no nutrition, click here to insert it!
            </GrayButton>
          </div>
        )}
        {hasNutrition && <RecipeNutrition recipe={meal} />}
        {showUpdateNutrition && <NutritionForm id={meal.id} />}
      </div>
    </div>
  );
}
