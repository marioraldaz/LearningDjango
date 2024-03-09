
import React, { useState, useEffect, useContext } from 'react'
import {AuthContext} from '../context/AuthContext';

export function Home() {

  
  return (
    <div className="flex items-center justify-center w-full text-green-600 text-4xl h-32">
      <h1 className="gradient-text">Living Fast Needs Keeping Track</h1>
    </div>
  );
}
