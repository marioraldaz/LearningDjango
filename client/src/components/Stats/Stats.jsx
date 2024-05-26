import React, { useState, useEffect, useContext } from "react";
import { BarChartCustom } from "./BarChart";
import { PieChart } from "./PieChart";
import { RadarChartCustom } from "./RadarChart";
import { AreaChart } from "./AreaChart";
import { fetchUserDailies } from "../../api/food_intake.api";
import AuthContext from "../../context/AuthContext";
import axios from "axios";

export function Stats({ profile }) {
  const [data, setData] = useState([]);
  useEffect(() => {});
  fetchUserDailies(profile.id);
  const { user } = useContext(AuthContext);

  useEffect(() => {
    const fetchData = async () => {
      console.log("Fetching");
      const response = axios
        .get(`http://localhost:8000/api/nutrition-stats/${profile.id}`)
        .then((response) => {
          setData(response.data);
        })
        .catch((error) => {
          //
          console.error("Error fetching nutrition stats:", error);
        });
    };
    fetchData();
  }, []);

  return (
    <>
      <BarChartCustom data={data} displayType={"weekly"} />
    </>
  );
}
