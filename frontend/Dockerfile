# Use Node.js LTS as base image
FROM node:20-slim

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Create a non-root user and switch to it
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose port 5173 for Vite dev server
EXPOSE 5173

# Set environment variables
ENV NODE_ENV=development

# Start the Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]
