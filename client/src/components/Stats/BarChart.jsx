import React, { useEffect, useState } from "react";
import { BarChart } from "@mui/x-charts";

export function BarChartCustom({ data, displayType }) {
  // Extracting data based on the display type

  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    if (data) {
      const newData =
        displayType === "weekly" ? data.last_week : data.last_month;
      setChartData(newData);
      console.log(chartData);
    }
  }, [data, displayType]);

  if (!chartData || chartData[0] === undefined) {
    return <h1>Loading</h1>;
  }
  return (
    <div className="bg-white">
      {chartData?.map((dayData, index) => (
        <div key={index}>
          <h2>
            {displayType === "weekly"
              ? `Week ${index + 1}`
              : `Day ${index + 1}`}
          </h2>
          <p>{JSON.stringify(dayData)}</p> {/* Render your data here */}
          {/* You can also pass this data to the BarChart component if needed */}
          <BarChart
            xAxis={[
              {
                scaleType: "band",
                data: ["Calories", "Fat", "Carbohydrates", "Protein"],
              },
            ]}
            series={[
              {
                data: Object.values(dayData.fields.total_nutrients),
                name: displayType === "weekly" ? "Weekly" : "Daily",
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
