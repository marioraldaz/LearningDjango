import React, { useState, useEffect, useContext } from "react";
import { getRecipeById } from "../../api/recipes.api";
import { useParams } from "react-router-dom";
import { GrayButton } from "../../components/Buttons/GrayButton";
import { RecipeNutrition } from "../../components/Recipes/RecipeNutrition";
import { useSelector, useDispatch } from "react-redux";
import { addRecipe } from "../../redux/recipesSlice";
import AuthContext from "../../context/AuthContext";

export function RecipePage() {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);
  const [showNutrition, setShowNutrition] = useState(false);
  const [showInstructions, setShowInstructions] = useState(false);
  const [saved, setSaved] = useState(false);
  const { saveRecipe, savedRecipes, unSaveRecipe, setSavedRecipes } =
    useContext(AuthContext);

  const recipes = useSelector((state) => state.recipes.recipes);
  const dispatch = useDispatch();

  useEffect(() => {
    const fetchRecipe = async () => {
      const recipeFound = recipes.find((recipeToFind) => {
        if (String(recipeToFind.id) == String(id)) {
          return recipeToFind;
        }
        return false;
      });
      if (recipeFound === undefined && id) {
        const res = await getRecipeById(id);
        setRecipe(res);
        dispatch(addRecipe(res));
      } else {
        setRecipe(recipeFound);
      }
      setSaved(false);
      savedRecipes.map((recipe) => {
        console.log(String(recipe), id);
        if (String(recipe) == id) {
          setSaved(true);
        }
      });
    };

    fetchRecipe();
  }, [id, savedRecipes]); // Fetch recipe whenever ID or recipes array changes

  const toggleNutrition = () => {
    setShowNutrition(!showNutrition);
  };

  const toggleInstructions = () => {
    setShowInstructions(!showInstructions);
  };

  const addToBalance = () => {};

  if (!recipe) {
    return <div>Loading...</div>;
  }
  return (
    <div className="flex flex-wrap flex-grow p-8 rounded-xl gap-8 min-h-[80vh]">
      <h1 className="w-full gradient-text text-center text-3xl mb-8">
        {recipe.title}{" "}
      </h1>
      <div className="w-full flex flex-wrap gap-8">
        {/*first row*/}
        <img
          src={recipe.image}
          alt={recipe.title}
          className="w-[700px] h-[400px] rounded-lg border"
        />
        <div className="flex flex-col gap-4 w-[200px]">
          <h2>Likes: {recipe.aggregateLikes}</h2>
          <div className="">
            Cooking Minutes:{" "}
            {recipe.cookingMinutes == -1
              ? "Not Specified"
              : recipe.cookingMinutes}
          </div>
          <div>Gluten Free: {recipe.glutenFree ? "Yes" : "No"}</div>
          <div>Dairy Free: {recipe.dairyFree ? "Yes" : "No"}</div>
        </div>
        <div
          className="ml-auto w-[750px] bg-neutral-800 p-4 rounded-lg justify-center items-center"
          dangerouslySetInnerHTML={{ __html: recipe.summary }}
        />
      </div>
      <div className="w-full flex flex-wrap gap-8">
        {/*second row*/}

        <div className="h-[60px] flex gap-4">
          {!saved && (
            <GrayButton
              onClick={() => {
                saveRecipe(recipe.id);
                setSaved(true);
                setSavedRecipes([...savedRecipes, recipe]);
              }}
            >
              Save Recipe
            </GrayButton>
          )}
          {saved && (
            <GrayButton
              onClick={() => {
                unSaveRecipe(recipe.id);
                setSaved(false);
                setSavedRecipes(
                  savedRecipes.filter(
                    (savedRecipe) => savedRecipe.id !== recipe.id
                  )
                );
              }}
            >
              Unsave Recipe
            </GrayButton>
          )}
          <GrayButton onClick={addToBalance}>Log Recipe For Today</GrayButton>
          <GrayButton onClick={toggleNutrition}>
            {!showNutrition ? "Show Nutrition" : "Hide Nutrition"}
          </GrayButton>
          <GrayButton onClick={toggleInstructions}>
            {!showInstructions ? "Show Instructions" : "Hide Instructions"}
          </GrayButton>
        </div>

        <div className="border p-2 rounded-lg ">
          <h2 className="mb-8">Compatible Diets </h2>
          <ul className="flex items-center">
            {recipe.diets.map((diet) => (
              <li key={diet} className="flex flex-row gap-4 w-full border p-4">
                {diet}
              </li>
            ))}
            {recipe.diets.length == 0 && (
              <h3 className="text-2xl">No Compatible Diets Were Saved</h3>
            )}
          </ul>
        </div>
      </div>
      <div className="">
        {showNutrition && <RecipeNutrition nutrition={recipe.nutrition} />}
      </div>

      {showInstructions && (
        <div className="">
          {recipe.instructions.length > 0 && (
            <div className="flex flex-col">
              <h2 className="text-2xl mb-2">Instructions:</h2>
              <div dangerouslySetInnerHTML={{ __html: recipe.instructions }} />
            </div>
          )}
          <ol className="list-decimal">
            {recipe.analyzedInstructions[0].steps.map((instruction, index) => (
              <li
                key={index}
                className="flex flex-row gap-4 items-center p-4 border-b border-gray-500 border-b-0.5 "
              >
                {index + ". " + instruction.step}
              </li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
}
