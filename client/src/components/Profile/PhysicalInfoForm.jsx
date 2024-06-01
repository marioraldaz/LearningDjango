import React, { useState } from "react";
import { GrayButton } from "../Buttons/GrayButton";
export const PhysicalInfoForm = ({ profile }) => {
  const [age, setAge] = useState(profile.age);
  const [height, setHeight] = useState(profile.height);
  const [heightUnit, setHeightUnit] = useState("cm");
  const [weight, setWeight] = useState(profile.weight);
  const [weightUnit, setWeightUnit] = useState("kg");
  const [activityLevel, setActivityLevel] = useState(profile.activityLevel);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted:", { age, height, weight, activityLevel });
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="2xl:grid 2xl:grid-cols-2 flex flex-col gap-4 bg-neutral-900 w-full rounded-lg mt-12 p-8 h-[350px] text-xl"
    >
      <div className="w-full h-min flex gap-2">
        <label>Age:</label>
        <input
          type="number"
          className="text-black text-center w-min"
          placeholder="Age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          required
        />
      </div>
      <div className="w-full flex gap-2 h-min">
        <label>Height:</label>
        <input
          type="number"
          className="text-black text-center w-min"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
          required
        />
        <select
          value={heightUnit}
          className="text-black"
          onChange={(e) => setHeightUnit(e.target.value)}
        >
          <option value="cm">cm</option>
          <option value="feet">feet</option>
        </select>
      </div>
      <div className="w-full flex gap-2 h-min ">
        <label>Weight:</label>
        <input
          type="number"
          className="text-black w-min text-center"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          required
        />
        <select
          value={weightUnit}
          className="text-black"
          onChange={(e) => setWeightUnit(e.target.value)}
        >
          <option value="kg">kg</option>
          <option value="lb">lb</option>
        </select>
      </div>
      <div className="w-full flex gap-2 h-min ">
        <label>Physical Activity Level:</label>
        <select
          value={activityLevel}
          onChange={(e) => setActivityLevel(e.target.value)}
          className="text-black"
          required
        >
          <option value="">Select...</option>
          <option value="sedentary">Sedentary</option>
          <option value="lightly_active">Lightly Active</option>
          <option value="moderately_active">Moderately Active</option>
          <option value="very_active">Very Active</option>
          <option value="super_active">Super Active</option>
        </select>
      </div>
      <div className="w-3/4 mx-auto flex col-span-2 h-20 mt-auto">
        <GrayButton onClick="submit">Submit</GrayButton>
      </div>
    </form>
  );
};
