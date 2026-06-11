import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  // Auto-scroll to latest message
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat, loading]);

  const sendMessage = async () => {
    if (!message.trim() || loading) return;

    const userText = message.trim();
    const newChat = [...chat, { sender: "user", text: userText }];
    setChat(newChat);
    setMessage("");
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: userText }),
      });
      const data = await res.json();
      setChat([...newChat, { sender: "ai", text: data.response }]);
    } catch {
      setChat([
        ...newChat,
        { sender: "ai", text: "❌ Could not reach the server. Make sure the backend is running." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const clearChat = () => setChat([]);

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <div className="header-left">
          <span className="logo">🤖</span>
          <div>
            <h1>AI Coding Mentor</h1>
            <p className="subtitle">Ask anything about Python, Java, SQL, React…</p>
          </div>
        </div>
        {chat.length > 0 && (
          <button className="clear-btn" onClick={clearChat} title="Clear chat">
            🗑 Clear
          </button>
        )}
      </header>

      {/* Chat area */}
      <div className="chat-box">
        {chat.length === 0 && (
          <div className="empty-state">
            <div className="empty-icon">💬</div>
            <p>Start by asking a coding question</p>
            <div className="suggestions">
              {[
                "Write Python factorial program",
                "Explain Java inheritance",
                "What is SQL JOIN?",
                "How does useState work in React?",
              ].map((s) => (
                <button key={s} className="suggestion-chip" onClick={() => setMessage(s)}>
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}

        {chat.map((msg, index) => (
          <div key={index} className={`message-row ${msg.sender}`}>
            <div className="avatar">{msg.sender === "ai" ? "🤖" : "🧑‍💻"}</div>
            <div className={`bubble ${msg.sender}`}>
              {msg.sender === "ai" ? (
                <ReactMarkdown>{msg.text}</ReactMarkdown>
              ) : (
                msg.text
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="message-row ai">
            <div className="avatar">🤖</div>
            <div className="bubble ai typing">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}

        <div ref={chatEndRef} />
      </div>

      {/* Input area */}
      <div className="input-area">
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask a coding question… (Enter to send, Shift+Enter for new line)"
          rows={1}
          disabled={loading}
        />
        <button
          onClick={sendMessage}
          disabled={loading || !message.trim()}
          className="send-btn"
        >
          {loading ? "⏳" : "➤"}
        </button>
      </div>
      <p className="hint">Enter to send · Shift+Enter for new line</p>
    </div>
  );
}

export default App;
