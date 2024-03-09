import React, { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";

export function Profile() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState("Not Loaded");
  const context = useContext(AuthContext);

  useEffect(() => {
    // Update the profile state with the user from the context
    setProfile(context.user);

    console.log(profile)
    if (profile) {
      navigate("/profile");
    }
  }, [context.user, navigate, profile]);

  return (
    <div>
      {/* Your profile content here */}
    </div>
  );
}
