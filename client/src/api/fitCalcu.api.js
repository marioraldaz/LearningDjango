import axios from "axios";
export const BASE_URL = "http://localhost:8000/api";

export const getActivityLevelByNumber = (number) => {
  switch (number) {
    case 1:
      return "sedentary";
    case 2:
      return "lightly_active";
    case 3:
      return "moderately_active";
    case 4:
      return "very_active";
    case 5:
      return "super_active";
    default:
      return "";
  }
};

export const cmToMeters = (heightCm) => {
  return (heightCm / 100).toFixed(2);
};

export const calculateAge = (birthDateString) => {
  const birthDate = new Date(birthDateString);
  const currentDate = new Date();
  const timeDifference = currentDate.getTime() - birthDate.getTime();
  const ageInYears = Math.floor(
    timeDifference / (1000 * 60 * 60 * 24 * 365.25)
  );
  return ageInYears;
};

export async function updateFitnessProfile(profile, goal) {
  const formData = new FormData();
  formData.append("goal", goal);
  formData.append("activityLevel", profile.activityLevel); // Assuming profile includes activityLevel

  try {
    const response = await axios.post(
      `${BASE_URL}/profiles/fitness-profile/`,
      formData
    );
    return response.data; // Return updated fitness profile data
  } catch (error) {
    console.error("Error updating fitness profile:", error);
    throw error; // Propagate the error for handling in the calling code
  }
}
