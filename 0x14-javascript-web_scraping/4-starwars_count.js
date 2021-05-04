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
      const film_ch = films[i].characters;
      for (const n in film_ch) {
        if (film_ch[n].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
