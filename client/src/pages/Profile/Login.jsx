import { useState, useEffect, useRef, useContext } from "react";
import { useNavigate } from "react-router-dom";
import {logIn} from "../../api/users.api";
import AuthContext from '../../context/AuthContext'


export const Login = () =>{
  const { authTokens, logoutUser,loginUser } = useContext(AuthContext);
  let [profile, setProfile] = useState([])
  let [error, setError] = useState(null);

  useEffect(() => {
   
  },[])

  const getProfile = async () => {
    try {
        const response = await fetch('http://localhost:8000/api/profile', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens?.access)
            }
        });
        const data = await response.json();
        
        if (response.ok) {
            setProfile(data);
        } else if (response.status === 401) {
            logoutUser();
        }
    } catch (error) {
        console.error('Error fetching profile:', error);
    }
};

  return (
    <div className="flex items-center justify-center mt-[40px]">
       <form onSubmit={loginUser} className="w-[500px] bg-neutral-800 p-[50px] h-full rounded-2xl text-black" >
        <h1 className="text-4xl text-center text-white">Log In </h1>
        {error &&     <div dangerouslySetInnerHTML={{ __html: error }} className="text-red-600 mt-8">
          </div>}
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
        </form>
    </div>
  )
}

export default logIn