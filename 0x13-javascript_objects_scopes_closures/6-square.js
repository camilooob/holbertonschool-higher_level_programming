#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { process.stdout.write(c); }
      console.log('');
    }
  }
}

module.exports = Square;
