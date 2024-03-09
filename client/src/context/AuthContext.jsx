import { createContext, useState, useEffect } from 'react'
import jwtDecode from 'jwt-decode';
import { useNavigate } from 'react-router-dom'
import {getCookie} from '../api/users.api'
export const AuthContext = createContext()
import axios from 'axios'

export default AuthContext;

export const AuthProvider = ({children}) => {
    let [user, setUser] = useState(() => (!localStorage.getItem('authTokens')=='{"detail":"No active account found with the given credentials"}' ? jwtDecode(localStorage.getItem('authTokens')) : null))
    let [authTokens, setAuthTokens] = useState(() => (localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null))
    let [loading, setLoading] = useState(true)

    const navigate = useNavigate()

    let loginUser = async (e) => {

        e.preventDefault();
        const csrftoken = getCookie('csrftoken');
        console.log("csrf",csrftoken);
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
        console.log(response.data.token);
        setAuthTokens(response.data.token);
        setUser(response.data.user);
        console.log(user);
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
            console.log(authTokens.refresh);
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

    useEffect(()=>{
        const REFRESH_INTERVAL = 1000 * 60 * 4 // 4 minutes
        let interval = setInterval(()=>{
            if(authTokens){
                updateToken()
            }
        }, REFRESH_INTERVAL)
        return () => clearInterval(interval)

    },[authTokens])

    return(
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}