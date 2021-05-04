#!/usr/bin/node
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});

/* const server = http.createServer();
server.on('request', (request, response) => {
  ...
}); */
