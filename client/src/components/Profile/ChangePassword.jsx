import React, { useState, useEffect } from "react";
import { GrayButton } from "../Buttons/GrayButton";

export function ChangePassword({ closePwdForm }) {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    setError("");
    let newError = "";
    if (newPassword !== confirmPassword) {
      newError += " Passwords do not match. ";
    }
  }, [newPassword, confirmPassword]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const newUser = Object.fromEntries(formData.entries());
    try {
      const res = await changePassword(oldPassword, newPassword);
      if (res.status === 201) {
        setError(NULL);
      }
    } catch (error) {
      let errorsEntries = [];
      error.response
        ? (errorsEntries = Object.entries(error.response.data))
        : "";
      let errorMessage = "";
      errorsEntries.forEach((error) => {
        errorMessage += `${error[0]}: ${error[1]}\n`;
      });
      setError(errorMessage);
    }
  };
  return (
    <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-2/3 h-2/3 bg-neutral-800 flex flex-col items-center rounded-xl border">
      <div className="">
        <h2 className="text-3xl w-full text-center mt-8">Change Password</h2>
        <button
          onClick={() => closePwdForm()}
          class="absolute top-0 right-0 p-4 bg-red-800 rounded-lg m-1 cursor-pointer"
        >
          <img className="" src="../../../public/whiteX.svg" />
        </button>
        <div className=" mt-16 flex gap-4 ">
          <h3 className="text-2xl">Current Password:</h3>
          <input
            type="password"
            className="text-black text-center"
            placeholder="  Type Current Password Here"
            value={oldPassword}
            onChange={(e) => setOldPassword(e.target.value)}
          />
        </div>
        <div className=" flex gap-4 mt-12">
          <h3 className="text-2xl">New Password:</h3>
          <input
            type="password"
            className="text-black text-center"
            placeholder="   Type New Password Here"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
          />
        </div>
        <div className=" flex gap-4 mt-12">
          <h3 className="text-2xl">Repeat New Password:</h3>

          <input
            type="password"
            className="text-black text-center"
            placeholder="   Repeat New Password Here"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </div>
        <div className="">{error}</div>
        <div className="w-full flex flex-col mt-auto items-center justify-center p-8 ">
          <div className="h-16 w-[200px] rounded-lg border">
            <GrayButton onClick={handleSubmit}>Change Password</GrayButton>
          </div>
        </div>
      </div>
    </div>
  );
}
