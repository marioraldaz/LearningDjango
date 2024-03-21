import React, { useContext, useEffect, useState, require } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { NavigationButton } from "../../components/buttons/NavigationButton";
import { ProfileOptions } from "../../components/Profile/ProfileOptions";
import { ProfileData } from "../../components/Profile/ProfileData";
import fitnessCalculatorFunctions from "fitness-calculator";
export function Profile() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);
  const context = useContext(AuthContext);
  const logout = context.logoutUser;

  useEffect(() => {
    setProfile(context.user);
    console.log(context.user);
    const myCalorieNeeds = fitnessCalculatorFunctions.calorieNeeds(
      "male",
      22,
      176,
      73,
      "active"
    );
  }, [context.user, profile]);

  const handleSubmit = (e) => {
    e.preventDefault();
    logoutUser();
  };
  if (!profile) {
    return <h1>Loading....</h1>;
  }

  return (
    <div className="p-4 grid grid-cols-2 w-full">
      <div className="bg-red-200">
        <ProfileOptions profile={profile} />
      </div>
      <div className="col-span-1">
        <ProfileData profile={profile} />
      </div>
      <div className="w-[200px] p-4">
        <NavigationButton text={"Profile Details"} link={"/profile/details"} />
        <form onSubmit={logout} className="mt-4">
          <button type="submit" className="bg-neutral-800 p-2 rounded-lg">
            Log Out
          </button>
        </form>
      </div>
    </div>
  );
}
