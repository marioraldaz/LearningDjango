import React, { useContext, useState, useEffect } from "react";
import { PhysicalInfoForm } from "./PhysicalInfoForm";
import { GrayButton } from "../Buttons/GrayButton";
import { NavigationButton } from "../Buttons/NavigationButton";

export function ProfileOptions({ profile }) {
  const [openPhysicalForm, setOpenPhysicalForm] = useState(false);

  const toggleOpenPhysicalForm = () => {
    setOpenPhysicalForm(!openPhysicalForm);
  };

  if (!profile) {
    return <h1>Loading....</h1>;
  }

  return (
    <div className="flex flex-col gap-4 w-full">
      <div className="flex flex-col gap-2 border p-2 rounded-lg bg-neutral-900">
        <span className="text-center  gradient-text bg-white">
          Complete Your Profile For A More Detailed Control
        </span>
        {!openPhysicalForm && (
          <div className="w-[400px] self-center mt-8">
            <GrayButton onClick={toggleOpenPhysicalForm}>
              Complete Or Change My Profile
            </GrayButton>
          </div>
        )}
        {openPhysicalForm && <PhysicalInfoForm profile={profile} />}
      </div>

      <div className="flex flex-col gap-2 border p-2 rounded-lg  bg-neutral-900">
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
