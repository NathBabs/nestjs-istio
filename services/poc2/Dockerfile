FROM node:14.17.6-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN  npm run build

EXPOSE 3000

ENTRYPOINT [ “node”, “dist/main.js” ]