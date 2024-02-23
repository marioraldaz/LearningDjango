import axios from "axios";

const API_KEY = "72ed57384eea4e91b4390428f582a705";

const options = {
  method: "GET",
  url: " https://api.spoonacular.com/recipes/complexsearch",
};

export async function fetchDataFromApi() {
  try {
    const response = await axios.request(
      "https://api.spoonacular.com/recipes/findByNutrients?apiKey=" +
        API_KEY +
        "&maxCarbs=15"
    );
    console.log(response.data);
    console.log(response.data.results);
  } catch (error) {
    console.error(error);
  }
}
