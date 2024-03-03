import React from "react";
import {filters} from "../../config/recipeFiltersConfig.js";
import { Searchbar } from "/src/components/Search/Searchbar";

export function Recipes() {
  return  <div className="mt-5 flex flex-col items-center">
  <h1 className="gradient-text-green text-center w-full mb-10">
    Search Awesome And Balanced Recipes
  </h1>
  <div className="w-full flex">
    <Searchbar filters={filters} />
  </div>
</div>;
}
