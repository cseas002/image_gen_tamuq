import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const handleGenerate = async () => {
    if (!prompt) return;

    const newMessage = { type: 'user', content: prompt };
    setMessages([...messages, newMessage]);
    setPrompt('');
    setLoading(true);

    try {
      const response = await axios.post('http://128.105.144.183:5000/generate', { prompt });
      const images = response.data.images; // assuming the API returns a list of base64 encoded images
      const imageMessages = images.map(image => ({ type: 'bot', content: `data:image/png;base64,${image}` }));
      setMessages([...messages, newMessage, ...imageMessages]);
    } catch (error) {
      console.error('Error generating image:', error);
      setMessages([...messages, newMessage, { type: 'error', content: 'Error generating image' }]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  return (
    <div className="App">
      <div className="chat-container">
        <div className="messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.type}`}>
              {message.type === 'bot' ? <img src={message.content} alt={`Generated ${index}`} /> : <p>{message.content}</p>}
            </div>
          ))}
          {loading && <div className="message bot"><div className="spinner"></div></div>}
          <div ref={messagesEndRef} />
        </div>
        <div className="input-container">
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter prompt"
            onKeyPress={(e) => e.key === 'Enter' && handleGenerate()}
          />
          <button onClick={handleGenerate} disabled={loading || !prompt}>
            {loading ? 'Generating...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
