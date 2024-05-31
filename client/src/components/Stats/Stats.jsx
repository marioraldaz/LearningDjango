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
      now.getDate() - now.getDay() - 7
    );
    const lastWeekEnd = new Date(
      now.getFullYear(),
      now.getMonth(),
      now.getDate() - now.getDay()
    );

    return data.filter((item) => {
      const itemDate = new Date(item.date);
      return itemDate >= lastWeekStart && itemDate < lastWeekEnd;
    });
  }

  function filterLastMonth(data) {
    const now = new Date();
    const lastMonth = new Date(now.getFullYear(), now.getMonth() - 1, 1);
    const thisMonth = new Date(now.getFullYear(), now.getMonth(), 1);
    return data.filter((item) => {
      const itemDate = new Date(item.date);
      return itemDate >= lastMonth && itemDate < thisMonth;
    });
  }
  useEffect(() => {
    const newData =
      range === "Weekly"
        ? filterLastWeek(userDailies)
        : filterLastMonth(userDailies);

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

    let dates = [];
    let amounts = [];
    newParams.map((intake) => {
      const date = intake.date.date;
      console.log(date);
      amounts[date]
        ? (amounts[date] += intake.amount)
        : (amounts[date] = intake.amount);

      dates[date] || dates.push(date);
    });

    setParams(amounts);
    setDates(dates);
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
      setUserDailies(intakes);
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
      <BarChartCustom values={params} dates={dates} />
    </>
  );
}
