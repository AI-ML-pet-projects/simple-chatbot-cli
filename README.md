# Simple Chatbot

A full-stack chatbot application built with Python (FastAPI) backend and React (Vite) frontend, powered by OpenAI's GPT models through LangChain.

## Features

- Interactive chat interface with multiple chat sessions
- Real-time message streaming
- Conversation history and memory
- Modern UI with Tailwind CSS
- Docker support for easy deployment
- TypeScript support for better code quality

## Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Docker and Docker Compose (optional)
- OpenAI API key

## Project Structure

```
simple_chatbot/
├── backend/               # Python FastAPI backend
│   ├── main.py           # FastAPI application
│   ├── chatbot.py        # Chatbot implementation
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        # Backend Docker configuration
│
├── frontend/             # React frontend
│   ├── src/             # Source files
│   │   ├── components/  # React components
│   │   ├── types/       # TypeScript types
│   │   └── App.tsx      # Main application
│   ├── package.json     # Node.js dependencies
│   └── Dockerfile       # Frontend Docker configuration
│
├── docker-compose.yml    # Docker Compose configuration
└── README.md            # Project documentation
```

## Quick Start

### Using Docker (Recommended)

1. Create a `.env` file in the root directory:

   ```
   OPENAI_API_KEY=your-api-key-here
   VITE_API_URL=http://backend:8000/api/v1
   ```

2. Start the application:

   ```bash
   docker-compose --env-file .env up -d
   ```

3. Access the application:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000

### Local Development

#### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:

   ```bash
   export OPENAI_API_KEY=your-api-key-here
   ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## API Documentation

The backend API provides the following endpoints:

- `POST /chat`: Send a message to the chatbot
- `POST /chat/new`: Create new chat

## Development

### Backend

The backend is built with FastAPI and uses LangChain for the chatbot implementation. Key features include:

- Conversation memory
- Message streaming
- Session management
- Error handling

### Frontend

The frontend is built with React and Vite, using TypeScript for type safety. Key features include:

- Multiple chat sessions
- Real-time message updates
- Modern UI with Tailwind CSS
- Responsive design

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
