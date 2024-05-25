import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { nutritionParams } from "../../data/nutritionParams.json";
import { GrayButton } from "../Buttons/GrayButton";
import { useSelector, useDispatch } from "react-redux";

export const NutritionForm = (id) => {
  const [selectedKey, setSelectedKey] = useState(null);
  const paramsInit = nutritionParams;
  const [params, setParams] = useState(paramsInit);
  const { updateNutrition } = useContext(AuthContext);
  const persistRecipes = useSelector((state) => state.recipes.recipes);
  console.log(persistRecipes);
  const dispatch = useDispatch();

  const handleChangeKey = (key) => {
    setSelectedKey(key);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    updateNutrition(id.id, params);
  };

  function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }
  return (
    <div className="p-4 gap-4 w-full h-[400px]">
      <div className="w-full h-full flex flex-col">
        <div className="flex flex-wrap gap-4 text-lg mb-2 w-full">
          {Object.keys(params).map((key) => (
            <div className="w-min h-min">
              <GrayButton key={key} onClick={() => handleChangeKey(key)}>
                {key}
              </GrayButton>
            </div>
          ))}
          {selectedKey && (
            <form
              onSubmit={handleSubmit}
              className=" flex flex-wrap w-50 h-min"
            >
              <button
                type="submit"
                className="bg-neutral-600 text-green-500 flex items-center justify center p-2 border rounded-md hover:scale-110 "
              >
                Update Nutrition
              </button>
            </form>
          )}
        </div>
        <div className="flex gap-4 flex-wrap h-full w-fit overflow-y-scroll">
          {selectedKey &&
            params[selectedKey].map((paramObject, index) => (
              <div
                className="flex flex-col p-2 gap-2 border border-black rounded-lg  bg-green-700"
                key={index}
              >
                <h4 className="w-full font-bold mb-2">{paramObject.name}</h4>
                {Object.entries(paramObject).map(([attribute, value]) => (
                  <div key={attribute} className="flex items-center gap-2">
                    <label htmlFor={attribute}>{capitalize(attribute)}</label>
                    <input
                      type="text"
                      value={value}
                      name={attribute}
                      className="w-[50px] h-4 "
                      onChange={(e) => {
                        const updatedParams = [...params];
                        updatedParams[selectedKey][index][attribute] =
                          e.target.value;
                        setParams(updatedParams);
                      }}
                    />
                  </div>
                ))}
              </div>
            ))}
        </div>
      </div>
    </div>
  );
};
