import React, { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { ProfileOptions } from "../../components/Profile/ProfileOptions";
import { ProfileData } from "../../components/Profile/ProfileData";
import { SavedRecipes } from "../../components/Profile/SavedRecipes";
import { Stats } from "../../components/Stats/Stats";
import { Loading } from "../../components/variety/loading";
export function Profile() {
  const [profile, setProfile] = useState(null);
  const {
    user,
    savedRecipes,
    uploadProfilePicture,
    changePassword,
    logoutUser,
  } = useContext(AuthContext);

  useEffect(() => {
    setProfile(user);
  }, [user, profile]);

  if (!profile || !savedRecipes) {
    return <Loading />;
  }

  return (
    <div className="p-4 mt-4 xl:grid xl:grid-cols-2 flex flex-col gap-4">
      <div className="order-3 xl:order-1">
        <ProfileOptions profile={profile} />
      </div>
      <div className="col-span-1 order-1 xl:order-2">
        <ProfileData
          profile={profile}
          uploadProfilePicture={uploadProfilePicture}
          changePassword={changePassword}
          logout={logoutUser}
        />
      </div>
      <div className="col-span-1 p-4 border rounded-lg order-2">
        <SavedRecipes savedRecipes={savedRecipes} />
      </div>
      <div className="col-span-2 p-4 rounded-lg border-white border h-[800px} w-full order-4">
        <h1 className="w-full gradient-text text-center text-4xl mb-8 p-8">
          Stats
        </h1>
        <Stats profile={profile} />
      </div>
    </div>
  );
}
