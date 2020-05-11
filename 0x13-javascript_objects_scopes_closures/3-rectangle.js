#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let step = 0; step < this.height; step++) {
      console.log('X'.repeat(this.width));
    }
  }
};
