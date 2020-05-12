#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const charUrl = 'https://swapi-api.hbtn.io/api/people/' + process.argv[2] + '/';

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    let numMovies = 0;
    const jsonObject = JSON.parse(body).results;
    for (let step = 0; step < jsonObject.length; step++) {
      if (jsonObject[step].characters.includes(charUrl)) {
        numMovies++;
      }
    }
    console.log(numMovies);
  }
});
