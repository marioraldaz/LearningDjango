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

    <div className="w-full h-full text-white bg-neutral-900 p-4 rounded-xl grid grid-cols-2 gap-8 capitalize">
      <ul className="w-[350px]">
        <li>Carbs Percentage: {nutrition.caloricBreakdown.percentCarbs} </li>
        <li>Fat Percentage: {nutrition.caloricBreakdown.percentFat}</li>
        <li>Protein Percentage: {nutrition.caloricBreakdown.percentProtein}</li>
      </ul>
        <h3>Weight Per Serving: {nutrition.weightPerServing.amount} {nutrition.weightPerServing.unit}</h3>
        
      <div className="col-span-2">
        <div className="w-[250px] h-[60px] col-span-2 border rounded-lg">
          <GrayButton onClick={() => setFlavonoids(!flavonoids)}>{flavonoids ? "Hide Flavonoids" : "Show Flavonoids"}</GrayButton>
        </div>
        {flavonoids && (
        <div className="flex flex-col col-span-1 gap-4">
        <h3 className="text-2xl">Flavonoids</h3>
          <ul className="flex flex-wrap overflow-y-scroll h-[300px]">
            {nutrition.flavonoids.map((elem) => (
              <ul key={elem.name} className="flex flex-row gap-4 w-full border p-4">
                <li className="w-1/2">Name: {elem.name}</li>
                <li>Amount: {elem.amount} {elem.unit}</li>
              </ul>
            ))}
          </ul>
            </div>
        )}
      </div>
      <div className="flex flex-col gap-4 border p-4 rounded-xl  h-[300px] overflow-y-scroll">
      <h3 className="text-2xl">Ingredients</h3>
        {nutrition.ingredients.map((ingredient) => (
          <ul key={ingredient.name} className="w-full flex rounded-lg gap-2">
            <li>Name: {ingredient.name}</li>
            <li>Amount: {ingredient.amount} {ingredient.unit}</li>
            <div className="ml-auto w-[300px] border rounded-lg">
              <GrayButton onClick={() => handleIngredientClick(ingredient)}>Show <span className="capitalize">{ingredient.name}</span> Nutrients</GrayButton>
            </div>
          </ul>
        ))}
      </div>
      {selectedIngredient && (
        <div className="">
            <h3 className='text-2xl'>{selectedIngredient.name} nutrients:</h3>
          <ul className="h-[350px] overflow-y-scroll " >
            {selectedIngredient.nutrients.map((nutrient) => (
              <li key={nutrient.name} className=" border p-4">
                {nutrient.name}: Amount: {nutrient.amount} {nutrient.unit} Percentage Of Daily Needs: {nutrient.percentOfDailyNeeds}
              </li>
            ))}
            </ul>
        </div>
      )}
      <div className="w-[250px] h-[60px]">
        <GrayButton on onClick={()=>{setShowNutrients(!showNutrients)}}>{!showNutrients ? "Show Recipe Nutrients" : "Hide Recipe Nutrients"}</GrayButton>
      </div>
      {showNutrients && 
      <ul className="">
        
      </ul>
      }
      <div className='w-full border rounded-lg p-2'>
      <h3 className="text-2xl mb-4">Properties</h3>
        {nutrition.properties.map((elem)=>
            <ul key={elem.amount} className="flex gap-4">
                <li>{elem.name}:</li>
                <li>{elem.amount} {elem.unit}</li>
            </ul>
        )}
      </div>
    </div>
  );
}



