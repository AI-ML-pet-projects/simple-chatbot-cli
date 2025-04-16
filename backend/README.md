# Simple Chatbot

A Python-based chatbot using LangChain and OpenAI's GPT models. This chatbot features a colorful CLI interface and conversation memory.

## Features

- Interactive command-line interface with colored output
- Conversation memory for context-aware responses
- Uses OpenAI's GPT models via LangChain
- Environment variable support for API keys
- Docker support for easy deployment

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Docker (optional, for containerized deployment)

## Local Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd simple_chatbot
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your-api-key-here`
   - Or, the chatbot will prompt you for the API key on first run

## Running the Chatbot

1. Activate your virtual environment (if not already activated):

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the chatbot:

```bash
python chatbot.py
```

3. Available commands:
   - Type your message to chat with the AI
   - Type `clear` to start a new conversation
   - Type `exit` or `quit` to end the session

## Docker Setup

1. Build the Docker image:

```bash
docker build -t simple-chatbot .
```

2. Run the container:

```bash
docker run -it --env OPENAI_API_KEY=your-api-key-here simple-chatbot
```

Alternatively, you can use a `.env` file with Docker:

```bash
docker run -it --env-file .env simple-chatbot
```

## Project Structure

```
simple_chatbot/
├── chatbot.py          # Main chatbot implementation
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
└── .env                # Environment variables (create this file)
```

## Dependencies

| Package            | Version  |
| ------------------ | -------- |
| `langchain`        | >=0.1.0  |
| `langchain-openai` | >=0.0.2  |
| `langchain-core`   | >=0.1.0  |
| `langgraph`        | >=0.2.28 |
| `python-dotenv`    | >=1.0.0  |
| `colorama`         | >=0.4.6  |
