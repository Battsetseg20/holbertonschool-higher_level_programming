#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle: */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { // if w and h equal to or (-), create en empty object
      this.width = w; // initialing instnace attributes with value of w and h
      this.height = h;
    }
  }

  print () { // instance method that prints rectangle with character 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () { // instance method that exchanges width and height
    [this.height, this.width] = [this.width, this.height]; // or use temp var
  }

  double () { // instance method that doubles size
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle; // export the module Rectangle
