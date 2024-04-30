import axios from "axios";

// Define base URL for API requests
const baseUrl = "http://localhost:8000/api";

// Function to fetch food intake details by ID
async function fetchFoodIntakeDetails(pk) {
  const url = `${baseUrl}/food-intake/${pk}/details/`;
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(`Error fetching food intake details for ID ${pk}:`, error);
    throw error;
  }
}

// Function to fetch user dailies by profile ID
async function fetchUserDailies(profileId) {
  const url = `${baseUrl}/user-dailies/${profileId}/`;
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(
      `Error fetching user dailies for profile ID ${profileId}:`,
      error
    );
    throw error;
  }
}

// Function to fetch user daily detail by profile ID and entry ID
async function fetchUserDailyDetail(profileId, entryId) {
  const url = `${baseUrl}/user-dailies/${profileId}/${entryId}/`;
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(
      `Error fetching user daily detail for profile ID ${profileId} and entry ID ${entryId}:`,
      error
    );
    throw error;
  }
}

// Function to fetch list of food intakes for a user daily
async function fetchListFoodIntakes() {
  const url = `${baseUrl}/user-daily/list-food-intakes/`;
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error("Error fetching list of food intakes:", error);
    throw error;
  }
}

// Function to fetch nutrition stats detail by profile ID
async function fetchNutritionStats(profileId) {
  const url = `${baseUrl}/nutrition-stats/${profileId}/`;
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(
      `Error fetching nutrition stats for profile ID ${profileId}:`,
      error
    );
    throw error;
  }
}

async function createFoodIntake(data) {
  const url = `${baseUrl}/food-intake/`;
  try {
    const response = await axios.post(url, data);
    return response.data;
  } catch (error) {
    console.error("Error creating food intake:", error);
    throw error;
  }
}

// Function to update a food intake entry by ID
async function updateFoodIntake(pk, data) {
  const url = `${baseUrl}/food-intake/${pk}/`;
  try {
    const response = await axios.put(url, data);
    return response.data;
  } catch (error) {
    console.error(`Error updating food intake for ID ${pk}:`, error);
    throw error;
  }
}

// Function to delete a food intake entry by ID
async function deleteFoodIntake(pk) {
  const url = `${baseUrl}/food-intake/${pk}/`;
  try {
    const response = await axios.delete(url);
    return response.data;
  } catch (error) {
    console.error(`Error deleting food intake for ID ${pk}:`, error);
    throw error;
  }
}

s;
export {
  fetchFoodIntakeDetails,
  fetchUserDailies,
  fetchUserDailyDetail,
  fetchListFoodIntakes,
  createFoodIntake,
  updateFoodIntake,
  deleteFoodIntake,
  fetchNutritionStats,
};
