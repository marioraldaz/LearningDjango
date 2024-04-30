import React, { useContext, useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { useSelector, useDispatch } from "react-redux";
export function IngredientPage() {
  const { id } = useParams();
  const [ingredient, setIngredient] = useState(null);
  const [amount, setAmount] = useState(1);
  const { getIngredient } = useContext(AuthContext);
  const ingredients = useSelector((state) => state.ingredients.ingredients);
  const dispatch = useDispatch();

  useEffect(() => {
    const fetchIngredient = async () => {
      const searched = await getIngredient(id, ingredients, dispatch);
      setIngredient(searched);
    };
    fetchIngredient();
  }, []);

  const handleAmountChange = (e) => {
    setAmount(parseInt(e.target.value, 10));
  };

  if (!ingredient) {
    return <div>Loading...</div>;
  }
  return (
    <div className="flex flex-wrap p-8 items-center justify-center xl:items-start xl:justify-start">
      <h3 className="w-full gradient-text text-center text-3xl capitalize  mb-20">
        {ingredient.name}
      </h3>
      <img
        className="rounded-lg border mr-8 mb-8"
        src={`https://spoonacular.com/cdn/ingredients_500x500/${ingredient.image}`}
      />
      <div className="flex flex-col flex-grow justify-center items-center text-center self-center">
        <div className="flex text-2xl mb-4 justify-center items-center text-center">
          <span className="mr-2 ">Amount Of {ingredient.name} To Compute:</span>
          <input
            type="number"
            name="amount"
            min="1"
            className="w-[50px] bg-black"
            value={amount}
            onChange={handleAmountChange}
          />
        </div>

        <h3 className="text-2xl capitalize mt-[80px]">
          Price (For {ingredient.amount} {ingredient.name}):{"  "}
          {ingredient.estimatedCost?.value * amount}{" "}
          {ingredient.estimatedCost?.unit}
        </h3>
        <h3 className="text-2xl capitalize mt-[80px]">
          Nutrients (For {amount} {ingredient.name}):
        </h3>
        <ul className="overflow-y-scroll h-[300px] mt-[40px] w-full flex flex-col">
          {ingredient.nutrition?.nutrients?.map((nutrient) => (
            <ul
              key={nutrient.name}
              className="flex flex-row gap-4 w-full border p-4 odd:bg-rgb-rgb(0, 0, 0) even:bg-yellow-500 even:text-black"
            >
              <li className="w-1/2">
                <div>
                  {`${nutrient.name}  Amount: ${(
                    nutrient.amount * amount
                  ).toFixed(2)}`}
                </div>
                {nutrient.unit}
              </li>

              <li>
                Percentage Of Daily Needs:{" "}
                {(nutrient.percentOfDailyNeeds * amount).toFixed(2)} {"%"}
              </li>
            </ul>
          ))}
        </ul>
      </div>
    </div>
  );
}
