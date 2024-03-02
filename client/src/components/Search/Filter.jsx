import React, { useState } from "react";

export function Filter({ filter, onChange }) {
  const [value, setValue] = useState("");

  const handleFilterChange = (event) => {
    setValue(event.target.value);
    onChange(filter.name, event.target.value);
  };

  return (
    <div className=" grid">
      <label htmlFor={filter.name}>{filter.label}</label>
      <input
        type={filter.type}
        id={filter.name}
        value={value}
        onChange={handleFilterChange}
      />
    </div>
  );
}
