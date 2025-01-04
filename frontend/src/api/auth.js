import API from "./axios";

export const registerUser = async (username, email, password) => {
    const userData = {
        username,
        email,
        password
    };

    try {
        const response = await API.post('/auth/register', userData);
        window.location.href = '/verify-email';     
    } catch (error) {
        throw error.response ? error.response.data : new Error("Failed to register user. Try again");
    }

};


export const verifyEmail = async (token) => {
    try {
        const response = await API.get(`/auth/verify-email?token=${token}`);
    } catch (error) {
        throw error.response ? error.response.data : new Error("Failed to verifiy email. Try again");
    }
}
