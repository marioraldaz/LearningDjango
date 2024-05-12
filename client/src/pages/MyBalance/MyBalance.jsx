import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { CardsList } from "../../components/Lists/CardsList.jsx";
import { useSelector, useDispatch } from "react-redux";
import { RecipeBalance } from "../../components/MyBalance/RecipeBalance.jsx";

export function MyBalance() {
  const [userDayIntakes, setUserDayIntakes] = useState([]);
  const [todaysRecipes, setTodaysRecipes] = useState([]);
  const { dayIntakes, getRecipe } = useContext(AuthContext);
  const dispatch = useDispatch();
  const recipes = useSelector((state) => state.recipes.recipes);

  useEffect(() => {
    const refreshIntakes = async () => {
      setUserDayIntakes(dayIntakes);
      let current = {};
      await dayIntakes.map(async (intake) => {
        const promises = await intake.details.map(async (intakeDetail) => {
          return await getRecipe(intakeDetail.recipe, recipes, dispatch);
        });
        Promise.all(promises).then((resolvedRecipes) => {
          current[intake.meal_type]
            ? current[intake.meal_type].push(resolvedRecipes[0])
            : (current[intake.meal_type] = resolvedRecipes);
        });
      });
      setTodaysRecipes(current);
    };
    refreshIntakes();
  }, [dayIntakes, getRecipe]);
  if (!todaysRecipes) {
    return <h1>Loading---</h1>;
  }
  return (
    <section className="w-full h-full">
      <h1 className="w-full gradient-text text-center text-4xl mb-8 p-8">
        MyBalance
      </h1>
      <h3 className="text-2xl text-center w-full mb-4">Today's Recipes</h3>
      {/* Use Object.entries to iterate over todaysRecipes */}
      <div className="m-8 main-w flex flex-col gap-8 overflow-y-auto items-center bg-neutral-700 p-4 rounded-lg">
        {Object.entries(todaysRecipes).map(([mealType, mealRecipes]) => (
          <div key={mealType} className="mb-4 w-full flex flex-col">
            <h4 className="text-xl mb-2">{mealType}</h4>
            {mealRecipes.map((meal, index) => (
              <RecipeBalance
                meal={meal}
                intake={dayIntakes[mealType]}
                key={index}
              />
            ))}
          </div>
        ))}
      </div>
    </section>
  );
}
