# frontend/Dockerfile

# Stage 1: Build the application
FROM node:20-alpine AS builder

ARG PUBLIC_BACKEND_URL
ENV PUBLIC_BACKEND_URL=$PUBLIC_BACKEND_URL

WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application source code
COPY . .

# Build the application
RUN npm run build

FROM builder AS test
RUN npm run test

# Stage 2: Serve the application
FROM node:20-alpine

WORKDIR /app

# We need to install production dependencies
COPY --from=builder /app/package.json ./package.json
RUN npm install --omit=dev

# Copy the build output from the builder stage
COPY --from=builder /app/build ./build

EXPOSE 5173
ENV PORT=5173

# The host needs to be 0.0.0.0 to be accessible from outside the container.
# The adapter-node output respects the HOST environment variable.
ENV HOST=0.0.0.0

CMD [ "node", "build" ]
