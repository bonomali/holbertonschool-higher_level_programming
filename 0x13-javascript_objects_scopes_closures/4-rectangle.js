#!/usr/bin/node
// Contains the class Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instance method that prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Instance method that exchanges the width and the height of the rectangle
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method that multiplies the width and the height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
