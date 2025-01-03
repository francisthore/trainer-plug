import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Login from "../features/auth/Login";
import RegisterTrainer from "../features/auth/RegisterTrainer";
import NotFound from "../pages/NotFound";
import Dashboard from "../pages/Dashboard";
import VerifyEmailAlert from "../features/auth/VerifyEmail";

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/trainer/register" element={<RegisterTrainer />} />
            <Route path="/verify-email" element={<VerifyEmailAlert />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="*" element={<NotFound />} />
        </Routes>
    );
};

export default AppRoutes;
