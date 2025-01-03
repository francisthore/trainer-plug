import API from "./axios";


export const fetchTrainerProfiles = async () => {
    try {
        const response = await API.get('/trainers/');
        return response.data;
    } catch (error) {
        throw new Error("Failed to fetch trainer profiles", error);
    }
};


export const fetchTrainerProfile = async (userId) => {
    try {
        const response = await API.get(`/trainers/${userId}`);
        return response.data;
    } catch (error) {
        throw new Error("Failed to fetch trainer profile", error);
    }
};
