import { registerUser } from "../../api/auth";
import { useState } from "react";
import Assets from "../../assets/Assets";
import Login from "./Login";

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isLoginOpen, setIsLoginOpen] = useState(false)
  const [isLoading, setIsLoading] = useState(false);



  const handleRegistration = async (e) => {
    e.preventDefault();

    try {
      setError("");
      setIsLoading(true);
      await registerUser(username, email, password);
      setUsername("");
      setEmail("");
      setPassword("");
      setIsLoading(false);
    } catch (error) {
      setError(error.message || "Failed to register");
    }
  };


  return (
    <div className="bg-gray-50 flex items-center justify-center p-10">
      <div className="relative flex flex-col rounded-xl
    bg-gradient-to-r from-slate-50 to-gray-100 
    shadow-2xl  md:p-5 p-2 text-gray-900">
        <img src={Assets["logo_url"]} className="object-cover h-28 w-100"></img>
        <h4 className="block text-2xl  font-bold my-2 text-center">
          Create Your Account
        </h4>
        {error && <p className="text-red-500 mb-2">{error}</p>}
        <form className="mt-2 mb-2 w-80 max-w-screen-lg sm:w-96" onSubmit={handleRegistration}>
          <div className="mb-1 flex flex-col gap-6">
            <div className="w-full max-w-sm min-w-[200px]">
              <label className="block mb-2 text-sm text-slate-600">
                Username
              </label>
              <input type="text" className="w-full bg-transparent placeholder:text-slate-400 
        text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition 
        duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 
        shadow-sm focus:shadow"
        required
        placeholder="username"
        value={username}
        onChange={(e) => {setUsername(e.target.value)}}/>
            </div>
            <div className="w-full max-w-sm min-w-[200px]">
              <label className="block mb-2 text-sm text-slate-600">
                Email
              </label>
              <input type="email" className="w-full bg-transparent placeholder:text-slate-400
        text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition
        duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300
        shadow-sm focus:shadow"
        required
        placeholder="john@doe.com"
        value={email}
        onChange={(e) => {setEmail(e.target.value)}} />
            </div>
            <div className="w-full max-w-sm min-w-[200px]">
              <label className="block mb-2 text-sm text-slate-600">
                Password
              </label>
              <input type="password" className="w-full bg-transparent placeholder:text-slate-400
        text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition
        duration-300 ease focus:outline-none focus:border-slate-400
        hover:border-slate-300 shadow-sm focus:shadow"
        required
        placeholder="password"
        value={password}
        onChange={(e) => {setPassword(e.target.value)}} />
            </div>
          </div>
          <div className="mt-4 flex justify-center">
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
              ) : ("Sign Up" ) }
              </button>
          </div>

          <p className="flex justify-center mt-6 text-sm text-slate-600">
            Already have an account?
            <a role="button" onClick={() => { setIsLoginOpen(true) }} className="ml-1 text-sm font-semibold text-slate-700 underline">
              Login
            </a>
          </p>
        </form>
      </div>
      <Login isOpen={isLoginOpen} onClose={() => setIsLoginOpen(false)} />
    </div>
  );
};

export default Register;

