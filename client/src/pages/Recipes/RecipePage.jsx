import React, {useState, useEffect} from 'react'
import { getRecipeById } from '../../api/recipes.api'
import { useParams } from 'react-router-dom';
import { GrayButton } from '../../components/buttons/GrayButton';
import { RecipeNutrition } from '../../components/recipes/RecipeNutrition';
import { useSelector, useDispatch } from 'react-redux';
import { addRecipe } from '../../redux/recipesSlice';

export function RecipePage() {
    const { id } = useParams();
    const [recipe, setRecipe] = useState(null);
    const [showNutrition, setShowNutrition] = useState(false);
    const recipes = useSelector(state => state.recipes.recipes);
    const dispatch = useDispatch();

    useEffect(() => {
        const fetchRecipe = async () => {
            const recipeFound = recipes.find((recipeToFind) => recipeToFind.id === id);
            console.log(recipes);
      
            if (recipeFound === undefined && id) {
              const res = await getRecipeById(id);
              setRecipe(res);
              dispatch(addRecipe(res));
            } else {
              setRecipe(recipeFound);
            }
          
        };
      
        fetchRecipe();
      }, [id]); // Fetch recipe whenever ID or recipes array changes
      

    const toggleNutrition = ()=>{
        setShowNutrition(!showNutrition);
    }
    
    if (!recipe) {
        return <div>Loading...</div>;
    }
  return (
    
    <div className="flex flex-wrap"> 
        <h2>Likes: {recipe.aggregateLikes}</h2>
        <h2>Instructions:</h2>
        <div className="">Cooking Minutes: {recipe.cookingMinutes}</div>
        <div dangerouslySetInnerHTML={{ __html: recipe.instructions }} />
        <div >Gluten Free {recipe.glutenFree ? "yes" : "No" }</div>
        <img src={recipe.image}/>
        <GrayButton onClick={toggleNutrition}>{showNutrition ? "Show Nutrition" : "Hide Nutrition" }</GrayButton>
        {showNutrition && <RecipeNutrition nutrition={recipe.nutrition}/>}
    </div>
  )
}
