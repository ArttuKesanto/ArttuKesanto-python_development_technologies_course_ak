FROM node:12-slim

WORKDIR /usr/src/app
# Could be without the port.
ENV PORT=80 

COPY package*.json ./

RUN npm install

COPY . ./

EXPOSE 80

CMD [ "node", "index.js" ]