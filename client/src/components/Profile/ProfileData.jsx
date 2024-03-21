import React from "react";

export function ProfileData({ profile }) {
  if (!profile) {
    return <h1>Loading....</h1>;
  }
  console.log(Object.entries(profile));
  return (
    <div className="flex flex-wrap w-full p-4 rounded-xl bg-neutral-800">
      <div className="w-full">
        <h3 className="text-2xl">{profile.username}</h3>
      </div>
    </div>
  );
}
