import { createSlice } from '@reduxjs/toolkit';


const initialState = {
    profileCookie: null, 
    profile: null,
    token: null
  };

const authSlice = createSlice({
    name:'auth',
    initialState,
    reducers:{
        setProfileCookie: (state, action) => {
            state.profileCookie = action.payload;
          },
        setCredentials: (state, action)=>{
            const { profile, accessToken} = action.payload;
            state.profile = profile;
            state.token = accessToken;
        },
        logOut: (state, action)=>{
            state.profile = null;
            state.token = null;
        }
    }
})

export const { setCredentials, logOut, setProfileCookie } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentprofile = (state) => state.auth.profile
export const selectCurrentToken= (state) => state.auth.token