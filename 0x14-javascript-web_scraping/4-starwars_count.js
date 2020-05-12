#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charUrl = 'https://swapi-api.hbtn.io/api/people/' + '18/';

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    let numMovies = 0;
    const jsonObject = JSON.parse(body).results;
    if (jsonObject !== undefined){
      for (let step = 0; step < jsonObject.length; step++) {
        if (jsonObject[step].characters.includes(charUrl)) {
          numMovies++;
        }
      }
    }
    console.log(numMovies);
  }
});
