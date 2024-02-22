import axios from "axios";

const API_KEY = "72ed57384eea4e91b4390428f582a705";

const options = {
  method: "GET",
  url: " https://api.spoonacular.com/recipes/complexsearch",
};

export async function fetchDataFromApi() {
  try {
    const response = await axios.request(
      "https://api.spoonacular.com/recipes/complexSearch?apiKey=" +
        API_KEY +
        "&query=pasta&maxFat=25&number=2"
    );
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}
