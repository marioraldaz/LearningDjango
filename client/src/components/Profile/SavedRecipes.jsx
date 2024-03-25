import React from "react";

export function SavedRecipes() {
  if (true) {
    return <></>;
  }
  return (
    <div>
      {context.savedRecipes.length > 0 ? (
        <div className="flex flex-row overflow-x-scroll">
          <CardsList products={context.savedRecipes} />
        </div>
      ) : (
        <h3 className="text-2xl gradient-text mt-2">
          Your Saved Recipes Will Appear Here
        </h3>
      )}
    </div>
  );
}
