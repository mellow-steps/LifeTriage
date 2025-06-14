import { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [isListening, setIsListening] = useState(false);

  const startListening = () => {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = true;

    recognition.onresult = (event) => {
      const transcript = Array.from(event.results)
        .map(result => result[0].transcript)
        .join('');
      setText(transcript);
    };

    recognition.onend = () => setIsListening(false);
    setIsListening(true);
    recognition.start();
  };

  const sendToBackend = async () => {
    console.log('Sending text:', text); // Debug: see what we're sending
    
    try {
      const response = await fetch('/api/tasks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task: text })
      });
      
      console.log('Response status:', response.status); // Debug: see response
      const result = await response.text();
      console.log('Response:', result); // Debug: see what Flask returns
      
      if (response.ok) {
        setText('');
        console.log('Task sent successfully!');
      } else {
        console.log('Error: Response not OK');
      }
    } catch (error) {
      console.log('Fetch error:', error); // Debug: see any network errors
    }
  };

  return (
    <div className="App">
      <h1>Life Triage</h1>
      <button 
        onClick={startListening} 
        disabled={isListening}
      >
        {isListening ? 'Listening...' : 'Talk Now'}
      </button>
      <textarea 
        value={text} 
        readOnly 
        rows="4" 
        cols="50" 
      />
      <button 
        onClick={sendToBackend} 
        disabled={!text}
      >
        Submit
      </button>
    </div>
  );
}

export default App;