import axios from "axios";
const API_KEY2 = "72ed57384eea4e91b4390428f582a705";
const API_KEY = "8347c0a7ffc148269108ea0a29f1509e";

const IngredientsApi = axios.create({
  baseURL: "http://localhost:800/food/ingredients",
});

export async function fetchIngredientsByName(name) {
  try {
    const response = await axios.request(
      "https://api.spoonacular.com/food/ingredients/search?apiKey=" +
        API_KEY +
        "&query=" +
        name
    );
    console.log(response.data);
    return response.data.results;
  } catch (error) {
    console.error(error);
  }
}

export async function getIngredientById(id, amount) {
  try {
    const response = await axios.request(
      `https://api.spoonacular.com/food/ingredients/${id}/information?amount=${amount}&apiKey=` +
        API_KEY
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
}
export const fetchFilteredIngredients = async (filters) => {
  const params = new URLSearchParams();
  Object.entries(filters).forEach((filter) => {
    if (filter[1] !== "") {
      params.append(filter[0], filter[1]);
    }
  });
  console.log(params.toString());
  const response = await fetch(
    `https://api.spoonacular.com/food/ingredients/search?apiKey=${API_KEY}&${params.toString()}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch ingredients");
  }

  const data = await response.json();
  return data.results;
};
