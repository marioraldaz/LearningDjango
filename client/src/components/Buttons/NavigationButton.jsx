import React from 'react';

export const NavigationButton = ({ link, text }) => {
  return (
    <a href={link} className="text-green-600 bg-neutral-800 p-3 rounded-lg transform hover:bg-neutral-200 transition duration-300 ease-in-out ">{text}</a>
  );

};

