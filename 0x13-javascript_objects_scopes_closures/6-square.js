#!/usr/bin/node
const pSquare = require('./5-square');

module.exports = class Square extends pSquare {
  charPrint (c) {
    c = !c ? 'X' : c;
    for (let step = 0; step < this.width; step++) {
      console.log(String(c).repeat(this.width));
    }
  }
};
