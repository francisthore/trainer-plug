import MainTrainerCard from "./TrainerCards";


const TrainersListing = () => {
    return (
        <section className="md:px-10 px-4 md:py-10 py-4">
            <hr/>
        <h2 className="my-4 text-2xl text-center md:text-left font-extrabold leading-none tracking-tight text-gray-900 md:text-3xl lg:text-3xl ">
        Top Trainers Ready to Transform Your Life
        </h2>
        <div className="flex gap-2 flex-wrap items-start justify-start">
            <MainTrainerCard  trainer={trainer}/>
        </div>
        </section>
    );
};

export default TrainersListing;
