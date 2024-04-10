#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  
  charPrint (c) {
    let letter;
    if (c === undefined) {
      letter = 'X';
    }
    else {
      letter = 'C';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += letter;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
