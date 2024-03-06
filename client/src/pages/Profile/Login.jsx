import React from "react";
import {logIn} from "../../api/users.api";
import CSRFToken from './CSRFToken';

export function Login() {

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      username: e.target.elements.username.value,
      password: e.target.elements.password.value
    };
    try {
      const response = await logIn(formData);
      console.log('Login successful:', response);
      // Store authentication token or session information (e.g., response.data.token)
      // Redirect user to protected route or dashboard
    } catch (error) {
      console.error('Login failed:', error);
      // Handle login failure (e.g., display error message to user)
    }
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
          <div className="m-10 flex justify-center items-center flex-col text-white">
          <input type="hidden" name="next" value="{{ request.GET.next }}" />  

          <button type="submit" 
          className="text-white block bg-green-700 p-[30px] pt-[10px] pb-[10px] rounded-lg mb-[20px]"
          >Login</button>
            You Do Not Have An Account?
          <a href="/Register"
            className="mt-[10px] w-[100px] text-center text-white block bg-green-700 pt-[10px] pb-[10px] rounded-lg"
            >  Register
          </a>
        </div>
      <CSRFToken/>
        </form>
    </div>
  )
}

export default logIn