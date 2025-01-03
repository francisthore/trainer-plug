import Assets from "../assets/Assets";
import {SolidButton, OutlineButton} from "./Button";
import { useAuth } from "../context/AuthContext";
import API from "../api/axios";


const Navbar = () => {
    const {auth, setAuth} = useAuth();
    const logo = Assets["logo_url"];

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
            onClick={() => {window.location.href = "/"}}
            ></img>
            <div className="flex gap-2">
                
                {auth.isAuthenticated ? (
                    <>
                    <span>Hi bro</span>
                    <OutlineButton onClick={handleLogout}>
                        Logout
                    </OutlineButton>
                    </>
                ) : (
                    <>
                    <SolidButton onClick={() => {window.location.href = '/trainer/register'}}>
                    Become a Trainer
                </SolidButton>
                <OutlineButton onClick={() => {window.location.href = '/login'}}>
                    Login
                </OutlineButton>
                    </>
                )}
                
            </div>
        </nav>
    );
};

export default Navbar;
