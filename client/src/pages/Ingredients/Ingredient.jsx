import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { getIngredientInfo } from "../../api/ingredients.api";

export function Ingredient() {
  const location = useLocation();
  const [info, setInfo] = useState(null); // Initialize info as null
  const [loading, setLoading] = useState(true); // Initialize loading state

  const searchParams = new URLSearchParams(location.search);
  const id = searchParams.get("id");

  useEffect(() => {
    async function getInfo() {
      try {
        const ingredient = await getIngredientInfo(id);
        setInfo(ingredient);
        setLoading(false); // Set loading to false after API call is done
        console.log(ingredient);
      } catch (error) {
        // Handle errors
        console.error("Error fetching ingredient info:", error);
      }
    }

    getInfo();
  }, [id]); // Run useEffect when id changes

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {/* Render ingredient info */}
      {info && (
        <div>
          <h2>{info.name}</h2>
          <p>{info.description}</p>
          {/* Render other info as needed */}
        </div>
      )}
    </div>
  );
}
