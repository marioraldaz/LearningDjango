import React, { useState, useEffect, useContext } from "react";
import { BarChartCustom } from "./BarChartCustom";
import { PieChart } from "./PieChart";
import { RadarChartCustom } from "./RadarChart";
import { AreaChart } from "./AreaChart";
import { fetchUserDailies } from "../../api/food_intake.api";
import AuthContext from "../../context/AuthContext";
import axios from "axios";
import { GrayButton } from "../Buttons/GrayButton";

export function Stats({ profile }) {
  const { user } = useContext(AuthContext);
  const [selected, setSelected] = useState("Protein");
  const [userDailies, setUserDailies] = useState([]);
  const [params, setParams] = useState([]);
  const [range, setRange] = useState("Weekly");
  const choices = ["Protein", "Fat", "Carbohydrates"];

  if (!profile) {
    return <h1>Loading</h1>;
  }
  useEffect(() => {
    const newData =
      range === "Weekly" ? userDailies?.last_week : userDailies?.last_month;
    console.log(newData);
    const newParams =
      newData?.map((intake) => {
        switch (selected) {
          case "Protein":
            return intake.fields.total_caloric_breakdown.percent_proteins;
          case "Fat":
            return intake.fields.total_caloric_breakdown.percent_fat;
          case "Carbohydrates":
            return intake.fields.total_caloric_breakdown.percent_carbs;
          default:
            return 0;
        }
      }) || [];
    console.log(newParams);
    setParams(newParams);
  }, [selected, range, userDailies]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/nutrition-stats/${profile.id}`
        );
        setUserDailies(response.data);
      } catch (error) {
        console.error("Error fetching nutrition stats:", error);
      }
    };
    fetchData();
  }, [profile.id]);

  return (
    <>
      <div className="w-24 flex mx-auto mb-4">
        <GrayButton
          onClick={() => setRange(range === "Weekly" ? "Monthly" : "Weekly")}
        >
          {range === "Weekly" ? "Monthly" : "Weekly"}
        </GrayButton>
      </div>
      <div className="flex">
        {choices.map((param) => (
          <GrayButton key={param} onClick={() => setSelected(param)}>
            {param}
          </GrayButton>
        ))}
      </div>
      <BarChartCustom data={params} />
    </>
  );
}
