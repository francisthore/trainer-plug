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



  const handleRegistration = async (e) => {
    e.preventDefault();

    try {
      setError("");

      await registerUser(username, email, password);
      setUsername("");
      setEmail("");
      setPassword("");
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
            <button type="submit" className="w-full bg-black text-white py-2 rounded-md hover:bg-gray-700">Sign Up</button>
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

