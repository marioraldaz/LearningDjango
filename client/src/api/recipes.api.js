import axios from "axios";

export const BASE_URL = process.env.BASE_URL || "http://localhost:8000";

export const fetchFilteredRecipes = async (filters) => {
  try {
    const params = new URLSearchParams();
    Object.entries(filters).forEach((filter) => {
      if (filter[1] !== "") {
        params.append(filter[0], filter[1]);
      }
    });
    console.log(params.toString());
    const response = await axios.get(
      `${BASE_URL}/recipes/fetch-filtered-recipes/?${params.toString()}`
    );

    if (!response.data) {
      throw new Error("Failed to fetch recipes");
    }

    return response.data;
  } catch (error) {
    console.error(error);
    throw error; // Rethrow the error for handling in the calling code
  }
};

export async function getRecipeInfo(id) {
  try {
    const response = await axios.get(
      `${BASE_URL}/recipes/get-recipe-info/${id}/`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw error; // Rethrow the error for handling in the calling code
  }
}

export async function fetchRecipesByName(name) {
  try {
    const response = await axios.get(
      `${BASE_URL}/recipes/fetch-recipes-by-name/name=${name}`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw error; // Rethrow the error for handling in the calling code
  }
}

export async function getRecipeById(recipeId) {
  try {
    const response = await axios.get(
      `${BASE_URL}/recipes/get-recipe-by-id/${recipeId}/`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw error; // Rethrow the error for handling in the calling code
  }
}
