/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import { useState } from "react";
import { sendMessage } from "../../api/messaging";
import { useAuth } from "../../context/AuthContext";


const SimpleMessage = ({ isOpen, onClose, userId }) => {
    const { auth } = useAuth();
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const [message, setMessage] = useState("");

    const handleMessageSend = async (e) => {
        e.preventDefault();
        try {
            if (message.length > 2) {
            const response = await sendMessage(auth.currentUserId, userId, message);
            setSuccess("Message sent successfully!")
            setMessage("");
            setError("");
        } else {
            setError("Message must be at least 2 characters long");
        }
        } catch (error) {
            setError("An error occured while sending message");
        }
    };

    if (!isOpen) return null;

    return (
        <div
            className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-60 backdrop-blur-sm"
            onClick={onClose}
        >
            <div
                className="relative bg-white rounded-lg shadow-lg p-6 max-w-sm w-full"
                onClick={(e) => e.stopPropagation()}
            >
                <h4 className="block text-2xl  font-bold my-2 text-center">Send a Message</h4>
                {error && <p className="text-red-500 text-sm">{error}</p>}
                {success && <p className="text-green-500 text-sm">{success}</p>}
                <form onSubmit={handleMessageSend} className="space-y-4">
                    <textarea
                        placeholder="Type message here..."
                        required
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        className="w-full border rounded-md p-2"
                    />
                    <button
                        type="submit"
                        className="w-full bg-black text-white py-2 rounded-md hover:bg-gray-700"
                    >
                        Send Message
                    </button>
                </form>
                <button
                    className="absolute top-2 right-2 text-gray-500 hover:text-gray-800"
                    onClick={onClose}
                >
                    ✕
                </button>
            </div>
        </div>
    );

};

export default SimpleMessage;
