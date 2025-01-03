import { useNavigate } from "react-router-dom";


const WelcomeDashboard = () => {
    const navigate = useNavigate();

    return (
        <div className="grid place-items-center py-4 px-4">
            <div className="text-center mb-8">
                <h1 className="text-3xl font-bold text-gray-800">
                    Welcome to the Dashboard
                </h1>
                <p className="text-lg text-gray-600 mt-2">
                    What would you like to do?
                </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-4xl justify-center">
                <div className="bg-blue-500 text-white h-64 flex flex-col justify-center items-center rounded-lg shadow-md">
                    <h2 className="text-xl font-semibold">Client</h2>
                    <p className="text-sm mt-2 px-4 text-center">
                        Browse through trainers to find the perfect match for your fitness journey.
                    </p>
                    <button className="mt-4 bg-white text-blue-500 font-semibold px-4 py-2 rounded"
                        onClick={() => navigate('/browse-trainers')}>
                        Browse Trainers
                    </button>
                </div>

                <div className="bg-green-500 text-white h-64 flex flex-col justify-center items-center rounded-lg shadow-md">
                    <h2 className="text-xl font-semibold">Trainer</h2>
                    <p className="text-sm mt-2 px-4 text-center">
                        Complete your registration process to start training clients.
                    </p>
                    <button className="mt-4 bg-white text-green-500 font-semibold px-4 py-2 rounded">
                        Complete Registration
                    </button>
                </div>
            </div>
        </div>
    );
};


export default WelcomeDashboard;
