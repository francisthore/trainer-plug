import API from "../../api/axios";

const handleLogout = async () => {
    try {
        await API.post("/auth/logout");
        alert("Logged out successfully!");
        window.location.href = "/login";
    } catch (error) {
        console.error("Logout failed:", error);
    }
};



