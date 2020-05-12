#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const reqChar = /18\/$/;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    let numMovies = 0;
    const jsonObject = JSON.parse(body).results;
    if (jsonObject !== undefined) {
      for (let step = 0; step < jsonObject.length; step++) {
        jsonObject[step].characters.forEach(character => {
          if (character.search(reqChar) !== -1) {
            numMovies++;
          }
        });
      }
    }
    console.log(numMovies);
  }
});
