import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { getIngredientInfo } from "../../api/ingredients.api";

export function Ingredient() {
  const location = useLocation();
  const [info, setInfo] = useState([]);

  // Parse the query string to get the 'id' parameter
  const searchParams = new URLSearchParams(location.search);
  const id = searchParams.get("id");

  useEffect(() => {
    async function getInfo() {
      const ingredient = await getIngredientInfo(id);
      setInfo(ingredient);
      console.log(ingredient);
    }
    getInfo();
  });

  return <div>id:{id}</div>;
}
