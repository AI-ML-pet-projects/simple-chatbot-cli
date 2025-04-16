# Simple Chatbot Backend

A FastAPI-based backend for the Simple Chatbot application, powered by LangChain and OpenAI's GPT models.

## Features

- RESTful API endpoints for chat functionality
- Conversation memory and session management
- Integration with OpenAI's GPT models via LangChain
- Real-time message streaming
- Docker support for easy deployment
- Environment variable configuration

## Tech Stack

- FastAPI 0.109.0
- Uvicorn 0.27.0
- LangChain 0.1.0
- LangChain OpenAI 0.0.2
- LangChain Core 0.1.0
- LangGraph 0.0.15
- Pydantic 2.6.0
- Python 3.8+

## Project Structure

```
backend/
├── app/
│   ├── api/              # API routes and endpoints
│   ├── services/         # Business logic and services
│   ├── __init__.py       # Package initialization
│   └── main.py           # FastAPI application
├── chatbot.py            # Chatbot implementation
├── run.py                # Application entry point
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── .env                  # Environment variables
└── .env.example          # Example environment variables
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Docker (optional, for containerized deployment)

### Local Development

1. Navigate to the backend directory:

   ```bash
   cd backend
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

4. Set up your environment variables:

   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your configuration

5. Run the application:
   ```bash
   python run.py
   ```

### Docker Development

1. Build and start the backend container:

   ```bash
   docker-compose --env-file .env up backend
   ```

2. The API will be available at:
   ```
   http://localhost:8000
   ```

## API Documentation

The backend provides the following endpoints:

- `POST /chat` - Send a message to the chatbot
- `POST /chat/new` - Create new chat

API documentation is available at:

```
http://localhost:8000/docs
```

## Environment Variables

Required environment variables:

```
OPENAI_API_KEY=your-api-key-here
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=simple-chatbot
```

## Dependencies

### Core

- FastAPI - Web framework
- Uvicorn - ASGI server
- LangChain - LLM framework
- LangChain OpenAI - OpenAI integration
- LangChain Core - Core LangChain functionality
- LangGraph - Graph-based conversation management

### Development

- Python-dotenv - Environment variable management
- Colorama - Terminal color output
- Pydantic - Data validation
- Python-multipart - Form data handling

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
