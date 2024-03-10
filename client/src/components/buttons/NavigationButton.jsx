import React from 'react';

const NavigationButton = ({ link, text }) => {
  return (
    <a href={link} className="text-green-600 bg-neutral-800 p-3 rounded-lg">{text}</a>
  );
};

export default NavigationButton;
