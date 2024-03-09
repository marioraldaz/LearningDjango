import { createContext, useState, useEffect } from 'react'
import jwtDecode from 'jwt-decode';
import { useNavigate } from 'react-router-dom'
import {getCookie} from '../api/users.api'
import axios from 'axios'
import Cookies from 'js-cookie'


export const AuthContext = createContext()
export default AuthContext;

export const AuthProvider = ({children}) => {
    let [user, setUser] = useState(() => (!localStorage.getItem('authTokens')=='{"detail":"No active account found with the given credentials"}' ? jwtDecode(localStorage.getItem('authTokens')) : null))
    let [authTokens, setAuthTokens] = useState(() => (localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null))
    let [loading, setLoading] = useState(true)
    let [csrftoken, setCsrfToken] = useState(null)


    const navigate = useNavigate()

    let loginUser = async (e) => {

        e.preventDefault();
        const formData = {
            username: e.target.username.value,
            password: e.target.password.value,
        };
        const response = await axios.post('http://localhost:8000/user/login/', formData, {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        withCredentials: true // Include cookies in the request
            });
        if(response.data.success){
            setAuthTokens(response.data.token);
            setUser(response.data.user);
            Cookies.set("profileToken", response.data.token);
        } else{
            return response.data.error
        }
    }
        let logoutUser = (e) => {
            e.preventDefault()
            localStorage.removeItem('authTokens')
            setAuthTokens(null)
            setUser(null)
            navigate('/login')
        }

    
    const updateToken = async () => {

        try {
            const response = await axios.post('http://localhost:8000/api/token/refresh/', {
                refresh: authTokens.refresh
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        
            const data = response.data;

            if (response.status === 200) {
                setAuthTokens(data);
                setUser(jwtDecode(data.access));
                localStorage.setItem('authTokens', JSON.stringify(data));
            } else {
                logoutUser();
            }
        
            if (loading) {
                setLoading(false);
            }
        } catch (error) {
            // Handle errors
            console.error('Error:', error);
        }
        
    }
    //updateToken();
    let contextData = {
        user:user,
        authTokens:authTokens,
        loginUser:loginUser,
        logoutUser:logoutUser,
    }

    const getProfileByToken= (token)=>{
        const response = axios.post('http://localhost:8000/api/get_profile/', { token: token }, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            withCredentials: true // Include cookies in the request
        });
        
    }
    
    useEffect( ()=>{
        const csrfGot = Cookies.get("csrftoken")
        setCsrfToken(csrfGot);
        const profileToken = Cookies.get('profileToken');
        if(profileToken && csrfGot){
            profileToken ? setUser(getProfileByToken(profileToken)) : "";
        }
        console.log(user);
        const REFRESH_INTERVAL = 1000 * 60 * 4 // 4 minutes
        let interval = setInterval(()=>{
            if(authTokens){
                updateToken()
            }
        }, REFRESH_INTERVAL)
        return () => clearInterval(interval)

    },[authTokens, csrftoken]) //

    

    return(
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}