import { configureStore } from '@reduxjs/toolkit';
import profileReducer from "./profileSlice";
import authReducer from './authSlice';
import recipesReducer from './recipesSlice';
import { persistReducer, persistStore } from 'redux-persist';
import storage from 'redux-persist/lib/storage'; 

const customSerialize = (value) => {
  return JSON.stringify(value);
};

const customDeserialize = (serializedValue) => {
  return JSON.parse(serializedValue);
};

const persistConfig = {
  key: 'root',
  storage,
  serialize: customSerialize,
  deserialize: customDeserialize,
};

const persistedReducer = persistReducer(persistConfig, recipesReducer);

 const store = configureStore({
  reducer: {
    profile: profileReducer,
    auth: authReducer,
    recipes: persistedReducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware(),
});

const persistor = persistStore(store);

export { store, persistor };
