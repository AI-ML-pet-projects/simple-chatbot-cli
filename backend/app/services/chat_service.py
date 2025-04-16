import uuid
from typing import Dict, List
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, trim_messages
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from dotenv import load_dotenv

class ChatService:
    def __init__(self):
        self.app = self._initialize_chat()
        self.active_chats = {}  # Store active chat sessions

    def _initialize_chat(self):
        """Initialize the chat model and workflow."""
        load_dotenv()
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
            return {"messages": state["messages"] + [response]}
        
        # Add nodes and edges
        workflow.add_edge(START, "model")
        workflow.add_node("model", call_model)
        
        # Add memory
        memory = MemorySaver()
        return workflow.compile(checkpointer=memory)

    def create_chat(self) -> str:
        """Create a new chat session and return its ID."""
        chat_id = str(uuid.uuid4())
        self.active_chats[chat_id] = {
            "state": MessagesState(messages=[SystemMessage(
                content="You are a helpful AI assistant. Be concise and friendly in your responses."
            )]),
            "config": {"configurable": {"thread_id": chat_id}}
        }
        return chat_id

    def get_chat(self, chat_id: str) -> Dict:
        """Get chat session by ID."""
        return self.active_chats.get(chat_id)

    def send_message(self, chat_id: str, message: str) -> Dict:
        """Send a message to the chat and get the response."""
        chat = self.get_chat(chat_id)
        if not chat:
            raise ValueError("Chat session not found")

        # Add user message to state
        chat["state"]["messages"].append(HumanMessage(content=message))
        
        # Get AI response
        output = self.app.invoke(chat["state"], config=chat["config"])
        chat["state"] = output  # Update state with the response
        
        # Return the latest AI message
        latest_message = chat["state"]["messages"][-1]
        return {
            "message": latest_message.content,
            "chat_id": chat_id
        }

# Create a singleton instance
chat_service = ChatService() 