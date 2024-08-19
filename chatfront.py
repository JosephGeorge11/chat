# npx create-react-app frontend
# cd frontend

import React, { useState } from 'react';
import axios from 'axios';

const ChatInterface = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const sendMessage = async () => {
        if (!input.trim()) return;
        
        // Add user message to chat history
        setMessages([...messages, { type: 'user', text: input }]);

        // Send request to backend
        try {
            const response = await axios.post('http://localhost:8000/chat', { message: input });
            setMessages([...messages, { type: 'user', text: input }, { type: 'bot', text: response.data.response }]);
        } catch (error) {
            console.error("Error sending message:", error);
        }

        setInput('');
    };

    return (
        <div className="chat-container">
            <div className="chat-box">
                {messages.map((msg, idx) => (
                    <div key={idx} className={`message ${msg.type}`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
                placeholder="Type your message..."
            />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default ChatInterface;


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# uvicorn app.main:app --reload
# npm start
