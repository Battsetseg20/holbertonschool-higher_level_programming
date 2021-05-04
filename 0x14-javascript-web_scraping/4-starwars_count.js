#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const filmC = films[i].characters;
      for (const n in filmC) {
        if (filmC[n].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
