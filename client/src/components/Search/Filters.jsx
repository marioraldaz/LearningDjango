import React from "react";
import { Filter } from "./Filter";

export function Filters({ filters, onFilterChange }) {
  const handleFilterChange = (name, value) => {
    onFilterChange(name, value);
  };

  return (
    <div className="bg-neutral-800 p-6 mt-4 border radius-lg rounded-2xl grid grid-cols-2 gap-3">
      {filters.map((filter) => (
        <Filter
          key={filter.name}
          filter={filter}
          onChange={handleFilterChange}
        />
      ))}
    </div>
  );
}
