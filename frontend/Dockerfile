# Base stage: Install dependencies
FROM node:20 AS base
WORKDIR /app

# Copy package.json and package-lock.json first to leverage Docker caching
COPY package.json ./
RUN npm install

# Copy the rest of the source code
COPY . .

# Build stage: For production builds
FROM base AS build
WORKDIR /app
RUN npm run build

# Production stage: Serve built files with Nginx
FROM nginx:alpine AS prod
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Development stage: For live reloading
FROM base AS dev
WORKDIR /app
RUN npm install -g vite
CMD ["vite", "serve", "--host"]
