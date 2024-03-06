import React from "react";
import { useSelector } from "react-redux"
import { selectCurrentUser, selectCurrentToken } from "../../store/authSlice";
import { Link } from "react-router-dom"

export function Profile() {
  const user = useSelector(selectCurrentUser)
  const token = useSelector(selectCurrentToken)
  const welcome = user ? `Welcome ${user}` : 'Welcome'
  const tokenAbbr = `${token.slice(0,9)}...`

 
  return <div>{welcome} {tokenAbbr}</div>;
}
