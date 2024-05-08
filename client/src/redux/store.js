import { configureStore } from "@reduxjs/toolkit";
import profileReducer from "./profileSlice";
import authReducer from "./authSlice";
import recipesReducer from "./recipesSlice";
import ingredientsReducer from "./ingredientsSlice";
import { persistReducer, persistStore } from "redux-persist";
import storage from "redux-persist/lib/storage";
import foodIntakeReducer from "./foodIntakeSlice";

const customSerialize = (value) => {
  return JSON.stringify(value);
};

const customDeserialize = (serializedValue) => {
  return JSON.parse(serializedValue);
};

const persistConfig = {
  key: "root",
  storage,
  serialize: customSerialize,
  deserialize: customDeserialize,
};

const pesistedRecipes = persistReducer(persistConfig, recipesReducer);
const persistedIngredients = persistReducer(persistConfig, ingredientsReducer);

const store = configureStore({
  reducer: {
    profile: profileReducer,
    auth: authReducer,
    recipes: pesistedRecipes,
    ingredients: persistedIngredients,
    foodIntakes: foodIntakeReducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware(),
});

const persistor = persistStore(store);

const purgePersistor = async () => {
  persistor.pause();
  persistor.flush().then(() => {
    return persistor.purge();
  });
};

export { store, persistor, purgePersistor };
