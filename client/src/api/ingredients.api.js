import axios from "axios";

const BASE_URL = process.env.BASE_URL || "http://localhost:8000"; // Adjust the base URL as needed

export async function fetchIngredientsByName(name) {
  try {
    const response = await axios.get(
      `${BASE_URL}/fetch-ingredients-by-name/${name}/`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw new Error("Failed to fetch ingredients by name");
  }
}

export async function getIngredientDetails(ingredientId, amount) {
  try {
    const response = await axios.get(
      `${BASE_URL}/get-ingredient-details/${ingredientId}/${amount}/`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw new Error("Failed to get ingredient details");
  }
}

export async function fetchFilteredIngredients(filters) {
  try {
    const response = await axios.get(
      `${BASE_URL}/fetch-filtered-ingredients/`,
      { params: filters }
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw new Error("Failed to fetch filtered ingredients");
  }
}
export async function getIngredientById(id, amount) {
  try {
    const response = await axios.get(
      `${BASE_URL}/api/get-ingredient-details/${id}/${amount}/`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw new Error("Failed to fetch ingredient details");
  }
}
