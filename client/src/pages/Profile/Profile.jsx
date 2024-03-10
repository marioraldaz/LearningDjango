import React, { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";

export function Profile() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);
  const context = useContext(AuthContext);
 //const logout = context.logoutUser();


  useEffect(() => {
    setProfile(context.user);
  }, [context.user]);
  

  const handleSubmit = () => {
   // logoutUser();
  };

  return (
    <div>
      <form method="post" onSubmit={handleSubmit}>
        <button type="submit">Log Out</button>

      </form>
    </div>
  );
}

