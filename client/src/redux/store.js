import {configureStore} from '@reduxjs/toolkit';
import profileReducer from "./profileSlice";
import authReducer from './authSlice';
import recipesReducer from './recipesSlice';


export const store = configureStore({
    reducer: {
        profile: profileReducer,
        auth: authReducer,
        recipes: recipesReducer
    },
})

export default store;