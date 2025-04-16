import { ChatSession, Message } from "@/types/chat";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

export const createNewChat = async (): Promise<ChatSession> => {
  const response = await fetch(`${API_URL}/chat/new`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Failed to create new chat");
  }

  const data = await response.json();

  return {
    id: data.chat_id,
    messages: [
      {
        content: data.message,
        isUser: false,
      },
    ],
  };
};

export const sendMessage = async (
  message: string,
  chatId: string
): Promise<Message> => {
  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
      chat_id: chatId,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to send message");
  }

  const data = await response.json();

  return {
    content: data.message,
    isUser: false,
  };
};
