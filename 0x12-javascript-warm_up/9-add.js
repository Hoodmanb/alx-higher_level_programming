#!/usr/bin/node

function add(a, b) {
  console.log(parseInt(a) + parseInt(b));
}

let a = process.argv[2];
let b = process.argv[3];

add(a, b);
