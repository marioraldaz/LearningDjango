import React from "react";
import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  Legend,
} from "recharts";

export const RadarChartCustom = ({ data, dataType }) => {
  const dataPrefix = dataType === "weekly" ? "last_week" : "last_30_days";
  const fields = Object.keys(data).filter((key) => key.startsWith(dataPrefix));

  return (
    <RadarChart outerRadius={90} width={730} height={250} data={data}>
      <PolarGrid />
      <PolarAngleAxis dataKey="id" />
      <PolarRadiusAxis angle={30} domain={[0, 1]} />
      {fields.map((field) => (
        <>
          <Radar
            key={field}
            name={field.replace(`${dataPrefix}_`, "")}
            dataKey={field}
            stroke="#8884d8"
            fill="#8884d8"
            fillOpacity={0.6}
            label={(value, index) =>
              `${fields[index].replace(`${dataPrefix}_`, "")}: ${value}`
            } // Displaying values as labels
          />
        </>
      ))}
      <Legend />
    </RadarChart>
  );
};
