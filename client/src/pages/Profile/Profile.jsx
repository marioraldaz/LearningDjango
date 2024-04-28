import React, { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { ProfileOptions } from "../../components/Profile/ProfileOptions";
import { ProfileData } from "../../components/Profile/ProfileData";
import { SavedRecipes } from "../../components/Profile/SavedRecipes";
import { Stats } from "../../components/Stats/Stats";

export function Profile() {
  const [profile, setProfile] = useState(null);
  const context = useContext(AuthContext);

  useEffect(() => {
    setProfile(context.user);
  }, [context.user, profile]);

  if (!profile || !context.savedRecipes) {
    return <h1>Loading....</h1>;
  }

  return (
    <div className="p-4 mt-4 grid grid-cols-2 gap-4">
      <div className="">
        <ProfileOptions profile={profile} />
      </div>
      <div className="col-span-1">
        <ProfileData
          profile={profile}
          uploadProfilePicture={context.uploadProfilePicture}
          changePassword={context.changePassword}
        />
      </div>
      <div className="col-span-1 p-4 border rounded-lg">
        <SavedRecipes savedRecipes={context.savedRecipes} />
      </div>
      <div className="col-span-2 bg-neutral-600 h-[800px} w-full">
        <Stats />
      </div>
    </div>
  );
}
