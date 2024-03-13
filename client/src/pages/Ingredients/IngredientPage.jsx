import React, { useState, useEffect } from "react";
import { getIngredientById } from "../../api/ingredients.api";
import { useParams } from "react-router-dom";
import { GrayButton } from "../../components/buttons/GrayButton";
import { useSelector, useDispatch } from "react-redux";
import { addIngredient } from "../../redux/ingredientsSlice";

export function IngredientPage() {
  const { id } = useParams();
  const [ingredient, setIngredient] = useState(null);
  const ingredients = useSelector((state) => state.ingredients.ingredients);
  const dispatch = useDispatch();

  useEffect(() => {
    const fetchRecipe = async () => {
      const ingredientFound = ingredients.find((recipeToFind) => {
        if (String(recipeToFind.id) == String(id)) {
          return recipeToFind;
        }
        return false;
      });
      console.log(ingredientFound);
      if (ingredientFound === undefined && id) {
        const res = await getIngredientById(id);
        const data = res.data;
        setIngredient(data);
        dispatch(addIngredient(data));
      } else {
        setIngredient(ingredientFound);
      }
    };

    fetchRecipe();
  }, [id]);

  return <div></div>;
}
