#!/usr/bin/node
/* class Square that defines a square and inherits from Rectangle of 4-rectangle.js */

class Square extends require('./4-rectangle.js') {
  constructor (size) { // Square constructor takes 1 argument
    super(size, size); // constructor of Rectangle called by super()
  }
}

module.exports = Square; // export the module
