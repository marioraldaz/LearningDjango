import React, { useState } from "react";
import { GrayButton } from "../buttons/GrayButton";
import {
  getActivityLevelByNumber,
  cmToMeters,
  calculateAge,
} from "../../api/fitCalcu.api";
import { ChangePassword } from "./ChangePassword";
export function ProfileData({ profile, uploadProfilePicture }) {
  const [file, setFile] = useState(null);
  const [showChangeProfileForm, setShowChangeProfileForm] = useState(false);
  const [changePassword, setChangePassword] = useState(false);

  if (!profile) {
    return <h1>Loading....</h1>;
  }
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const closePwdForm = () => {
    setChangePassword(false);
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("profile_picture", file);
    formData.append("profile_id", profile.id);
    for (var pair of formData.entries()) {
      console.log(pair[0] + ", " + pair[1]);
    }
    uploadProfilePicture(formData);
  };

  return (
    <div className="grid grid-cols-2 w-full p-4 rounded-xl bg-neutral-800">
      <div className="col-span-1 flex flex-col gap-4">
        <h3 className="text-2xl">{profile.username}</h3>
        <h3 className="text-xl">
          Lifestyle: {getActivityLevelByNumber(profile.activityLevel)}
        </h3>
        <h3 className="text-xl">Height: {cmToMeters(profile.height)} m</h3>
        <h3 className="text-xl">Weight: {profile.height} Kg</h3>
        <h3 className="text-xl">Gender: {profile.gender}</h3>
        <h3 className="text-xl">Age: {calculateAge(profile.date_of_birth)}</h3>
        <h3 className="text-xl">Email: {profile.email}</h3>
      </div>
      <div className="">
        <img
          className=""
          src={
            profile.profile_picture
              ? `http://localhost:8000${profile.profile_picture}`
              : "../../../public/default_profile.jpg"
          }
        />
      </div>
      <div className="col-span-1">
        <div className="h-16 m-2">
          <GrayButton onClick={() => setChangePassword(true)}>
            Change Password
          </GrayButton>
        </div>
        {changePassword && <ChangePassword closePwdForm={closePwdForm} />}
      </div>
      <div className="col-span-1">
        <div className="h-16 m-2">
          <GrayButton
            onClick={() => setShowChangeProfileForm(!showChangeProfileForm)}
          >
            Change Profile Picture:{" "}
          </GrayButton>
        </div>
        {showChangeProfileForm && (
          <form onSubmit={handleSubmit} className="m-2 gap-2 p-4">
            <>
              <input type="file" onChange={handleFileChange} />
              <button type="submit">Upload</button>
            </>
          </form>
        )}
      </div>
    </div>
  );
}
