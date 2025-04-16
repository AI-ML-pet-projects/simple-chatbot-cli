# Simple Chatbot Frontend

A modern React-based frontend for the Simple Chatbot application, featuring a clean and intuitive chat interface.

## Features

- Interactive chat interface with multiple chat sessions
- Real-time message streaming with typing indicators
- Markdown support for rich message formatting
- Modern UI using Tailwind CSS and shadcn/ui components
- Responsive design that works on desktop and mobile
- TypeScript for enhanced code quality and developer experience

## Tech Stack

- React 19
- TypeScript 5.7
- Vite 6.2
- Tailwind CSS 4.1
- shadcn/ui components
- Radix UI primitives
- React Markdown
- Lucide React icons

## Project Structure

```
frontend/
├── src/
│   ├── components/         # React components
│   ├── lib/               # Utility functions and configurations
│   ├── services/          # API services and data fetching
│   ├── types/             # TypeScript type definitions
│   ├── assets/            # Static assets
│   ├── App.tsx            # Main application component
│   ├── main.tsx           # Application entry point
│   ├── index.css          # Global styles
│   └── vite-env.d.ts      # Vite environment type definitions
├── public/                # Static files
├── vite.config.ts         # Vite configuration
├── tailwind.config.ts     # Tailwind CSS configuration
├── postcss.config.js      # PostCSS configuration
├── tsconfig.json          # TypeScript configuration
├── tsconfig.node.json     # Node-specific TypeScript config
├── tsconfig.app.json      # Application-specific TypeScript config
├── eslint.config.js       # ESLint configuration
├── components.json        # shadcn/ui configuration
└── Dockerfile             # Docker configuration
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Docker (optional, for containerized deployment)

### Local Development

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

4. Open your browser and visit:
   ```
   http://localhost:5173
   ```

### Docker Development

1. Build and start the frontend container:

   ```bash
   docker-compose up frontend
   ```

2. Access the application at:
   ```
   http://localhost:5173
   ```

## Environment Variables

Create a `.env` file in the frontend directory with the following variables:

```
VITE_API_URL=http://localhost:8000/api/v1
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Key Dependencies

### Core

- React 19
- TypeScript 5.7
- Vite 6.2

### UI Components

- Tailwind CSS 4.1
- shadcn/ui
- Radix UI
- Lucide React icons

### Development Tools

- ESLint 9.21
- PostCSS 8.5
- TypeScript ESLint 8.24

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
