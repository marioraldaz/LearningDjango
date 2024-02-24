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
import { Ingredients } from "./pages/Ingredients.jsx";
import { Recipes } from "./pages/Recipes.jsx";
import { MyBalance } from "./pages/MyBalance.jsx";
redirect("/Home");

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Ingredients" element={<Ingredients />} />
        <Route path="/Recipes" element={<Recipes />} />
        <Route path="/MyBalance" element={<MyBalance />} />-
      </Routes>
    </BrowserRouter>
  );
}

export default App;
