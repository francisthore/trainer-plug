import HeroSearchBar from "./HeroSearchBar";


const Hero = () => {
    return (
        <section className="pt-12 bg-gray-50 sm:pt-16">
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div className="max-w-2xl mx-auto text-center">
                <h1 className="px-6 text-lg text-gray-600 font-inter">Find Your Perfect Trainer on Trainer Plug.</h1>
                <p className="mt-5 text-4xl font-bold leading-tight text-gray-900 sm:leading-tight sm:text-5xl lg:text-6xl lg:leading-tight font-pj">
                Start Your Fitness Journey
                    <span className="relative inline-flex sm:inline">
                        <span className="bg-gradient-to-r from-[#44BCFF] via-[#FF44EC] to-[#FF675E] blur-lg filter opacity-30 w-full h-full absolute inset-0"></span>
                        <span className="relative"> Today! </span>
                    </span>
                </p>

                <div className="px-8 sm:items-center sm:justify-center sm:px-0 sm:space-x-5 sm:flex mt-9">
                   <HeroSearchBar />
                </div>

                <p className="mt-8 text-base text-gray-500 font-inter">Browse certified personal trainers based on your goals, location, and expertise. Train your way—online or in person.</p>
            </div>
        </div>
    </section>
    );
}


export default Hero;
