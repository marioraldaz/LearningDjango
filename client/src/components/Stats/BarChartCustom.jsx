import React, { useEffect, useState } from "react";
import { BarChart } from "@mui/x-charts";

export function BarChartCustom({ values, dates }) {
  // Extracting data based on the display type
  return (
    <div className="bg-white flex flex-col w-full mt-4">
      <BarChart
        xAxis={[
          {
            scaleType: "band",
            data: dates.map((date) => {
              return date;
            }),
          },
        ]}
        series={[
          {
            data: Object.values(values).map((value) => {
              console.log(value);
              return value;
            }),
          },
        ]}
        width={500}
        height={300}
      />
    </div>
  );
}

export default BarChartCustom;
