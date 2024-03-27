import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { NavigationButton } from "../../components/Buttons/NavigationButton";
import { GrayButton } from "../../components/Buttons/GrayButton";
import { CardsList } from "../../components/Lists/CardsList.jsx";
import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";

export function FoodIntake() {
  const [formData, setFormData] = useState({
    meal_type: "Breakfast",
    intake_date: null,
    profile_id: null,
  });
  const [ingredients, setIngredients] = useState([]);
  const [recipeToAdd, setRecipeToAdd] = useState([]);
  const { addFoodIntake, user, getRecipe } = useContext(AuthContext);
  const { add } = useParams();
  const recipes = useSelector((state) => state.recipes.recipes);
  const dispatch = useDispatch();

  useEffect(() => {
    const getRecipeToAdd = async () => {
      setRecipeToAdd(await getRecipe(add, recipes, dispatch));
    };
    getRecipeToAdd();
  }, [add]);

  const handleSubmit = (e) => {
    history.push("/FoodIntake");

    e.preventDefault();
    addFoodIntake(formData);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  if (!user) {
    return <h1>Loading...</h1>;
  }

  return (
    <div className="h-full overflow-hidden gap-8 tex-center text-xl m-12 flex bg-neutral-900 items-center justify-center">
      <div className="">
        <form className="flex flex-col gap-4 mb-8" onSubmit={handleSubmit}>
          <h3 className="text-3xl gradient-text text-center mt-8 mb-4">
            Log Your Meal
          </h3>
          <div className="grid grid-cols-2 gap-4">
            <CardsList products={[recipeToAdd]} />
            <div className="flex gap-4 items-center justify-center">
              <label htmlFor="meal_type">Type:</label>
              <select
                name="meal_type"
                className="text-black h-8"
                value={formData.meal_type}
                onChange={handleInputChange}
              >
                <option value="Breakfast">Breakfast</option>
                <option value="Lunch">Lunch</option>
                <option value="Dinner">Dinner</option>
                <option value="Snack">Snack</option>
              </select>
            </div>
          </div>

          <div className="">
            <GrayButton onClick={handleSubmit}>Log For Today</GrayButton>
          </div>
        </form>

        <div className="">
          <h3 className="text-2xl">Search For Recipes</h3>
          <NavigationButton link="/Recipes" text="Recipes" />
        </div>

        <div className="">
          <h3 className="text-2xl">Save Your Own Recipe</h3>
          <NavigationButton link="/Recipes" text="Create Recipe" />
        </div>

        <div className="">
          <h3 className="text-2xl">Search For Ingredients</h3>
          <NavigationButton link="/Ingredients" text="Search For Ingredients" />
        </div>
      </div>
      <div className="">
        <CardsList products={ingredients} />
      </div>
    </div>
  );
}
