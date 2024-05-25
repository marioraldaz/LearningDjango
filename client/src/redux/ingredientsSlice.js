import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  ingredients: [],
};

const ingredientsSlice = createSlice({
  name: "ingredients",
  initialState,
  reducers: {
    addIngredient(state, action) {
      state.ingredients.push(action.payload);
    },
    removeIngredient(state, action) {
      state.ingredients = state.ingredients.filter(
        (recipe) => recipe.id !== action.payload.id
      );
    },
  },
});

export const { addIngredient, removeIngredient } = ingredientsSlice.actions;
export default ingredientsSlice.reducer;
