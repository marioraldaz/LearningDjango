import React, { useState } from "react";
import { uploadProfilePicture } from "../../api/users.api";
import axios from "axios";
export function ProfileData({ profile, uploadProfilePicture }) {
  const [file, setFile] = useState(null);

  if (!profile) {
    return <h1>Loading....</h1>;
  }
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
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
      <div className="w-full">
        <h3 className="text-2xl">{profile.username}</h3>
      </div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}
