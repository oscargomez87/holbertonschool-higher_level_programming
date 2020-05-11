#!/usr/bin/node
const pSquare = require('./5-square');

module.exports = class Square extends pSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    c = !c ? 'X': c;
    for (let step = 0; step < this.size; step++) {
      console.log(String(c).repeat(this.size));
    }
  }
};
