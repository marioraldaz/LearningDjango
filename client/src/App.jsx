import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { TaskPage } from "./pages/TaskPage";
import { Navigation } from "./components/Navigation";
import { TaskFormPage } from "./pages/TaskFormPage";

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<Navigate to="/tasks" />} />
        <Route path="/tasks" element={<TaskPage />}></Route>
        <Route path="/tasks-create" element={<TaskFormPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
