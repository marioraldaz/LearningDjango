import React, { useContext, useState, useEffect } from "react";
import { PhysicalInfoForm } from "./PhysicalInfoForm";
import { GrayButton } from "../buttons/GrayButton";
import { NavigationButton } from "../buttons/NavigationButton";

export function ProfileOptions({ profile }) {
  const [openPhysicalForm, setOpenPhysicalForm] = useState(false);

  const toggleOpenPhysicalForm = () => {
    setOpenPhysicalForm(!openPhysicalForm);
  };

  if (!profile) {
    return <h1>Loading....</h1>;
  }

  return (
    <div className="flex p-4 gap-4 mt-4 justify-center items-center ">
      <div className="w-1/2 flex flex-col gap-2 border p-2 rounded-lg">
        <span className="text-center  gradient-text bg-white">
          Complete Your Profile For A More Detailed Control
        </span>
        <div className="w-[300px]">
          <GrayButton onClick={toggleOpenPhysicalForm}>
            Complete Or Change My Profile
          </GrayButton>
        </div>
        {openPhysicalForm && <PhysicalInfoForm profile={profile} />}
      </div>

      <div className="w-1/2 flex flex-col gap-2 border p-2 rounded-lg">
        <h1 className="text-center  gradient-text bg-white">
          Add Today`s Meal
        </h1>
        <NavigationButton
          link={"/Recipes"}
          text={"Search For A Delicious And Nutritive Recipe"}
        />
        <NavigationButton
          link={"/Recipes/AddARecipe"}
          text={"Save Your Own Amazing Recipe"}
        />
      </div>
    </div>
  );
}
