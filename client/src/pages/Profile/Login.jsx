import { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { useLoginMutation } from "../../store/authApiSlice";
import {logIn} from "../../api/users.api";
import CSRFToken from './CSRFToken';
import { setCredentials } from "../../;

export function Login() {
  const userRef = userRef();
  const navigate = useNavigate();
  const errRef = useRef();
  const [user, setUser] = useState('');
  const [pwd, setPwd] = useState('');
  const [error, setError] = useState(null);
  const [errMsg, setErrMsg] = useState('');

  const [login, {isLoading}] = useLoginMutation()
  const dispatch = useDispatch();

  useEffect(()=>{
    userRef.current.focus();
  },[])

  useEffect(()=>{
    setErrMsg('')
  },[user, pwd])

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      username: e.target.elements.username.value,
      password: e.target.elements.password.value
    };

    try {
      const userData = await login({user, pwd}).unwrap();
      dispatch(setCredentials({...userData, user})) //user and access token
      setUser('')
      setPwd('')
      navigate('/profile')
      const res = await logIn(formData);
      if(res.status === 201){
        setError(NULL);
      } 
    } catch (error) {
      console.log(error);
      let errorsEntries = [];
      error.response ? errorsEntries = Object.entries(error.response.data) : "";
      let errorMessage = "";
      errorsEntries.forEach((error) => {
        errorMessage += `${error[0]}: ${error[1]}<br>`;
      });
      setErrMsg("ERROR");
      setError(errorMessage);
      errRef.current.focus();
    }
  };

  return (
    <div className="flex items-center justify-center mt-[40px]">
       <form onSubmit={handleSubmit} className="w-[500px] bg-neutral-800 p-[50px] h-full rounded-2xl text-black" >
        <h1 className="text-4xl text-center text-white">Log In </h1>
        {error &&     <div dangerouslySetInnerHTML={{ __html: error }} className="text-red-600 mt-8">
          </div>}
          <h1>{errMsg}</h1>
          <div className="mt-10 flex justify-center items-center flex-col">
            <label htmlFor="username" className="block  text-green-600 font-semibold">Username:</label>
            <input
              type="text"
              id="username"
              name="username"
              ref={userRef}
              value={user}
              onChange={handleUserInput}
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
              ref={userRef}
              value={pwd}
              onChange={handleUserInput}
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