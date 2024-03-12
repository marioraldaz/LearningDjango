import React, {useContext} from 'react'
import {AuthContext} from "../../context/AuthContext"
export function ProfileDetails() {
    const context = useContext(AuthContext);
    console.log(context);
  return (
    <div className="grid span-cols-3 p-4">   
        <h1 className="col-span-3 text-center gradient-text text-3xl">Complete Your Profile For A More Detailed Control</h1>

        
    </div>
  )
}

