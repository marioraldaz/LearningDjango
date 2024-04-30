import React, { useState } from "react";
import { updateFitnessProfile } from "/src/api/fitCalcu.api.js";
import { BarChart } from "./BarChart";
import { PieChart } from "./PieChart";
import { RadarChart } from "./RadarChart";
import { AreaChart } from "./AreaChart";

export function Stats() {
  const [data, setData] = useState([]);
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
