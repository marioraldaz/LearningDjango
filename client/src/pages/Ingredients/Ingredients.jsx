import React from "react";
import { Searchbar } from "/src/components/Search/Searchbar";
import { filters } from "../../config/filtersConfig.js";
import { fetchFilteredIngredients, fetchIngredientsByName } from "../../api/ingredients.api";

export function Ingredients() {
  return (
    <div className="mt-5 flex flex-col items-center">
      <h1 className="gradient-text-green text-center w-full mb-10">
        Search Delicious And Nutritive Ingredients
      </h1>
      <div className="w-full flex">
        <Searchbar filters={filters} complexFetch={fetchFilteredIngredients} fetchByName={fetchIngredientsByName}/>
      </div>
    </div>
  );
}
