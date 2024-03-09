import {createSlice} from "@reduxjs/toolkit"

const initialState={
    username:"",
    email:"",

}

export const profileSlice = createSlice({
    name:"profile",
    initialState,
    reducers:{
       addProfile : (state, action) =>{
        const { username, email } = action.payload;
        state.username = username;
        state.email = email;
       },
       deleteProfile : (state) =>{
        state.username = "";
        state.email = "";
       }
    }
})

export const {addProfile, deleteProfile} = profileSlice.actions;
export default profileSlice.reducer;