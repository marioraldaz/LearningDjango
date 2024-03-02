import axios from "axios";

const API_KEY = "72ed57384eea4e91b4390428f582a705";

const options = {
  method: "GET",
  url: " https://api.spoonacular.com/recipes/complexsearch",
};

export async function fetchDataFromApi() {
  try {
    const response = await axios.request(
      "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + API_KEY
    );
    console.log(response.data);
    console.log(response.data.results);
    return response.data.results;
  } catch (error) {
    console.error(error);
  }
}

export async function fetchIngredientsByName(name) {
  try {
    const response = await axios.request(
      "https://api.spoonacular.com/food/ingredients/search?apiKey=" +
        API_KEY +
        "&query=" +
        name
    );
    return response.data.results;
  } catch (error) {
    console.error(error);
  }
}

export async function getIngredientInfo(id) {
  try {
    const response = await axios.request(
      `https://api.spoonacular.com/food/ingredients/${id}/information?apiKey=` +
        API_KEY
    );
    return response;
  } catch (error) {
    console.error(error);
  }
}
export const fetchFilteredIngredients = async (filters) => {
  const params = new URLSearchParams();

  filters.forEach((filter) => {
    if (filter.value !== "") {
      params.append(filter.name, filter.value);
    }
  });
  console.log(params);
  const response = await fetch(
    `https://api.spoonacular.com/food/ingredients/search?${params.toString()}&apiKey=${API_KEY}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch ingredients");
  }

  const data = await response.json();
  return data.results;
};
