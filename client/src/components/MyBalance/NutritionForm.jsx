import React, { useState } from "react";
import { nutritionParams } from "../../data/nutritionParams.json";
export const NutritionForm = () => {
  const [selectedKey, setSelectedKey] = useState(null);
  const paramsInit = nutritionParams;
  const [params, setParams] = useState(paramsInit);

  const handleChangeKey = (key) => {
    setSelectedKey(key);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setSelectedNutrient(null);
    setAmount("");
  };
  function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }
  return (
    <div className="p-4 flex gap-4 w-full">
      <div className="w-full h-1/5 flex flex-col">
        <div className="flex gap-4 text-lg">
          {Object.keys(params).map((key) => (
            <button key={key} onClick={() => handleChangeKey(key)}>
              {key}
            </button>
          ))}
          {selectedKey && (
            <form
              onSubmit={handleSubmit}
              className="w-full h-full flex flex-wrap"
            >
              <button type="submit">Update Nutrition</button>
            </form>
          )}
        </div>
        <div className="flex gap-4 flex-wrap h-[300px] w-fulloverflow-scroll">
          {selectedKey &&
            params[selectedKey].map((paramObject, index) => (
              <div
                className="flex flex-col gap-2 p-1 border border-black rounded-lg  bg-green-700"
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
