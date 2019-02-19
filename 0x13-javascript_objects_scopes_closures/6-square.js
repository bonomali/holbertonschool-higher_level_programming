#!/usr/bin/node
// Contains the class Square

const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
