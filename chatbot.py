import getpass
import os
import uuid
from typing import List, TypedDict, Annotated
from colorama import init, Fore, Style
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, trim_messages
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

from dotenv import load_dotenv


def setup_environment():
    """Set up the OpenAI API key from environment or user input."""
    init()  # Initialize colorama
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(f"{Fore.YELLOW}Enter API key for OpenAI: {Style.RESET_ALL}")

def initialize_chat():
    """Initialize the chat model and workflow."""
    llm = init_chat_model(
        "gpt-4o-mini",
        temperature=0.7,
        model_provider="openai",
    )

    trimmer = trim_messages(
      max_tokens=4000,
      strategy="last",
      token_counter=llm,
      include_system=True,
      allow_partial=False,
      start_on="human",    
    )
    
    # Define the workflow
    workflow = StateGraph(state_schema=MessagesState)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Be concise and friendly in your responses."),
        MessagesPlaceholder(variable_name="messages")
    ])
    # Define the model node
    def call_model(state: MessagesState):
        trimmed_messages = trimmer.invoke(state["messages"])
        prompt = prompt_template.invoke({ "messages": trimmed_messages })
        response = llm.invoke(prompt)
        return {"messages": [response] }
    
    # Add nodes and edges
    workflow.add_edge(START, "model")
    workflow.add_node("model", call_model)
    
    # Add memory
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)
    
    return app

def create_new_chat():
    """Create a new chat with a new thread_id."""
    new_thread_id = str(uuid.uuid4())
    print(f"{Fore.YELLOW}Starting new chat with Thread ID: {new_thread_id}{Style.RESET_ALL}")
    return {
        "state": MessagesState(messages=[SystemMessage(
            content="You are a helpful AI assistant. Be concise and friendly in your responses."
        )]),
        "config": {"configurable": {"thread_id": new_thread_id}}
    }

def load_chat(thread_id: str, app):
    """Load an existing chat with the given thread_id."""
    try:
        # Try to load the existing state
        state = app.get_state({"configurable": {"thread_id": thread_id}})
        print(f"{Fore.GREEN}Successfully loaded chat with Thread ID: {thread_id}{Style.RESET_ALL}")
        return {
            "state": state,
            "config": {"configurable": {"thread_id": thread_id}}
        }
    except Exception as e:
        print(f"{Fore.RED}Error loading chat: {str(e)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Creating new chat instead...{Style.RESET_ALL}")
        return create_new_chat()

def main():
    """Main chat loop."""
    setup_environment()
    app = initialize_chat()
    
    print(f"{Fore.GREEN}Welcome to the Chatbot!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Available commands:")
    print(f"- Type 'exit' or 'quit' to end the conversation")
    print(f"- Type 'clear' to start a new conversation")
    print(f"- Type 'new' to start a new chat with a new thread_id")
    print(f"- Type 'load <thread_id>' to load an existing conversation{Style.RESET_ALL}")
    
    # Initialize first chat
    chat_data = create_new_chat()
    state = chat_data["state"]
    config = chat_data["config"]
    
    while True:
        user_input = input(f"\n{Fore.BLUE}You: {Style.RESET_ALL}").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['exit', 'quit']:
            print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
            break
            
        if user_input.lower() == 'clear':
            state = MessagesState(messages=[SystemMessage(
                content="You are a helpful AI assistant. Be concise and friendly in your responses."
            )])
            print(f"{Fore.YELLOW}Conversation cleared. Starting fresh!{Style.RESET_ALL}")
            continue
            
        if user_input.lower() == 'new':
            chat_data = create_new_chat()
            state = chat_data["state"]
            config = chat_data["config"]
            continue
            
        if user_input.lower().startswith('load '):
            thread_id = user_input[5:].strip()
            if thread_id:
                chat_data = load_chat(thread_id, app)
                state = chat_data["state"]
                config = chat_data["config"]
            else:
                print(f"{Fore.RED}Please provide a thread_id to load.{Style.RESET_ALL}")
            continue
        
        # Add user message to state with naive check
        if (isinstance(state, dict)):
            state["messages"].append(HumanMessage(content=user_input))
        else:
            state.values["messages"].append(HumanMessage(content=user_input))
        
        # Get AI response with config
        output = app.invoke(state, config=config)
        state = output  # Update state with the response
        
        # Print the latest AI message
        latest_message = state["messages"][-1]
        if isinstance(latest_message, AIMessage):
            print(f"{Fore.CYAN}Thread ID: {config['configurable']['thread_id']}{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}AI: {Style.BRIGHT}{latest_message.content}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()


