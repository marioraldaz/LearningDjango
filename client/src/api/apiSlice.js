import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { setCredentials,logOut } from '../store/authSlice';

//attaching token in every cookie
const baseQuery = fetchBaseQuery({
    baseUrl: 'http://localhost:8000',
    credentials: 'include',
    prepareHeaders:(headers, {getState}) =>{
        const token = getState().auth.token;
        if(token){
            headers.append('authorization', `Bearer ${token}`);
        }
        return headers;
    }
});

const baseQueryWithReauth = async (args, api, extraoptions) => {
    let result = await baseQuery(args, api, extraoptions);

    if (result?.error?.originalStatus === 403) { //expired Token
        console.log('sending refresh token');
        const refreshResult= await baseQuery('/refresh', api, extraoptions);
        console.log(refreshResult);
    }
    if(result?.error?.data){
        const user = api.getState().auth.user
        //store new token
        api.dispatch(setCredentials({...refreshResult.data, user: user}))
        //retry the original query with new access token
        result = await baseQuery(args, api, extraoptions);
    } else{
        api.dispatch(logOut());
    }

    return result;
};

export const apiSlice = createApi({
    baseQuery: baseQueryWithReauth,
    endpoints: builder =>({})
});