#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { process.stdout.write('X'); }
      console.log('');
    }
  }

  rotate () {
    const a = this.width;
    const b = this.height;
    this.width = b;
    this.height = a;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
module.exports = Square;
