import React from "react";
import { CardsList } from "../Lists/CardsList";
export function SavedRecipes({ savedRecipes }) {
  if (!savedRecipes) {
    return <h1>Loading...</h1>;
  }
  return (
    <>
      {console.log(savedRecipes)}
      {savedRecipes.length > 0 ? (
        <div>
          <h1 className="text-2xl gradient-text w-full text-center mb-8">
            Saved Recipes
          </h1>
          <div className="flex flex-row h-[400px] overflow-x-scroll overflow-y-hidden">
            <CardsList products={savedRecipes} />
          </div>
        </div>
      ) : (
        <h3 className="text-2xl gradient-text mt-2">
          Your Saved Recipes Will Appear Here
        </h3>
      )}
    </>
  );
}
