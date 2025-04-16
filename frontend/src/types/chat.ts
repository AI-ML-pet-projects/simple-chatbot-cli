interface Message {
  content: string;
  isUser: boolean;
}

interface ChatSession {
  id: string;
  messages: Message[];
}

export type { Message, ChatSession };
