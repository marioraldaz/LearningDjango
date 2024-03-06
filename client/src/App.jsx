import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
  NavLink,
  redirect,
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
function App() {
  return (
    <BrowserRouter>
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
    </BrowserRouter>
  );
}

export default App;
