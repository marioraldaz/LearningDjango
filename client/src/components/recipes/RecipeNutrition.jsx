import React, { useState } from 'react';
import { GrayButton } from '../buttons/GrayButton';

export function RecipeNutrition({ nutrition }) {
  const [flavonoids, setFlavonoids] = useState(false);
  const [selectedIngredient, setSelectedIngredient] = useState(null);
  const [showNutrients, setShowNutrients] = useState(false);
  const handleIngredientClick = (ingredient) => {
    setSelectedIngredient(ingredient);
  };
  console.log(nutrition)
  return (
    <div>
      <ul className="">
        <li>Carbs Percentage: {nutrition.caloricBreakdown.percentCarbs} </li>
        <li>Fat Percentage: {nutrition.caloricBreakdown.percentFat}</li>
        <li>Protein Percentage: {nutrition.caloricBreakdown.percentProtein}</li>
      </ul>
      {flavonoids && (
        <ul className="">
          {nutrition.flavonoids.map((elem) => (
            <ul key={elem.name} className="">
              <li>Name: {elem.name}</li>
              <li>Amount: {elem.amount}</li>
              <li>Unit: {elem.unit}</li>
            </ul>
          ))}
        </ul>
      )}
      <div className="">
        {nutrition.ingredients.map((ingredient) => (
          <ul key={ingredient.name} className="">
            <li>Name: {ingredient.name}</li>
            <li>Amount: {ingredient.amount}</li>
            <li>Unit: {ingredient.unit}</li>
            <GrayButton onClick={() => handleIngredientClick(ingredient)}>Show {ingredient.name} Nutrients</GrayButton>
          </ul>
        ))}
      </div>
      {selectedIngredient && (
        <div className="">
          <ul>
            {selectedIngredient.nutrients.map((nutrient) => (
              <li key={nutrient.name}>
                {nutrient.name}: Amount: {nutrient.amount} Unit: {nutrient.unit} Percentage Of Daily Needs: {nutrient.percentageOfDailyNeeds}
              </li>
            ))}
          </ul>
        </div>
      )}
    <GrayButton on onClick={()=>{setShowNutrients(!showNutrients)}}>{showNutrients ? "Show Recipe Nutrients" : "Hide Recipe Nutrients"}</GrayButton>
      {showNutrients && 
      <ul className="">
        
      </ul>
      }
      <h3>Properties</h3>
      <div>
        {nutrition.properties.map((elem)=>{
            <ul key={elem.name}>
                <li>{elem.name}</li>
                <li>{elem.amount}</li>
                <li>{elem.unit}</li>
            </ul>
        })}
      </div>
      <div>
        <h3>Weight Per Serving: {nutrition.weightPerServing.amount} Unit: {nutrition.weightPerServing.unit}</h3>
      </div>
    </div>
  );
}



