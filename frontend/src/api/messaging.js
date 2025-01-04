import API from "./axios";


export const sendMessage = async (senderId, receiverId, content) => {
    const messageData = {
        "sender_id": senderId,
        "receiver_id": receiverId,
        "content": content
    }
    try {
        const response = await API.post('/messages/', messageData);
    } catch (error) {
        throw new Error("Failed sending message", error);
    }
};
