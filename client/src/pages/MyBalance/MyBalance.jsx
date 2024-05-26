import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { useSelector, useDispatch } from "react-redux";
import { NavigationButton } from "../../components/Buttons/NavigationButton.jsx";
import { Scrollable } from "../../components/MyBalance/Scrollable.jsx";
import { Stats } from "../../components/Stats/Stats.jsx";
export function MyBalance() {
  const [loading, setLoading] = useState(true);
  const [userIntakes, setUserIntakes] = useState([]);
  const [todaysRecipes, setTodaysRecipes] = useState([]);
  const { getUserIntakes, user } = useContext(AuthContext);
  const dispatch = useDispatch();
  const recipes = useSelector((state) => state.recipes.recipes);

  useEffect(() => {
    const fetchData = async () => {
      const today = new Date();
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, "0"); // Months are zero-indexed, so add 1 and pad with leading zero if necessary
      const day = String(today.getDate()).padStart(2, "0"); // Pad with leading zero if necessary
      const fetchedIntakes = await getUserIntakes();
      // Format the date as 'YYYY-MM-DD'
      const formattedDate = `${year}-${month}-${day}`;
      const filtered = fetchedIntakes.filter(
        (intake) => intake.date === formattedDate
      );

      setTodaysRecipes(filtered);
      setUserIntakes(fetchedIntakes);
      setLoading(false);
    };
    fetchData();
  }, [user?.id]);

  if (loading) {
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
      <Scrollable recipes={todaysRecipes} />
      <h1 className="w-full gradient-text text-center text-4xl mb-8 p-8">
        Stats
      </h1>
      <Stats profile={user} />
    </section>
  );
}
