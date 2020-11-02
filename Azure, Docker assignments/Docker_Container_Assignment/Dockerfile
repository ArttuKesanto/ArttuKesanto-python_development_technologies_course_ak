FROM node:12-slim
# Can leave this dir.
WORKDIR /usr/src/app
# Could be without the port.
ENV PORT=80 

COPY package*.json ./

RUN npm install

COPY . ./

EXPOSE 80

CMD [ "node", "index.js" ]