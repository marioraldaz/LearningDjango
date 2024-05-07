import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { CardsList } from "../../components/Lists/CardsList.jsx";
import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { IntakeForm } from "../../components/food_intake/IntakeForm.jsx";
import { purgePersistor } from "../../redux/store.js";
export function FoodIntake() {
  const [ingredients, setIngredients] = useState([]);
  const [recipeToAdd, setRecipeToAdd] = useState([]);

  const {
    addFoodIntake,
    user,
    getRecipe,
    savedRecipes,
    getDayIntakes,
  } = useContext(AuthContext);

  const { add } = useParams();
  const persistRecipes = useSelector((state) => state.recipes.recipes);
  const dispatch = useDispatch();

  useEffect(() => {
    const getRecipeToAdd = async () => {
      setRecipeToAdd(await getRecipe(add, persistRecipes, dispatch));
    };
    getRecipeToAdd();
    const dayIntakes = getDayIntakes();
    console.log(dayIntakes);
  }, [add]);

  const handleSubmit = (e) => {
    e.preventDefault();
  };

  if (!user) {
    return <h1>Loading...</h1>;
  }

  return (
    <section className="p-4 grid grid-cols-3 items-center justify-center">
      <div className="h-[700px] w-[430px] flex flex-col overflow-y-auto items-center bg-neutral-700 p-4 rounded-lg">
        <h3 className="text-2xl mb-4">Recently Seen Recipes</h3>
        <CardsList products={persistRecipes} />
      </div>
      <IntakeForm addFoodIntake={addFoodIntake} recipes={recipeToAdd} />
      <form className="" onSubmit={handleSubmit}></form>
      <div className="h-[700px] w-[430px] flex flex-col overflow-y-auto items-center bg-neutral-700 p-4 rounded-lg ml-auto">
        <h3 className="">My Saved Recipes</h3>
        <CardsList products={savedRecipes} />
      </div>
    </section>
  );
}
