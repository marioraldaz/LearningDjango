import React, { useState, useEffect } from "react";
import axios from "axios";
import { Loading } from "../variety/loading";
export const Daily = ({ profileId }) => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await axios.get(
          `http:///daily-nutritional-stats/${profileId}/`
        );
        setStats(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching daily nutritional stats:", error);
        setLoading(false);
      }
    };

    fetchStats();
  }, [profileId]);

  if (loading) {
    return <Loading />;
  }

  if (!stats) {
    return <div>No data available</div>;
  }

  return (
    <div>
      <h2>Daily Nutritional Stats</h2>
      <p>Date: {stats.date}</p>
      <p>Total Calories Consumed: {stats.total_calories_consumed}</p>
      <p>Total Protein Consumed: {stats.total_protein_consumed}</p>
      <p>Total Fat Consumed: {stats.total_fat_consumed}</p>
      <p>Total Carbohydrates Consumed: {stats.total_carbohydrates_consumed}</p>
    </div>
  );
};
