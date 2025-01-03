import API from "./axios";
import { useNavigate } from "react-router-dom";

export const registerUser = async (username, email, password) => {
    const userData = {
        username,
        email,
        password
    };
    const navigate = useNavigate();

    try {
        const response = await API.post('/auth/register', userData);
        navigate('/verify-email');
    } catch (error) {
        throw error.response ? error.response.data : new Error("Failed to register user. Try again");
    }

};


export const verifyEmail = async (token) => {
    try {
        const response = await API.get(`/auth/verify-email?token=${token}`);
        navigate('/login');
    } catch (error) {
        throw error.response ? error.response.data : new Error("Failed to verifiy email. Try again");
    }
}
