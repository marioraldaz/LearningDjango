import React from 'react';

export const GrayButton = ({ onClick, children }) => {
  return (
    <button
      className="bg-neutral-800 p-2 rounded-lg hover:scale-105 hover:bg-green-800 m-4"
      onClick={onClick}
    >
      {children}
    </button>
  );
};

