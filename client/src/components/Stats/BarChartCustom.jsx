import React, { useEffect, useState } from "react";
import { BarChart } from "@mui/x-charts";

export function BarChartCustom({ data }) {
  // Extracting data based on the display type

  return (
    <div className="bg-white flex flex-col w-full mt-4">
      {data?.map((value, index) => (
        <div key={index}>
          <BarChart
            xAxis={[
              {
                scaleType: "band",
                data: ["Calories", "Fat", "Carbohydrates", "Protein"],
              },
            ]}
            series={[
              {
                data: [4, 3, 5],
              },
            ]}
            width={500}
            height={300}
          />
        </div>
      ))}
    </div>
  );
}

export default BarChartCustom;
