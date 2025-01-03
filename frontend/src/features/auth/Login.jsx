import  { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import API from "../../api/axios"
import Assets from "../../assets/Assets";


const Login = ({ isOpen, onClose }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await API.post("auth/login", { username, password });
            onClose();
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
                    <button
                        type="submit"
                        className="w-full bg-black text-white py-2 rounded-md hover:bg-gray-700"
                    >
                        Login
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
