import React, { useState } from "react";
import { useForm } from "react-hook-form";


export function Login() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    // Here you can handle the form submission, e.g., send data to the server for authentication
    console.log('Submitted:', data);
  };

  return (
    <div className="flex items-center h-[500px] justify-center mt-[40px]">
       <form onSubmit={handleSubmit} className="w-[500px] bg-neutral-800 p-[50px] h-full rounded-2xl text-black" >
        <h1 className="text-4xl text-center text-white">Log In </h1>
          <div className="mt-10 flex justify-center items-center flex-col">
            <label htmlFor="username" className="block  text-green-600 font-semibold">Username:</label>
            <input
              type="text"
              id="username"
              name="username"
              className="text-center mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
              required
            />
          </div>

          <div className="mt-10 flex justify-center items-center flex-col">
            <label htmlFor="password" className="block text-green-600 font-semibold">Password:</label>
            <input
              type="password"
              id="password"
              name="password"
              className="mt-1 text-center block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
              required
            />
          </div>
          <div className="m-20 flex justify-center items-center flex-col">
          <button type="submit" 
          className="text-white block bg-green-700 p-[30px] pt-[10px] pb-[10px] rounded-lg"
          >Login</button>
        </div>
        </form>
    </div>
  )
}

