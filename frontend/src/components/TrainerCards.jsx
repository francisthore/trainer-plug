/* eslint-disable react/prop-types */
import { SolidButton } from "./Button";
import TrainerProfile from "./TrainerProfile";



const MainTrainerCard = ( { trainer, openModal } ) => {
    const generateProfilePicUrl = (filePath) => `${import.meta.env.VITE_S3_BASE_URL}/${filePath}`;


    return (
        <div className="relative flex flex-col my-6 bg-white shadow-sm border border-slate-200 rounded-lg w-96">
            <div className="relative h-56 m-2.5 overflow-hidden text-white rounded-md">
            <img src={generateProfilePicUrl(trainer.profile_picture)} alt={`${trainer.full_name}'s profile`} />
            </div>
            <div className="p-4">
                <div className="flex items-center mb-2">
                    <h6 className="text-slate-800 text-xl font-semibold">
                        {trainer.full_name}
                    </h6>

                    <div className="flex items-center gap-0 5 ml-auto">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                            className="w-5 h-5 text-yellow-600">
                            <path fillRule="evenodd"
                                d="M10.788 3.21c.448-1.077 1.976-1.077 2.424 0l2.082 5.007 5.404.433c1.164.093 1.636 1.545.749 2.305l-4.117 3.527 1.257 5.273c.271 1.136-.964 2.033-1.96 1.425L12 18.354 7.373 21.18c-.996.608-2.231-.29-1.96-1.425l1.257-5.273-4.117-3.527c-.887-.76-.415-2.212.749-2.305l5.404-.433 2.082-5.006z"
                                clipRule="evenodd"></path>
                        </svg>
                        <span className="text-slate-600 ml-1.5">5.0</span>
                    </div>
                </div>

                <p className="text-slate-600 leading-normal font-light">
                    {trainer.bio}
                </p>
            </div>

            <div className="group my-3 inline-flex flex-wrap justify-start px-4 items-center gap-2">
                <p className="font-bold">
                    R{trainer.hourly_rate}/h
                </p>
            </div>

            <div className="px-4 pb-4 pt-0 mt-2">
                <SolidButton onClick={() => openModal(trainer.user_id)}>
                    View Trainer Profile
                </SolidButton>
            </div>
        </div>
    );
};

export default MainTrainerCard;
