#!/usr/bin/node
// Contains the class Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  // Instance method that prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
