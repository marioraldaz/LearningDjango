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
            const recipeFound = recipes.find((recipeToFind) => {
                if(String(recipeToFind.id) == String(id)){
                    return recipeToFind;
                }
                return false;
            })
            console.log(recipeFound);
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
    
    <div className="grid grid-cols-2 p-8 rounded-xl gap-4"> 
        <div dangerouslySetInnerHTML={{ __html: recipe.summary }} />

        <img src={recipe.image}/>
        <h2>Likes: {recipe.aggregateLikes}</h2>

        {recipe.instructions.length>0 &&
        <div className="">
            <div dangerouslySetInnerHTML={{ __html: recipe.instructions }} />
            <h2>Instructions:</h2>
        </div>
        }

        <div className="">Cooking Minutes: {recipe.cookingMinutes==-1 ? "Not Specified" : recipe.cookingMinutes}</div>
        <div >Gluten Free: {recipe.glutenFree ? "Yes" : "No" }</div>
        <div className="w-[150px] h-[60px]">
            <GrayButton onClick={toggleNutrition}>{!showNutrition ? "Show Nutrition" : "Hide Nutrition" }</GrayButton>
        </div>
        {showNutrition && 
        <div className="col-span-2">
            <RecipeNutrition nutrition={recipe.nutrition}/>
        </div>
        }
    </div>
  )
}
