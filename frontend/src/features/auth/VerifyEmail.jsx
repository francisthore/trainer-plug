import { useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { verifyEmail } from "../../api/auth";


const VerifyEmailAlert = () => {
    const location = useLocation();
    const navigate =useNavigate();

    useEffect(() =>{
        const params = new URLSearchParams(location.search);
        const token = params.get("token");

        if (token) {
            const verify = async () => {
                try {
                    await verifyEmail(token);
                } catch (error) {
                    alert(error.message || "Failed to verify email");
                }
            };

            verify();
        }
    }, [location.search]);



    return (
        <div className="flex justify-center items-center h-96">
            <div className="relative flex flex-col my-6 bg-white shadow-sm border border-slate-200 rounded-lg w-96">
                <div className="p-4">
                    <h5 className="mb-2 text-slate-800 text-xl font-semibold">
                        {location.search.includes("token")
                        ? "Verifiyin email..."
                        : "Check your email inbox"}
                    </h5>
                    <p className="text-slate-600 leading-normal font-light">
                    {location.search.includes("token")
                    ? "Please wait while your email gets verified"
                    : "An email has been sent to your inbox with a verification link. Please open it and verify before loggin in."}
                    </p>
                </div>
            </div>
        </div>
    );
};

export default VerifyEmailAlert;
