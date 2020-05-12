#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + parseInt(process.argv[2]);

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
