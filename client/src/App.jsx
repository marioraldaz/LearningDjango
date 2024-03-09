import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import { Navbar } from "./components/Navbar.jsx";
import { Home } from "./pages/Home.jsx";
import { Ingredients } from "./pages/Ingredients/Ingredients.jsx";
import { Recipes } from "./pages/Recipes/Recipes.jsx";
import { MyBalance } from "./pages/MyBalance/MyBalance.jsx";
import { Footer } from "./components/Footer.jsx";
import { Ingredient } from "./pages/Ingredients/Ingredient.jsx";
import { Profile } from "./pages/Profile/Profile.jsx";
import { Login } from "./pages/Profile/Login.jsx";
import { Register } from "./pages/Profile/Register.jsx";
import { RequireAuth } from "./pages/Profile/RequireAuth.jsx";
import { PrivateRoute} from "./utils/PrivateRoute.jsx";
import { AuthProvider } from "./context/AuthContext.jsx";
import { Provider } from "react-redux";
import  store  from "./redux/store.js";
import Cookies from 'js-cookie';

function App() {
  
  return (
      <Provider store={store}>
          <BrowserRouter>
            <AuthProvider>
            <div className="bg-black min-h-screen w-full text-white flex flex-col overflow-hidden">
            <Navbar />
            <div className="w-full min-h-full flex-grow">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/Ingredients" element={<Ingredients />} />
                <Route path="/Recipes" element={<Recipes />} />
                <Route path="/MyBalance" element={<MyBalance />} />
                <Route path="/Ingredient" element={<Ingredient />} />
                <Route path="/login" element={<Login />} />
                <Route path="/Register" element={<Register />} />
                <Route path="/Profile" element={<Profile />} />
                <Route path="/RequireAuth" element={<RequireAuth />} />
              </Routes>
            </div> 
            <Footer />
          </div>
          </AuthProvider>
        </BrowserRouter>
      </Provider>
    
    
  );
}

export default App;
