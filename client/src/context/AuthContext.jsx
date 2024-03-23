import { createContext, useState, useEffect } from "react";
import jwtDecode from "jwt-decode";
import { useNavigate } from "react-router-dom";
import { getRecipeById } from "../api/recipes.api";
import { getCookie } from "../api/users.api";
import axios from "axios";
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
  const navigate = useNavigate();

  let loginUser = async (e) => {
    e.preventDefault();
    const formData = {
      username: e.target.username.value,
      password: e.target.password.value,
    };
    const response = await axios.post(
      "http://localhost:8000/user/login/",
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

  const getSavedRecipes = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/get-saved-recipes",
        { profile_id: user.id },
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
        const recipes = await Promise.all(
          recipesIds.map(async (recipe_id) => {
            const recipe = await getRecipeById(recipe_id);
            return recipe;
          })
        );
        setSavedRecipes(recipes);
        console.log(recipes);
      }
    } catch (error) {
      console.error("Error fetching saved recipes:", error);
    }
  };

  const unSaveRecipe = async (recipe_id) => {
    try {
      const formData = new FormData();
      formData.append("profile_id", user.id); // Assuming user.id is the profile ID
      formData.append("recipe_id", recipe_id);

      const response = await axios.post(
        "http://localhost:8000/api/unsave-recipe",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data", // Set content type for FormData
            "X-CSRFToken": csrftoken, // Assuming csrftoken is defined in your context
          },
          withCredentials: true, // Include credentials for CSRF protection
        }
      );

      if (response.data.success) {
        // Optionally, handle success message or update state
        console.log("Recipe unsaved successfully");
      } else {
        // Optionally, handle error message or update state
        console.error("Error unsaving recipe:", response.data.error);
      }
    } catch (error) {
      console.error("Error unsaving recipe:", error);
    }
  };

  useEffect(() => {
    const csrfGot = Cookies.get("csrftoken");
    setCsrfToken(csrfGot);
    const profileToken = Cookies.get("profileJWT");
    getProfileByToken(profileToken, csrfGot);
    if (user) {
      getSavedRecipes();
    }
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
  };

  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};
