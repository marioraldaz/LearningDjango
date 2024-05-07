// foodIntakeSlice.js

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  recipes: [], // Array to hold saved recipes
};

const foodIntakeSlice = createSlice({
  name: "foodIntake",
  initialState,
  reducers: {
    addRecipe(state, action) {
      // Add a new recipe to the recipes array
      state.recipes.push(action.payload);
    },
    removeRecipe(state, action) {
      // Remove a recipe from the recipes array based on its index
      state.recipes.splice(action.payload, 1);
    },
    clearRecipes(state) {
      // Clear all saved recipes
      state.recipes = [];
    },
  },
});

export const {
  addRecipe,
  removeRecipe,
  clearRecipes,
} = foodIntakeSlice.actions;

export default foodIntakeSlice.reducer;
