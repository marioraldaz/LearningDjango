import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { CardsList } from "../../components/Lists/CardsList.jsx";
import { useSelector, useDispatch } from "react-redux";

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
          current[intake.meal_type] = resolvedRecipes;
        });
      });
      setTodaysRecipes(current);
    };
    console.log(todaysRecipes);
    refreshIntakes();
  }, [dayIntakes]);

  if (!todaysRecipes) {
    return <h1>Loading---</h1>;
  }
  return (
    <section className="w-full h-full">
      <h1 className="w-full gradient-text text-center text-3xl mb-8 p-8">
        MyBalance
      </h1>
      <h3 className="text-2xl text-center w-full mb-4">Today's Recipes</h3>
      {/* Use Object.entries to iterate over todaysRecipes */}
      <div className="m-8 w-4/5 flex flex-row gap-8 overflow-y-auto items-center bg-neutral-700 p-4 rounded-lg">
        {Object.entries(todaysRecipes).map(([mealType, mealRecipes]) => (
          <div key={mealType} className="mb-4">
            {/* Display the meal type as a heading */}
            <h4 className="text-xl mb-2">{mealType}</h4>
            {/* Render the list of recipes for the current meal type */}
            <div>
              {/* Assuming CardsList is a component that renders a list of recipes */}
              <CardsList products={mealRecipes} />
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
