import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { CardsList } from "../../components/Lists/CardsList.jsx";
import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { IntakeForm } from "../../components/food_intake/IntakeForm.jsx";
import { purgePersistor } from "../../redux/store.js";
import persistReducer from "redux-persist/es/persistReducer";

export function FoodIntake() {
  const [ingredients, setIngredients] = useState([]);
  const [recipeToAdd, setRecipeToAdd] = useState([]);
  const { addFoodIntake, user, getRecipe, savedRecipes } =
    useContext(AuthContext);
  const { add } = useParams();
  const persistRecipes = useSelector((state) => state.recipes.recipes);
  const dispatch = useDispatch();

  useEffect(() => {
    purgePersistor();
    console.log("TRIGGERED", persistRecipes);
    const getRecipeToAdd = async () => {
      setRecipeToAdd(await getRecipe(add, persistRecipes, dispatch));
    };
    getRecipeToAdd();
  }, [add]);

  if (!user) {
    return <h1>Loading...</h1>;
  }

  return (
    <section className="p-4 grid 2xl:grid-cols-3 xl:grid-cols-2 bg-black grid-cols-1 mt-[50px] justify-center items-center px-10">
      <div className="order-2 2xl:order1 h-[700px] w-[430px] xl:ml-[200px] 2xl:ml-0 flex flex-col overflow-y-auto items-center bg-neutral-700 p-4 rounded-lg ml-auto mr-auto mt-4">
        <h3 className="text-2xl mb-4 ">Recently Seen Recipes</h3>
        <CardsList products={persistRecipes} />
      </div>
      <div className="order-1 2xl:order-2">
        <IntakeForm addFoodIntake={addFoodIntake} recipes={[recipeToAdd]} />
      </div>
      <div className="order-3 2xl:order-3 h-[700px] w-[430px] flex flex-col overflow-y-auto items-center bg-neutral-700 p-4 rounded-lg ml-auto xl:mr-0 mr-auto mt-4">
        <h3 className="text-2xl mb-4">My Saved Recipes</h3>
        <CardsList products={savedRecipes} />
      </div>
    </section>
  );
}
