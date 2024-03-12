import axios from "axios";

const API_KEY = "72ed57384eea4e91b4390428f582a705";


export const fetchFilteredRecipes = async (filters) => {
    const params = new URLSearchParams();
    Object.entries(filters).forEach((filter) => {
      if (filter[1] !== "") {
        params.append(filter[0], filter[1]);
      }
    });
    console.log(params.toString());
    const response = await fetch(
      `https://api.spoonacular.com/recipes/complexSearch?apiKey=${API_KEY}&${params.toString()}`
    );
  
    if (!response.ok) {
      throw new Error("Failed to fetch ingredients");
    }
  
    const data = await response.json();
    return data.results;
  };
  
  export async function getRecipeInfo(id) {
    try {
      const response = await axios.request(
        `https://api.spoonacular.com/recipes/${id}/information?apiKey=` +
          API_KEY
      );
      return response;
    } catch (error) {
      console.error(error);
    }
  }

  export async function fetchRecipesByName(name) {
    try {
      const response = await axios.request(
        "https://api.spoonacular.com/recipes/complexSearch?apiKey=" +
          API_KEY +
          "&query=" +
          name+"&sort=popularity"
      );
      return response.data.results;
    } catch (error) {
      console.error(error);
    }
  }


  export async function getRecipeById(recipeId) {
    try {
      const response = await axios.get(
        `https://api.spoonacular.com/recipes/${recipeId}/information?apiKey=${API_KEY}&includeNutrition=true`
      );
      return response.data;
    } catch (error) {
      console.error(error);
    }
  }