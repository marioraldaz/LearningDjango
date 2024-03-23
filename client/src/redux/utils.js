import { useSelector, useDispatch } from "react-redux";
import { getIngredientById } from "../api/ingredients.api";
import { addIngredient } from "./ingredientsSlice";

export const getIngredient = async (id) => {
  const ingredients = useSelector((state) => state.ingredients.ingredients);
  const dispatch = useDispatch();
  const ingredientFound = ingredients.find((ingredientToFind) => {
    if (String(ingredientToFind.id) == String(id)) {
      return ingredientToFind;
    }
    return false;
  });
  if (ingredientFound === undefined && id) {
    const res = await getIngredientById(id, 1);
    const data = res.data;
    dispatch(addIngredient(data));
    return data;
  } else {
    return await getIngredientById(id);
  }
};
