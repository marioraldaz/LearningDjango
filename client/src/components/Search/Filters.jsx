import React from "react";
import { Filter } from "./Filter";

export function Filters({ filters, onFilterChange }) {
  const handleFilterChange = (name, value) => {
    onFilterChange(name, value);
  };

  return (
    <div>
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
