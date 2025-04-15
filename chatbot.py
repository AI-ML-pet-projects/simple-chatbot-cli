import getpass
import os
from typing import List
from colorama import init, Fore, Style
from langchain.chat_models import init_chat_model
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

def setup_environment():
    """Set up the OpenAI API key from environment or user input."""
    init()  # Initialize colorama
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(f"{Fore.YELLOW}Enter API key for OpenAI: {Style.RESET_ALL}")

def initialize_chat():
    """Initialize the chat model and memory."""
    llm = init_chat_model(
        "gpt-4o-mini",
        temperature=0.7,
        model_provider="openai",
    )
    memory = ConversationBufferMemory(return_messages=True)
    return llm, memory

def get_chat_response(llm: any, memory: ConversationBufferMemory, user_input: str) -> str:
    """Get response from the chat model."""
    try:
        # Add system message if this is the first message
        if not memory.chat_memory.messages:
            memory.chat_memory.add_message(SystemMessage(
                content="You are a helpful AI assistant. Be concise and friendly in your responses."
            ))
        
        # Add user message to memory
        memory.chat_memory.add_message(HumanMessage(content=user_input))
        
        # Get AI response
        response = llm.invoke(memory.chat_memory.messages)
        
        # Add AI response to memory
        memory.chat_memory.add_message(AIMessage(content=response.content))
        
        return response.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

def main():
    """Main chat loop."""
    setup_environment()
    llm, memory = initialize_chat()
    
    print(f"{Fore.GREEN}Welcome to the Chatbot!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Type 'exit' or 'quit' to end the conversation.")
    print(f"Type 'clear' to start a new conversation.{Style.RESET_ALL}")
    
    while True:
        user_input = input(f"\n{Fore.BLUE}You: {Style.RESET_ALL}").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['exit', 'quit']:
            print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
            break
            
        if user_input.lower() == 'clear':
            memory.clear()
            print(f"{Fore.YELLOW}Conversation cleared. Starting fresh!{Style.RESET_ALL}")
            continue
        
        response = get_chat_response(llm, memory, user_input)
        print(f"\n{Fore.GREEN}AI: {Style.BRIGHT}{response}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()


