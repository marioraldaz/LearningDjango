/* eslint-disable no-unused-vars */
import React from 'react'
import { NavLink } from "react-router-dom";

export function NavElem({text, route}) {
  return (
    <NavLink
    to={route}
    className="hover:text-green-400 hover:bg-neutral-800 p-[15px] transform hover:scale-110 transition duration-300 ease-in-out hover:border-lg rounded-lg 2 text-center"
  >
    <span className="text-3xl">{text}</span>
  </NavLink>
  )
}
