import { createContext, useState, useEffect } from "react";
import jwtDecode from "jwt-decode";
import { useNavigate } from "react-router-dom";
import { getRecipeById } from "../api/recipes.api";
import { getIngredientById } from "../api/ingredients.api";
import { addIngredient } from "../redux/ingredientsSlice";
import { addRecipe } from "../redux/recipesSlice";
import { useSelector, useDispatch } from "react-redux";

import axios, { AxiosError } from "axios";
import Cookies from "js-cookie";

export const AuthContext = createContext();
export default AuthContext;

export const AuthProvider = ({ children }) => {
  let [user, setUser] = useState(() =>
    !localStorage.getItem("authTokens") ==
    '{"detail":"No active account found with the given credentials"}'
      ? jwtDecode(localStorage.getItem("authTokens"))
      : null
  );
  let [authTokens, setAuthTokens] = useState(null);
  let [loading, setLoading] = useState(true);
  let [csrftoken, setCsrfToken] = useState(null);
  let [savedRecipes, setSavedRecipes] = useState([]);
  const [currentRecipe, setCurrentRecipe] = useState(null);
  const [recipesForDaily, setRecipesForDaily] = useState([]);
  const [ingredientsForDaily, setIngredientsForDaily] = useState([]);

  const navigate = useNavigate();

  ////////////////////////////////////////////////////////////////////////   PROFILE FUNCTIONS         ////////////////////////////////

  async function register(user) {
    try {
      const { username, password, gender, date_of_birth, email } = user;
      console.log(user);
      const formData = {
        username: username,
        password: password,
        gender: gender,
        date_of_birth: date_of_birth,
        email,
      };
      const response = await axios.post(
        "http://localhost:8000/api/register/",
        formData,
        {
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },
          withCredentials: true,
        }
      );
    } catch (e) {
      console.log(e);
    }
  }
  let loginUser = async (e) => {
    e.preventDefault();
    const formData = {
      username: e.target.username.value,
      password: e.target.password.value,
    };
    const response = await axios.post(
      "http://localhost:8000/api/login/",
      formData,
      {
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        withCredentials: true,
      }
    );
    if (response.data.success) {
      const token = response.data.token;
      const refreshToken = response.data.refresh_token;
      setAuthTokens(token);
      setUser(response.data.user);
      Cookies.set("profileJWT", token, { secure: true, sameSite: "strict" });
      Cookies.set("refreshToken", refreshToken, {
        secure: true,
        sameSite: "strict",
      });
    } else {
      return response.data.error;
    }
  };

  let logoutUser = () => {
    console.log("logged out");
    Cookies.set("profileJWT", null);
    Cookies.set("profileRefreshToken", null);
    setAuthTokens(null);
    setUser(null);
    navigate("/login");
  };

  const updateToken = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/token/refresh/",
        {
          refresh: authTokens.refresh,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const data = response.data;

      if (response.status === 200) {
        setAuthTokens(data);
        setUser(jwtDecode(data.access));
        localStorage.setItem("authTokens", JSON.stringify(data));
      } else {
        // logoutUser();
      }

      if (loading) {
        setLoading(false);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const getProfileByToken = async (token, csrfToken) => {
    const response = await axios.post(
      "http://localhost:8000/api/get_profile/",
      { token: token },
      {
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );
    if (response.data.success) {
      setAuthTokens(token);
      setUser(response.data.user);
      return response.data.user;
    } else {
      return response.data.error;
    }
  };

  const uploadProfilePicture = async (formData) => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/upload-profile-picture/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFToken": csrftoken,
          },
          withCredentials: true,
        }
      );
    } catch (error) {
      console.error("Error uploading profile picture:", error);
    }
  };

  const changePassword = async (formData) => {
    const response = await axios.post(
      "http://localhost:8000/api/change-password/",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          "X-CSRFToken": csrftoken,
        },
        withCredentials: true,
      }
    );
  };

  ////////////////////////////////////////////////////////////////////////////////////////// RECIPES AND INGREDIENTS FUNCTIONS////////////////////////////////

  const saveRecipe = async (recipe_id) => {
    const formData = new FormData();
    formData.append("profile_id", user.id);
    formData.append("recipe_id", recipe_id);
    const res = await axios.post(
      "http://localhost:8000/api/save-recipe",
      formData,
      {
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        withCredentials: true,
      }
    );
  };

  const getSavedRecipes = async (id, csrftoken, recipes, dispatch) => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/get-saved-recipes",
        { profile_id: id },
        {
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },
          withCredentials: true,
        }
      );
      if (response.data.saved_recipes) {
        const recipesIds = response.data.saved_recipes;
        const foundRecipes = await Promise.all(
          recipesIds.map(async (recipe_id) => {
            const recipe = getRecipe(recipe_id, recipes, dispatch);
            return recipe;
          })
        );
        setSavedRecipes(foundRecipes);
      }
    } catch (error) {
      console.error("Error fetching saved recipes:", error);
    }
  };

  const unSaveRecipe = async (recipe_id) => {
    try {
      const formData = new FormData();
      formData.append("profile_id", user.id);
      formData.append("recipe_id", recipe_id);

      const response = await axios.post(
        "http://localhost:8000/api/unsave-recipe",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFToken": csrftoken,
          },
          withCredentials: true,
        }
      );

      if (response.data.success) {
        console.log("Recipe unsaved successfully");
      } else {
        console.error("Error unsaving recipe:", response.data.error);
      }
    } catch (error) {
      console.error("Error unsaving recipe:", error);
    }
  };

  const fetchData = async (id, dataArray, getDataById, dispatch, addData) => {
    const dataFound = dataArray.find(
      (dataToFind) => String(dataToFind?.id) === String(id)
    );
    if (dataFound === undefined && id) {
      const res = await getDataById(id, 1);
      const data = res;
      dispatch(await addData(data));
      return data;
    } else {
      return dataFound;
    }
  };

  const getRecipe = async (id, recipes, dispatch) => {
    return await fetchData(id, recipes, getRecipeById, dispatch, addRecipe);
  };

  const getIngredient = async (id, ingredients, dispatch) => {
    return await fetchData(
      id,
      ingredients,
      getIngredientById,
      dispatch,
      addIngredient
    );
  };

  //////////////////////////////////////////////////////////////////////////// FOOD INTAKE FUNCTIONS //////////////////////////////////////////////////////////////////////////

  const addFoodIntake = async (mealType, details) => {
    // Create a new FormData object
    const formData = new FormData();

    // Append simple fields to FormData
    formData.append("profile_id", user.id);
    formData.append("meal_type", mealType);
    formData.append("date", "2024-05-07"); // Example date
    console.log(formData);

    // Append details array to FormData
    details.forEach((detail, index) => {
      formData.append(`details[${index}]`, JSON.stringify(detail));
    });
    const response = await axios.post(
      `http://localhost:8000/api/food-intake/`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          "X-CSRFToken": csrftoken,
        },
        withCredentials: true,
      }
    );
    console.log(response.data);
    return response.data;
  };

  const getDayIntakes = async () => {
    const response = await axios.post(
      `http://localhost:8000/api/food-intake/${user.id}`,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          "X-CSRFToken": csrftoken,
        },
        withCredentials: true,
      }
    );
    console.log(response.data);
    return response.data;
  };

  //////////////////////////////////////////////////////////////// useEffects //////////////////////////////////////////////////

  const recipes = useSelector((state) => state.recipes.recipes);
  const dispatch = useDispatch();
  useEffect(() => {
    console.log("triggered", savedRecipes);
    const fetchData = async () => {
      const csrfGot = Cookies.get("csrftoken");
      setCsrfToken(csrfGot);
      const profileToken = Cookies.get("profileJWT");
      const profile = await getProfileByToken(profileToken, csrfGot);
      setUser(profile);
      if (profile) {
        return await getSavedRecipes(profile.id, csrfGot, recipes, dispatch);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    const csrfGot = Cookies.get("csrftoken");
    setCsrfToken(csrfGot);
    const profileToken = Cookies.get("profileJWT");
    getProfileByToken(profileToken, csrfGot);

    const REFRESH_INTERVAL = 1000 * 60 * 4;
    let interval = setInterval(() => {
      if (authTokens) {
        //updateToken();
      }
    }, REFRESH_INTERVAL);

    return () => clearInterval(interval);
  }, [user?.id]);

  let contextData = {
    user: user,
    authTokens: authTokens,
    savedRecipes: savedRecipes,
    loginUser: loginUser,
    logoutUser: logoutUser,
    uploadProfilePicture: uploadProfilePicture,
    saveRecipe: saveRecipe,
    unSaveRecipe: unSaveRecipe,
    getSavedRecipes: getSavedRecipes,
    getIngredient: getIngredient,
    changePassword: changePassword,
    setSavedRecipes: setSavedRecipes,
    addFoodIntake: addFoodIntake,
    getDayIntakes: getDayIntakes,
    getRecipe: getRecipe,
    ingredientsForDaily: ingredientsForDaily,
    recipesForDaily: recipesForDaily,
    setIngredientsForDaily: setIngredientsForDaily,
    setRecipesForDaily: setRecipesForDaily,
    currentRecipe: currentRecipe,
    setCurrentRecipe: setCurrentRecipe,
    register: register,
  };
  useEffect(() => {}, [setCurrentRecipe, currentRecipe]);
  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};
