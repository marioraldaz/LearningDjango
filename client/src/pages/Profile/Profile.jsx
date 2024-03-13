import React, { useContext, useEffect, useState, require } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { NavigationButton } from "../../components/buttons/NavigationButton";
import { ProfileOptions } from "../../components/Profile/ProfileOptions";
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
    console.log(myCalorieNeeds);
  }, [context.user]);

  const handleSubmit = (e) => {
    e.preventDefault();
    logoutUser();
  };

  return (
    <div className="p-4">
      <ProfileOptions profile={profile} />
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
