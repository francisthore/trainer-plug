import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Login from "../features/auth/Login";
import RegisterTrainer from "../features/auth/RegisterTrainer";
import NotFound from "../pages/NotFound";
import Dashboard from "../pages/Dashboard";

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register-trainer" element={<RegisterTrainer />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="*" element={<NotFound />} />
        </Routes>
    );
};

export default AppRoutes;
