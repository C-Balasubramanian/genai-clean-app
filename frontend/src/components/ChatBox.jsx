import { useState, useRef, useEffect } from "react";
import { sendMessage, sendImage } from "../services/api";
import ReactMarkdown from "react-markdown";
import "../styles/ChatBox.css";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const fileInputRef = useRef();

  const chatWindowRef = useRef(null);

  // Auto scroll
  useEffect(() => {
    chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
  }, [messages]);

  // Send message
  async function handleSend() {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { sender: "user", text: input }]);

    try {
      const res = await sendMessage(input);
      setMessages((prev) => [...prev, { sender: "bot", text: res.reply }]);
    } catch (err) {
      setMessages((prev) => [...prev, { sender: "bot", text: "Error: " + err.message }]);
    }

    setInput("");
  }

  // Send image
  async function handleImageUpload(e) {
    const file = e.target.files[0];
    if (!file) return;

    setMessages((prev) => [...prev, { sender: "user", image: URL.createObjectURL(file) }]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await sendImage(formData);
      setMessages((prev) => [...prev, { sender: "bot", text: res.reply }]);
    } catch (err) {
      setMessages((prev) => [...prev, { sender: "bot", text: "Error: " + err.message }]);
    }
  }

  // Auto-resize textarea
//   function autoResize(e) {
//     e.target.style.height = "auto";
//     e.target.style.height = e.target.scrollHeight + "px";
//   }

  function autoResize(e) {
  const textarea = e.target;
  textarea.style.height = "auto";

  const newHeight = Math.min(textarea.scrollHeight, 140);  
  textarea.style.height = newHeight + "px";
}

  return (
    <div className="chat-container">
      <h1 className="title">GenAI Chat</h1>

      <div className="chat-window" ref={chatWindowRef}>
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.sender}`}>
            <div className="bubble">
              {msg.image ? (
                <img src={msg.image} alt="uploaded" style={{ maxWidth: "200px", borderRadius: "10px" }} />
              ) : (
                <ReactMarkdown>{msg.text}</ReactMarkdown>
              )}
            </div>
          </div>
        ))}
      </div>

      <div className="input-area">

        <button className="upload-btn" onClick={() => fileInputRef.current.click()}>
          📎
        </button>
        <input
          type="file"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={handleImageUpload}
        />

       <textarea
  className="input-box"
  placeholder="Type a message or upload..."
  value={input}
  onChange={(e) => setInput(e.target.value)}
  onInput={autoResize}
  rows={1}
  onKeyDown={(e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }}
/>


        <button className="send-btn" onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}
