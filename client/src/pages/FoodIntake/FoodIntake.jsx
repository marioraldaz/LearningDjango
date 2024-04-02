import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { CardsList } from "../../components/Lists/CardsList.jsx";
import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { IntakeForm } from "./IntakeForm.jsx";
import { purgePersistor } from "../../redux/store.js";
export function FoodIntake() {
  const [ingredients, setIngredients] = useState([]);
  const [recipeToAdd, setRecipeToAdd] = useState([]);
  const { addFoodIntake, user, getRecipe, savedRecipes } = useContext(
    AuthContext
  );
  const { add } = useParams();
  const persistRecipes = useSelector((state) => state.recipes.recipes);
  const dispatch = useDispatch();

  useEffect(() => {
    const getRecipeToAdd = async () => {
      setRecipeToAdd(await getRecipe(add, persistRecipes, dispatch));
    };
    getRecipeToAdd();
    purgePersistor();
    console.log(persistRecipes);
  }, [add]);

  if (!user) {
    return <h1>Loading...</h1>;
  }

  return (
    <div className="p-4 grid grid-cols-3 items-center justify-center">
      <div className="h-[400px] w-min flex flex-col overflow-y-auto items-center">
        <h3 className="">Recently Seen Recipes</h3>
        <CardsList products={persistRecipes} />
      </div>
      <div className="">
        <IntakeForm addFoodIntake={addFoodIntake} recipeToAdd={recipeToAdd} />
      </div>
      <div>
        <h3 className="">My Saved Recipes</h3>
        <CardsList products={savedRecipes} />
      </div>
    </div>
  );
}
