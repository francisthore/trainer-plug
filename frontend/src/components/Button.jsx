/* eslint-disable react/prop-types */
export const SolidButton = ({ children, onClick }) => {
    return (
        <button
        type="button"
        className="inline-flex items-center justify-center w-full
        md:px-8 px-2 md:py-3 text-lg font-bold text-white transition-all
        duration-200 bg-gray-900 border-2 border-transparent
        sm:w-auto rounded-xl font-pj hover:bg-gray-600 focus:outline-none
        focus:ring-2 focus:ring-offset-2 focus:ring-gray-900"
        onClick={onClick}
        >
            { children }
        </button>
    );
};

export const OutlineButton = ({ children, onClick }) => {
    return (
        <button
        type="button"
        className="inline-flex items-center justify-center w-full
        md:px-6 md:py-3 text-lg font-bold text-gray-900 transition-all
        duration-200 border-2 border-gray-400 sm:w-auto sm:mt-0 rounded-xl
        font-pj focus:outline-none focus:ring-2 focus:ring-offset-2
        focus:ring-gray-900 hover:bg-gray-900 focus:bg-gray-900 hover:text-white
        focus:text-white hover:border-gray-900 focus:border-gray-900"
        onClick={onClick}
        >
            { children }
        </button>
    );
};
