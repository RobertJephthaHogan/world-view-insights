FROM node:alpine

# Set the working directory to /client
WORKDIR /client

# Copy package.json and install dependencies
COPY ./package.json /client
RUN npm install

# Copy the rest of your app's source code from your host to your image filesystem.
COPY ./ /client

# Build the Next.js application
RUN npm run build

# Expose port 3008 on the container
EXPOSE 3008

# Start the Next.js app
CMD ["npm", "start"]