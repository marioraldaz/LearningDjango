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
import { Footer } from "./components/Footer.jsx";

function App() {
  return (
    <BrowserRouter>
      <div className="bg-black min-h-screen w-full text-white flex flex-col">
        <Navbar />
        <div className="w-full flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Ingredients" element={<Ingredients />} />
            <Route path="/Recipes" element={<Recipes />} />
            <Route path="/MyBalance" element={<MyBalance />} />-
          </Routes>
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
