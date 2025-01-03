import { createContext, useState, useEffect, useContext, Children } from "react";
import API from "../api/axios";


const AuthContext = createContext();


export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({
        isAuthenticated: false,
        currentUserId: null,
        currentUserRole: null
    });

    useEffect(() => {
        const checkAuth = async () => {
            try {
                const response = await API.get('/auth/me');
                const user = response.data['user'];
                setAuth({
                    isAuthenticated: true,
                    currentUserId: user.sub,
                    currentUserRole: user.role
                });
            } catch (error) {
                setAuth({
                    isAuthenticated: false,
                    currentUserId: null,
                    currentUserRole: null
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
