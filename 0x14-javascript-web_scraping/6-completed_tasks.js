#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const comTasks = {};
    const bodyJSON = JSON.parse(body);
    for (let step = 0; step < bodyJSON.length; step++) {
      if (bodyJSON[step].completed) {
        const key = bodyJSON[step].userId;
        if (isNaN(comTasks[key])) {
          comTasks[key] = 1;
        } else {
          comTasks[key] = comTasks[key] + 1;
        }
      }
    }
    console.log(comTasks);
  }
});
