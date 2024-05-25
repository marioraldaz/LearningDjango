import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { CardsList } from "../../components/Lists/CardsList.jsx";
import { useSelector, useDispatch } from "react-redux";
import { RecipeBalance } from "../../components/MyBalance/RecipeBalance.jsx";
import { NavigationButton } from "../../components/Buttons/NavigationButton.jsx";

export function MyBalance() {
  const [userDayIntakes, setUserDayIntakes] = useState([]);
  const [todaysRecipes, setTodaysRecipes] = useState([]);
  const { dayIntakes, getRecipe, user } = useContext(AuthContext);
  const dispatch = useDispatch();
  const recipes = useSelector((state) => state.recipes.recipes);

  useEffect(() => {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, "0"); // Months are zero-indexed, so add 1 and pad with leading zero if necessary
    const day = String(today.getDate()).padStart(2, "0"); // Pad with leading zero if necessary

    // Format the date as 'YYYY-MM-DD'
    const formattedDate = `${year}-${month}-${day}`;
    const intakes = dayIntakes.map((intake) => {
      if (intake["date"] == formattedDate) {
        return intake;
      }
    });
    setTodaysRecipes(intakes);
  }, [dayIntakes]);

  if (!user) {
    return (
      <div>
        <h1>Log In To Access this page !</h1>
        <NavigationButton link="/login" text="Go to login" />
      </div>
    );
  }
  if (!todaysRecipes && user) {
    return <h1>Loading---</h1>;
  }
  return (
    <section className="w-full h-full">
      <h1 className="w-full gradient-text text-center text-4xl mb-8 p-8">
        MyBalance
      </h1>
      <h3 className="text-2xl text-center w-full mb-4">Today's Recipes</h3>
      {/* Use Object.entries to iterate over todaysRecipes */}
      <div className="m-8 flex flex-col gap-8 overflow-y-auto items-center bg-neutral-700 p-4 rounded-lg">
        {Object.entries(todaysRecipes).map(([index, intake]) => (
          <div key={index} className="mb-4 w-full flex flex-col">
            <h4 className="text-xl mb-2">{intake["mealType"]}</h4>
            {console.log(intake, intake["details"].recipe)}
            <RecipeBalance
              meal={intake["details"][0]["recipe"]}
              intake={intake}
              key={index}
            />
          </div>
        ))}
      </div>
    </section>
  );
}
