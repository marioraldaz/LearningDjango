import React, { useState } from "react";
import { GrayButton } from "../buttons/GrayButton";

export function ChangePassword() {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const handleSubmit = () => {};

  return (
    <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-2/3 h-2/3 bg-neutral-800 flex flex-col items-center rounded-xl border">
      <h2 className="text-3xl w-full text-center mt-8">Change Password</h2>
      <div class="absolute top-0 right-0 p-4 ">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </div>
      <div className=" flex gap-4 mt-12">
        <h3 className="text-2xl">Current Password:</h3>
        <input
          type="password"
          placeholder="  Type Current Password Here"
          value={oldPassword}
          onChange={(e) => setOldPassword(e.target.value)}
        />
      </div>
      <div className=" flex gap-4 mt-12">
        <h3 className="text-2xl">New Password:</h3>
        <input
          type="password"
          placeholder="   Type New Password Here"
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
        />
      </div>
      <div className=" flex gap-4 mt-12">
        <h3 className="text-2xl">Repeat New Password:</h3>
        <input
          type="password"
          placeholder="   Repeat New Password Here"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
      </div>
      <div className="h-16 w-24 mt-auto mb-8">
        <GrayButton onClick={handleSubmit}>Change Password</GrayButton>
      </div>
    </div>
  );
}
