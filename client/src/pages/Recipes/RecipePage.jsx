import React, {useState, useEffect} from 'react'
import { getRecipeById } from '../../api/recipes.api'
import { useParams } from 'react-router-dom';
import { GrayButton } from '../../components/buttons/GrayButton';
export function RecipePage() {
    const { id } = useParams(); // Get the ID parameter from the URL
    const [recipe, setRecipe] = useState(null);
    const [showNutrition, setShowNutrition] = useState(false);
    useEffect(() => {
        console.log(id);
        const fetchRecipe = async () => {
            try {
                const res = await getRecipeById(id);
                setRecipe(res); // Assuming your API returns the entire recipe data object directly
                console.log(res); // Check the fetched recipe data in the console
            } catch (error) {
                console.error('Error fetching recipe:', error);
            }
        };

        if (id) { // Make sure ID is available before fetching the recipe
            fetchRecipe();
        }
    }, [id]); // Fetch recipe whenever ID changes

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
        <GrayButton onClick={toggleNutrition}>Show Nutrition</GrayButton>
        {showNutrition && }
    </div>
  )
}
