import React, { useState, useEffect, useContext } from "react";
import { BarChart } from "./BarChart";
import { PieChart } from "./PieChart";
import { RadarChart } from "./RadarChart";
import { AreaChart } from "./AreaChart";
import { fetchUserDailies } from "../../api/food_intake.api";
import AuthContext from "../../context/AuthContext";

export function Stats() {
  const [data, setData] = useState([]);
  fetchUserDailies(data, setData);
  const { user } = useContext(AuthContext);
  return (
    <>
      {/*
      <BarChart data={data} />
      <PieChart data={data} />
      <RadarChart data={data} />
      <AreaChart data={data} />
      */}
    </>
  );
}
