import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  recipes: [],
};

const recipesSlice = createSlice({
  name: 'recipes',
  initialState,
  reducers: {
    addRecipe(state, action) {
      state.recipes.push(action.payload);
    },
    removeRecipe(state, action) {
      state.recipes = state.recipes.filter(recipe => recipe.id !== action.payload.id);
    },
  },
});

export const { addRecipe, removeRecipe } = recipesSlice.actions;
export default recipesSlice.reducer;