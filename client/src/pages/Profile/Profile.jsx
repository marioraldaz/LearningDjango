import React, { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { NavigationButton } from "../../components/buttons/NavigationButton";
export function Profile() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);
  const context = useContext(AuthContext);
  const logout = context.logoutUser;


  useEffect(() => {
    setProfile(context.user);
    console.log(context.user);
  }, [context.user]);
  

  const handleSubmit = (e) => {
    e.preventDefault();
     logoutUser();

  };

  return (
    <div className="text-2xl p-4 grid grid-cols-4 gap-4">
        <div className="w-[200px]">
          <NavigationButton text={"Profile Details"} link={"/profile/details"}/>
        </div>
      <form onSubmit={logout} className="col-span-4">
        <button type="submit" className="bg-neutral-800 p-2 rounded-lg">Log Out</button>
      </form>
    </div>
  );
}

