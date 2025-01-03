import Assets from "../assets/Assets";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {SolidButton, OutlineButton} from "./Button";
import { useAuth } from "../context/AuthContext";
import API from "../api/axios";
import Login from "../features/auth/Login";


const Navbar = () => {
    const [isLoginOpen, setIsLoginOpen] = useState(false);
    const {auth, setAuth} = useAuth();
    const logo = Assets["logo_url"];
    const navigate = useNavigate();

    const handleLogout = async () => {
        try {
            await API.post("/auth/logout");
            setAuth({
                isAuthenticated: false,
                user: null,
                role: null,
            });
        } catch (error) {
            console.error("Logout failed", error);
        }
    };


    return (
        <nav className="flex justify-between items-center px-1 py-3 gap-1 bg-gray-50 overflow-hidden">
            <img src={ logo }
            alt="trainerplug logo"
            className="logo" 
            onClick={() => {navigate('/')}}
            ></img>
            <div className="flex gap-2">
                
                {auth.isAuthenticated ? (
                    <>
                    <OutlineButton onClick={handleLogout}>
                        Logout
                    </OutlineButton>
                    </>
                ) : (
                    <>
                    <SolidButton onClick={() => navigate('/register')}>
                    Become a Trainer
                </SolidButton>
                <OutlineButton onClick={() => setIsLoginOpen(true)}>
                    Login
                </OutlineButton>
                    </>
                )}

                
            </div>
            <Login isOpen={isLoginOpen} onClose={() => setIsLoginOpen(false)} />
        </nav>
    );
};

export default Navbar;
