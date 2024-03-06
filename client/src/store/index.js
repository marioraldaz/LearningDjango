import { configureStore } from '@reduxjs/toolkit';

import { authReducer } from './authSlice';
import { usersReducer } from './users.slice';

export * from './authSlice';
export * from './users.slice';

export const store = configureStore({
    reducer: {
        auth: authReducer,
        users: usersReducer
    },
});