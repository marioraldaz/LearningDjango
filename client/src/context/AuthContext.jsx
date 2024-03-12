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
    let [authTokens, setAuthTokens] = useState(null);
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
        withCredentials: true
            });
        if(response.data.success){
            const token = response.data.token;
            const refreshToken = response.data.refresh_token
            console.log(response.data)
            setAuthTokens(token);
            setUser(response.data.user);
            Cookies.set('profileJWT', token, { secure: true, sameSite: 'strict' });
            Cookies.set('refreshToken', refreshToken, { secure: true, sameSite:'strict' });

        } else{
            return response.data.error
        }
    }

    let logoutUser = () => {
        console.log('logged out')
        Cookies.set('profileJWT',null)
        Cookies.set('profileRefreshToken',null)
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
               // logoutUser();
            }
        
            if (loading) {
                setLoading(false);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }

    let contextData = {
        user:user,
        authTokens:authTokens,
        loginUser:loginUser,
        logoutUser:logoutUser,
    }

    const getProfileByToken = async(token, csrfToken) => { 

            const response = await axios.post('http://localhost:8000/api/get_profile/', { token: token }, {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken 
                },
                withCredentials: true 
            });    
            console.log(response.data);
            if(response.data.success){
                setAuthTokens(token);
                setUser(response.data.user);            
            } else{
                return response.data.error
            }
    }
    
    useEffect(() => {
        const csrfGot = Cookies.get("csrftoken");
        setCsrfToken(csrfGot);
        
        const profileToken = Cookies.get('profileJWT');
        console.log("csrftoken", csrfGot, "jwt token", profileToken);
        
            getProfileByToken(profileToken, csrfGot)            
        
    
        
        const REFRESH_INTERVAL = 1000 * 60 * 4; 
        let interval = setInterval(() => {
            if (authTokens) {
                //updateToken();
            }
        }, REFRESH_INTERVAL);
    
        return () => clearInterval(interval);
    }, []);
    
    
    return(
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}