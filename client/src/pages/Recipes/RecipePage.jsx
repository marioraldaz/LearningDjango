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

    const saveRecipe =()=>{

    }

    const addToBalance = ()=>{
    }
    
    if (!recipe) {
        return <div>Loading...</div>;
    }
  return (
    
    <div className="flex flex-wrap p-8 rounded-xl gap-8"> 

        <h1 className="w-full gradient-text text-center text-2xl"> {recipe.title} </h1>
        <div className="w-full h-[400px] flex gap-8"> {/*first row*/}
            <img src={recipe.image} alt={recipe.title} className="w-1/2 h-auto" />
            <div className="flex flex-col gap-4">
                <h2>Likes: {recipe.aggregateLikes}</h2>
                <div className="">Cooking Minutes: {recipe.cookingMinutes==-1 ? "Not Specified" : recipe.cookingMinutes}</div>
                <div >Gluten Free: {recipe.glutenFree ? "Yes" : "No" }</div>
                <div >Dairy Free: {recipe.dairyFree ? "Yes" : "No" }</div>  
            </div>
            <div className="ml-auto w-1/2" dangerouslySetInnerHTML={{ __html: recipe.summary }} />
        </div>

        <div className="w-full flex gap-8">{/*second row*/}
            <div className="w-[300px] h-[60px] flex flex-col gap-4">
                <GrayButton onClick={saveRecipe}>Save Recipe</GrayButton>
                <GrayButton onClick={addToBalance}>Log Recipe For Today</GrayButton>  
                <GrayButton onClick={toggleNutrition}>{!showNutrition ? "Show Nutrition" : "Hide Nutrition" }</GrayButton>
            </div>
            <div className="border w-[300px] p-2 rounded-lg ">
                <h2 className='mb-8'>Compatible Diets </h2>
                <ul className="overflow-x-scroll flex h-[100px]">
                    {recipe.diets.map((diet) => (
                        <li key={diet} className='flex flex-row gap-4 w-full border p-4'>{diet}</li>
                        ))}
                        {recipe.diets.length==0 && <h3 className='text-2xl'>No Compatible Diets Were Saved</h3>}
                </ul>
            </div>
        </div>

        {showNutrition && 
        <div className="col-span-2">
            <RecipeNutrition nutrition={recipe.nutrition}/>
        </div>
        }

        {recipe.instructions.length>0 &&
        <div className=""> {/* <last row> */}
            <div dangerouslySetInnerHTML={{ __html: recipe.instructions }} />
            <h2>Instructions:</h2>
        </div>
        }
    </div>
  )
}
