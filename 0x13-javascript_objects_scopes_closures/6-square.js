#!/usr/bin/node
const pSquare = require('./5-square');

module.exports = class Square extends pSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let step = 0; step < this.size; step++) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
