import { useState, useEffect } from "react";
import { fetchTrainerProfile } from "../api/trainers";

const TrainerProfile = ({ userId, onClose }) => {
    const [trainer, setTrainer] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await fetchTrainerProfile(userId);
                setTrainer(data);
            } catch (error) {
                console.error(`${error}`);
            }
        }
        if (userId) fetchData();
    }, [userId]);

    if (!trainer) return null;

    return (
        <div
            className="fixed inset-0 z-[999] grid h-screen w-screen place-items-center bg-black bg-opacity-60 backdrop-blur-sm transition-opacity duration-300"
            onClick={onClose}
        >
            <div
                className="relative m-4 p-4 w-3/5 rounded-lg bg-white shadow-sm"
                onClick={(e) => e.stopPropagation()}
            >
                <div className="flex justify-between items-center pb-4">
                    <h2 className="text-xl font-medium text-slate-800">
                        {trainer.full_name}
                    </h2>
                    <button
                        className="text-gray-500 hover:text-gray-800"
                        onClick={onClose}
                    >
                        ✕
                    </button>
                </div>

                <div className="border-t border-slate-200 py-4 text-slate-600 font-light">
                    <p>{trainer.bio}</p>
                    <p>Hourly Rate: R{trainer.hourly_rate}</p>
                </div>
            </div>
        </div>
    );
}


export default TrainerProfile;
