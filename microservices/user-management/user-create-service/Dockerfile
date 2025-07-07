FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
# This Dockerfile sets up a Node.js application for user creation service.
# It uses the official Node.js 18 image, sets the working directory to /app,
# copies the package.json files, installs the dependencies, copies the application code,
# exposes port 3000, and starts the application using npm.