
import React, { useState, useEffect, useContext } from 'react'

export function Home() {

  
  return (
    <div className="flex flex-wrap items-center justify-center w-full text-green-600 text-4xl h-32">


      <div className="w-full flex flex-wrap items-center justify-center">
        <h1 className="gradient-text ">Living Fast Needs Keeping Track</h1>
      </div>
      <div className="grid ">

      <a href="/recipes" className="text-white bg-neutral-800">Recipes Page</a>
      <a href="/ingredients">Ingredients Page</a>

      </div>
    </div>
  );
}
