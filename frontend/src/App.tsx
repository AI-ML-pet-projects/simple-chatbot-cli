"use client";

import type React from "react";

import { useState, useEffect, useRef } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Send, Plus } from "lucide-react";
import Header from "@/components/layout/header";
import Footer from "@/components/layout/footer";
import { ChatSession, Message } from "@/types/chat";
import { createNewChat, sendMessage } from "@/services/chatService";
import TypingIndicator from "@/components/common/typing-indicator";
import ReactMarkdown from "react-markdown";
import type { Components } from "react-markdown";

export default function ChatbotUI() {
  const [input, setInput] = useState<string>("");
  const [currentChat, setCurrentChat] = useState<ChatSession | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Create a new chat session when the component mounts
  useEffect(() => {
    handleCreateNewChat();
  }, []);

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [currentChat?.messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const handleCreateNewChat = async () => {
    setLoading(true);
    try {
      const data = await createNewChat();
      setCurrentChat(data);
    } catch (error) {
      console.error("Error creating new chat:", error);
      setCurrentChat({
        id: "-1",
        messages: [
          {
            content: "Failed to create new chat",
            isUser: false,
          },
        ],
      });
    } finally {
      console.log(currentChat);
      setLoading(false);
    }
  };

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!input.trim() || !currentChat) return;

    // Optimistically update UI
    const userMessage: Message = {
      content: input,
      isUser: true,
    };

    setCurrentChat((prev) =>
      prev
        ? {
            ...prev,
            messages: [...prev.messages, userMessage],
          }
        : null
    );

    setInput("");
    setLoading(true);

    try {
      const data = await sendMessage(input, currentChat.id);
      setCurrentChat((prev) =>
        prev
          ? {
              ...prev,
              messages: [...prev.messages, data],
            }
          : null
      );
    } catch (error) {
      console.error("Error sending message:", error);
      // Add error message
      setCurrentChat((prev) =>
        prev
          ? {
              ...prev,
              messages: [
                ...prev.messages,
                {
                  content:
                    "Sorry, I couldn't process your request. Please try again.",
                  isUser: false,
                },
              ],
            }
          : null
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className='flex flex-col min-h-screen bg-background'>
      {/* Header */}
      <Header />

      {/* Main content */}
      <main className='flex-1 container mx-auto px-4 py-8'>
        <Card className='w-full max-w-4xl mx-auto shadow-lg border-0 overflow-hidden'>
          <CardHeader className='bg-primary text-primary-foreground'>
            <div className='flex justify-between items-center'>
              <CardTitle>RMIT Career Assistant</CardTitle>
              <Button
                variant='ghost'
                size='icon'
                className='text-primary-foreground hover:bg-primary/90'
                onClick={handleCreateNewChat}
                disabled={loading}
              >
                <Plus className='h-5 w-5' />
              </Button>
            </div>
          </CardHeader>
          <CardContent className='p-0'>
            <div className='h-[60vh] overflow-y-auto p-6 bg-muted'>
              {currentChat?.messages.map((msg, index) => (
                <div
                  key={index}
                  className={`mb-4 flex ${
                    msg.isUser ? "justify-end" : "justify-start"
                  }`}
                >
                  <div
                    className={`max-w-[80%] p-3 rounded-lg ${
                      msg.isUser
                        ? "bg-destructive text-destructive-foreground"
                        : "bg-primary text-primary-foreground"
                    }`}
                  >
                    <ReactMarkdown
                      components={
                        {
                          p: (props: React.ComponentProps<"p">) => (
                            <p className='mb-2 last:mb-0' {...props} />
                          ),
                          strong: (props: React.ComponentProps<"strong">) => (
                            <strong className='font-bold' {...props} />
                          ),
                          em: (props: React.ComponentProps<"em">) => (
                            <em className='italic' {...props} />
                          ),
                          code: (props: React.ComponentProps<"code">) => (
                            <code
                              className='bg-black/20 px-1 py-0.5 rounded'
                              {...props}
                            />
                          ),
                          pre: (props: React.ComponentProps<"pre">) => (
                            <pre
                              className='bg-black/20 p-2 rounded overflow-x-auto'
                              {...props}
                            />
                          ),
                          ul: (props: React.ComponentProps<"ul">) => (
                            <ul className='list-disc pl-4 mb-2' {...props} />
                          ),
                          ol: (props: React.ComponentProps<"ol">) => (
                            <ol className='list-decimal pl-4 mb-2' {...props} />
                          ),
                          li: (props: React.ComponentProps<"li">) => (
                            <li className='mb-1' {...props} />
                          ),
                        } as Components
                      }
                    >
                      {msg.content}
                    </ReactMarkdown>
                  </div>
                </div>
              ))}
              {loading && <TypingIndicator />}
              <div ref={messagesEndRef} />
            </div>
          </CardContent>
          <CardFooter className='p-4 bg-muted'>
            <form
              onSubmit={(e) => handleSendMessage(e)}
              className='flex w-full space-x-2'
            >
              <Input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder='Type your message...'
                className='flex-grow'
                disabled={loading}
              />
              <Button
                type='submit'
                disabled={loading || !input.trim()}
                className='bg-destructive hover:bg-destructive/90 text-destructive-foreground'
              >
                <Send className='h-4 w-4' />
              </Button>
            </form>
          </CardFooter>
        </Card>
      </main>

      {/* Footer */}
      <Footer />
    </div>
  );
}
