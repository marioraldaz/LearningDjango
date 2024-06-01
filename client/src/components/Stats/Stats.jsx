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
  const { user, getUserIntakes } = useContext(AuthContext);
  const [selected, setSelected] = useState("Protein");
  const [userDailies, setUserDailies] = useState([]);
  const [params, setParams] = useState([]);
  const [range, setRange] = useState("Weekly");
  const choices = ["Protein", "Fat", "Carbohydrates"];
  const [dates, setDates] = useState([]);

  if (!profile) {
    return <h1>Loading</h1>;
  }

  function filterLastWeek(data) {
    const now = new Date();
    const lastWeekStart = new Date(
      now.getFullYear(),
      now.getMonth(),
      now.getDate() - now.getDay() - 1
    );
    const lastWeekEnd = new Date();

    return data.filter((item) => {
      const itemDate = new Date(item.date);
      return itemDate >= lastWeekStart && itemDate < lastWeekEnd;
    });
  }

  function filterLast30Days(data) {
    const now = new Date();
    const thirtyDaysAgo = new Date(now.getTime() - 30 * 24 * 60 * 60 * 1000); // Calculate 30 days ago from now
    return data.filter((item) => {
      const itemDate = new Date(item.date);
      return itemDate >= thirtyDaysAgo && itemDate <= now; // Include items from 30 days ago up to now
    });
  }
  useEffect(() => {
    console.log(range);
    const newData =
      range === "Weekly"
        ? filterLastWeek(userDailies)
        : filterLast30Days(userDailies);
    const newParams =
      newData?.map((intake) => {
        switch (selected) {
          case "Protein":
            return {
              date: intake,
              amount: intake.details[0].recipe.nutrition.percent_protein,
            };
          case "Fat":
            return {
              date: intake,
              amount: intake.details[0].recipe.nutrition.percent_fat,
            };
          case "Carbohydrates":
            return {
              date: intake,
              amount: intake.details[0].recipe.nutrition.percent_carbs,
            };
          default:
            return 0;
        }
      }) || [];

    let dates = {};
    let amounts = {};
    newParams.forEach((intake) => {
      const date = intake.date.date;
      amounts[date] = (amounts[date] || 0) + intake.amount;
      dates[date] = true;
    });

    // Extract unique dates from the object keys
    let uniqueDates = Object.keys(dates);

    setParams(amounts);
    setDates(uniqueDates);
  }, [selected, range, userDailies]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/nutrition-stats/${profile.id}`
        );
      } catch (error) {
        console.error("Error fetching nutrition stats:", error);
      }
      const intakes = await getUserIntakes();
      intakes.sort((a, b) => new Date(a.date) - new Date(b.date));
      setUserDailies(intakes);
    };
    fetchData();
  }, [profile.id]);

  return (
    <>
      <div className="w-full flex mx-auto mb-4">
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

      <BarChartCustom values={params} dates={dates} />
    </>
  );
}
