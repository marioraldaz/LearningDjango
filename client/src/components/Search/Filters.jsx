import React from "react";
import { Filter } from "./Filter";

export function Filters({ filters, onFilterChange, onSubmit }) {
  const handleFilterChange = (name, value) => {
    onFilterChange(name, value);
  };

  const handleSubmit = () => {
    onSubmit();
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
      <button
        type="button" // Change type to button to prevent form submission
        className="text-white bg-green-600 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        onClick={handleSubmit} // Attach onSubmit function to onClick event
      >
        Search For Ingredients
      </button>
    </div>
  );
}
