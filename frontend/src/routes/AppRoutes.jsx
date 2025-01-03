import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Login from "../features/auth/Login";
import Register from "../features/auth/Register";
import NotFound from "../pages/NotFound";
import Dashboard from "../pages/Dashboard";
import VerifyEmailAlert from "../features/auth/VerifyEmail";
import BrowseTrainers from "../pages/BrowseTrainers";

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/verify-email" element={<VerifyEmailAlert />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/browse-trainers" element={<BrowseTrainers />} />
            <Route path="*" element={<NotFound />} />
        </Routes>
    );
};

export default AppRoutes;
