# Use the official Node.js 18 image
FROM node:18

# Set working directory
WORKDIR /app

# Copy only the package files first to leverage Docker cache
COPY package*.json ./

# Ensure proper permissions inside container
RUN chown -R node:node /app

# Switch to the non-root 'node' user for safer builds
USER node

# Install dependencies (no optional packages, good for Docker)
RUN npm install --legacy-peer-deps --no-optional

# Copy the rest of the app
COPY --chown=node:node . .

# Expose Vite's dev server port
EXPOSE 5173

# Run the Vite dev server using npx
CMD ["npx", "vite", "--host", "0.0.0.0"]
