FROM node:20

# workdir
WORKDIR /app

# install dependencies
COPY package*.json .
RUN npm install

# run server
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
