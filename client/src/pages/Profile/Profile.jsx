import React, { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";

export function Profile() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);
  const context = useContext(AuthContext);
  
  useEffect(() => {
    setProfile(context.user);
  }, [context.user]);

  return (
    <div>
      {/* Your profile content here */}
    </div>
  );
}
