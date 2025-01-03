/* eslint-disable react/prop-types */
import { useState, useEffect } from "react";
import { fetchTrainerProfile } from "../api/trainers";
import { SolidButton } from "./Button";

const generateProfilePicUrl = (filePath) => `${import.meta.env.VITE_S3_BASE_URL}/${filePath}`;


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
                <div className="flex items-center justify-between p-4">
                    <div className="flex items-center gap-3">
                        <img
                            alt={`${trainer.full_name}'s profile`}
                            src={generateProfilePicUrl(trainer.profile_picture)}
                            className="relative inline-block h-9 w-9 rounded-full object-cover object-center"
                        />
                        <div className="-mt-px flex flex-col">
                            <p className="text-sm text-slate-800 font-medium">
                                {trainer.full_name}
                            </p>
                            <p className="text-xs font-normal text-slate-500">
                                {trainer.specialization}
                            </p>
                        </div>
                    </div>
                    <div className="flex items-center gap-2">
                        <button className="rounded-md border border-transparent p-2.5 text-center text-sm transition-all text-slate-600 hover:bg-slate-100 focus:bg-slate-100 active:bg-slate-100 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4">
                                <path d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z" />
                            </svg>
                        </button>
                        <SolidButton onClick={() => alert("Chat coming soon!")}>
                            Message
                        </SolidButton>
                        <button
                            className="text-gray-500 hover:text-gray-800"
                            onClick={onClose}
                        >
                            ✕
                        </button>
                    </div>
                </div>
                <div className="flex justify-between items-center pb-4">


                </div>

                <div className="flex  gap-5 border-t border-slate-200 py-4">
                    <div className="text-slate-600 font-light">
                        <h2 className="text-xl md:text-2xl font-bold text-slate-800">
                            Hi I am {trainer.full_name}
                        </h2>
                        <p>{trainer.bio}</p>
                    </div>
                </div>
                <div className="flex shrink-0 flex-wrap items-center justify-between p-4 text-blue-gray-500">
                    <div className="flex items-center gap-16">
                        <div>
                            <p className="text-slate-500 text-md font-bold">
                                Hourly Rate
                            </p>
                            <p className="text-slate-800 font-medium">
                                R{trainer.hourly_rate}/h
                            </p>
                        </div>
                        <div>
                            <p className="text-slate-500 text-md font-bold">
                                Specialization
                            </p>
                            <p className="text-slate-800 font-medium">
                                {trainer.specialization}
                            </p>
                        </div>
                    </div>
                    <button className="flex items-center rounded-md border border-slate-300 py-2 px-4 text-center text-sm transition-all shadow-sm hover:shadow-lg text-slate-600 hover:text-black hover:bg-slate-800 hover:border-slate-800 focus:text-black focus:bg-slate-800 focus:border-slate-800 active:border-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24"
                            fill="currentColor"
                            aria-hidden="true"
                            className="h-4 w-4 mr-1.5"
                        >
                            <path
                                fillRule="evenodd"
                                d="M15.75 4.5a3 3 0 11.825 2.066l-8.421 4.679a3.002 3.002 0 010 1.51l8.421 4.679a3 3 0 11-.729 1.31l-8.421-4.678a3 3 0 110-4.132l8.421-4.679a3 3 0 01-.096-.755z"
                                clipRule="evenodd"
                            ></path>
                        </svg>
                        Share
                    </button>
                </div>


            </div>
        </div>
    );
}


export default TrainerProfile;
