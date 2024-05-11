import React from "react";
import { CardsList } from "../../components/Lists/CardsList.jsx";

export function RecipeBalance({ meal, intake }) {
  console.log(intake);
  return (
    <>
      <div className="w-min">
        <CardsList products={[meal]} />
      </div>
      <div>a</div>
    </>
  );
}
