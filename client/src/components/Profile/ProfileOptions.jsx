import React, {useContext, useState} from 'react'
import {AuthContext} from "../../context/AuthContext";
import  { PhysicalInfoForm} from "./PhysicalInfoForm";
import { GrayButton } from '../buttons/GrayButton';
import { NavigationButton } from '../buttons/NavigationButton';

export function ProfileOptions() {
    const context = useContext(AuthContext);
    const [openPhysicalForm, setOpenPhysicalForm] = useState(false);

    const toggleOpenPhysicalForm = () => {
        setOpenPhysicalForm(!openPhysicalForm);
    }
    console.log(context);
  return (
    <div className="flex span-cols-2 p-4 gap-4 mt-4 ">
      <div className="w-1/2 flex flex-col gap-2 border p-2 rounded-lg">
        <span className="text-center  gradient-text bg-white">Complete Your Profile For A More Detailed Control</span>
        <GrayButton onClick={toggleOpenPhysicalForm}>Complete Or Change My Profile</GrayButton>
      </div>
    
      <div className="w-1/2 flex flex-col gap-2 border p-2 rounded-lg">
        <h1 className="text-center  gradient-text bg-white">Add Today`s Meal</h1>
        <NavigationButton link={"/Recipes"} text={"Search For A Delicious And Nutritive Recipe"}/>
        <NavigationButton link={"/Recipes/AddARecipe"} text={"Save Your Own Amazing Recipe"}/>
      </div>
      {openPhysicalForm && <PhysicalInfoForm/>}
    </div>
  )
}

