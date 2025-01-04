import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../../api/axios"
import Assets from "../../assets/Assets";
import { useAuth } from "../../context/AuthContext";


const Login = ({ isOpen, onClose }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();
    const { setAuth } = useAuth();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            setIsLoading(true);
            const response = await API.post("auth/login", { username, password });
            const user = response.data;
            setAuth({
                isAuthenticated: true,
                currentUserId: user.id,
                currentUserRole: user.role
            });
            onClose();
            setIsLoading(false);
            navigate("/dashboard");
        } catch (error) {
            setError(`Login failed, please check your credentials ${error.message}`)
        }
    };

    if (!isOpen) return null;

    return (
        <div
            className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-60 backdrop-blur-sm"
            onClick={onClose}
        >
            <div
                className="relative bg-white rounded-lg shadow-lg p-6 max-w-sm w-full"
                onClick={(e) => e.stopPropagation()}
            >
                <img src={Assets["logo_url"]} className="object-cover h-28 w-full"></img>
                <h4 className="block text-2xl  font-bold my-2 text-center">Login</h4>
                {error && <p className="text-red-500 text-sm">{error}</p>}
                <form onSubmit={handleLogin} className="space-y-4">
                    <input
                        type="text"
                        placeholder="Username"
                        required
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="w-full border rounded-md p-2"
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        required
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full border rounded-md p-2"
                    />
                    <button type="submit" className="w-full bg-black text-white flex justify-center align-center py-2 rounded-md hover:bg-gray-700">
                        {isLoading ? (
                            <svg className="text-gray-300 animate-spin" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"
                                width="24" height="24">
                                <path
                                    d="M32 3C35.8083 3 39.5794 3.75011 43.0978 5.20749C46.6163 6.66488 49.8132 8.80101 52.5061 11.4939C55.199 14.1868 57.3351 17.3837 58.7925 20.9022C60.2499 24.4206 61 28.1917 61 32C61 35.8083 60.2499 39.5794 58.7925 43.0978C57.3351 46.6163 55.199 49.8132 52.5061 52.5061C49.8132 55.199 46.6163 57.3351 43.0978 58.7925C39.5794 60.2499 35.8083 61 32 61C28.1917 61 24.4206 60.2499 20.9022 58.7925C17.3837 57.3351 14.1868 55.199 11.4939 52.5061C8.801 49.8132 6.66487 46.6163 5.20749 43.0978C3.7501 39.5794 3 35.8083 3 32C3 28.1917 3.75011 24.4206 5.2075 20.9022C6.66489 17.3837 8.80101 14.1868 11.4939 11.4939C14.1868 8.80099 17.3838 6.66487 20.9022 5.20749C24.4206 3.7501 28.1917 3 32 3L32 3Z"
                                    stroke="currentColor" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round"></path>
                                <path
                                    d="M32 3C36.5778 3 41.0906 4.08374 45.1692 6.16256C49.2477 8.24138 52.7762 11.2562 55.466 14.9605C58.1558 18.6647 59.9304 22.9531 60.6448 27.4748C61.3591 31.9965 60.9928 36.6232 59.5759 40.9762"
                                    stroke="currentColor" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" className="text-gray-900">
                                </path>
                            </svg>
                        ) : ("Login")}
                    </button>
                </form>
                <p className="text-center text-sm mt-4">
                    Don&apos;t have an account?{" "}
                    <span
                        onClick={() => {
                            navigate("/register");
                            onClose();
                        }}
                        className="text-blue-500 underline cursor-pointer"
                    >
                        Register
                    </span>
                </p>
                <button
                    className="absolute top-2 right-2 text-gray-500 hover:text-gray-800"
                    onClick={onClose}
                >
                    ✕
                </button>
            </div>
        </div>
    );
};

export default Login
