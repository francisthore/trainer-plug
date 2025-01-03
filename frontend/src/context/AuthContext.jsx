import { createContext, useState, useEffect, useContext, Children } from "react";
import API from "../api/axios";


const AuthContext = createContext();


export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({
        isAuthenticated: false,
        userId: null,
        role: null
    });

    useEffect(() => {
        const checkAuth = async () => {
            try {
                const response = await API.get('/auth/me');
                setAuth({
                    isAuthenticated: true,
                    userId: response.data.username,
                    role: response.data.user.role
                });
            } catch (error) {
                setAuth({
                    isAuthenticated: false,
                    userId: null,
                    role: null
                });
            }

        };
        checkAuth();
    }, []);

    return (
        <AuthContext.Provider value={{auth, setAuth}}>
            {children}
        </AuthContext.Provider>
    );
}


export const useAuth = () => useContext(AuthContext);
