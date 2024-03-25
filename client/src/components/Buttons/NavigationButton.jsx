import React from "react";

export const NavigationButton = ({ link, text }) => {
  return (
    <a
      href={link}
      className="text-green-600 h-full bg-neutral-800 p-3 rounded-lg flex flex-wrap items-center transform hover:bg-neutral-200 transition duration-300 ease-in-out "
    >
      {text}
    </a>
  );
};
