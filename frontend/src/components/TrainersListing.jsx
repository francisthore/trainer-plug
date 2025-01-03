import { MainTrainerCard } from "./TrainerCards";
import { useState, useEffect } from "react";
import { fetchTrainerProfiles } from "../api/trainers";
import { ButtonLoading } from "./Button";
import TrainerProfile from "./TrainerProfile";


const TrainersListing = () => {
    const [trainers, setTrainers] = useState([]);
    const [selectedTrainerId, setSelectedTrainerId] = useState(null);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [loading, setLoading] = useState(true);

    const openModal = (userId) => {
        setSelectedTrainerId(userId);
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setSelectedTrainerId(null);
        setIsModalOpen(false);
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await fetchTrainerProfiles();
                setTrainers(data);
            } catch (error) {
                console.error(`${error}`);
            } finally {
                setLoading(false);
            }
        }
        fetchData()
    }, []);


    return (
        <section className="md:px-10 px-4 md:py-10 py-4">
            <hr />
            <h2 className="my-4 text-2xl text-center md:text-left font-extrabold leading-none tracking-tight text-gray-900 md:text-3xl lg:text-3xl ">
                Top Trainers Ready to Transform Your Life
            </h2>
            <div className="flex gap-2 flex-wrap items-start justify-start">
                {loading ? (
                    <div className="flex items-center justify-center w-full">
                        <ButtonLoading>
                            Loading personal trainers
                        </ButtonLoading>
                    </div>
                ) : trainers.length > 0 ? (
                    trainers.map((trainer) => (
                        <MainTrainerCard
                            key={trainer.id}
                            trainer={trainer}
                            openModal={openModal} />
                    ))
                ) : (
                    <p className="text-gray-500">No trainers found.</p>
                )}
            </div>
            {isModalOpen && (
                <TrainerProfile userId={selectedTrainerId} onClose={closeModal} />
            )}
        </section>
    );
};

export default TrainersListing;
