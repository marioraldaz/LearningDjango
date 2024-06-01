import React, { useContext, useEffect, useState } from "react";
import { AuthContext } from "../../context/AuthContext";

export function NutriExpert() {
  const { user, nutriExpert } = useContext(AuthContext);
  const [profile, setProfile] = useState(null);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");

  const handleSendMessage = async () => {
    if (inputValue.trim() !== "") {
      setInputValue("");
      const prev = messages;
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: inputValue, fromUser: true },
      ]);
      try {
        const response = await nutriExpert(inputValue, prev);
        console.log(response);
        setMessages((prevMessages) => [
          ...prevMessages,
          { text: response, fromUser: false },
        ]);
      } catch (error) {
        console.error("An error occurred:", error);
      }
    }
  };
  useEffect(() => {
    setProfile(user);
  }, [user, profile]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <div className="gray-bg h-screen m-10 rounded-lg">
      <div className="mx-auto pt-8 w-1/2 h-16 gap-4 flex items-center justify-center">
        <input
          type="text"
          className="w-full h-full p-4 text-black"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Type a message..."
        />
        <button
          className="w-[100px] h-full bg-green-700 hover:scale-110"
          onClick={handleSendMessage}
        >
          Send
        </button>
      </div>
      <div className=" w-1/2 m-6 mx-auto flex bg-white justify-center flex-col text-black">
        {messages.map((message, index) => (
          <div key={index} className="text-black py-2 px-2 text-left flex">
            <span
              className={
                message.fromUser
                  ? "text-gray-600 mr-3 h-full w-[60px]"
                  : "text-red-700 mr-3 h-full w-[60px]"
              }
            >
              {message.fromUser ? "You:" : "Chatbot:"}
            </span>

            {String(message.text)}
          </div>
        ))}
      </div>
    </div>
  );
}

export default NutriExpert;
