#!/usr/bin/node

function add(a, b) {
  return console.log(parseInt(a) + parseInt(b));
}

let a = Number(process.argv[2]);
let b = Number(process.argv[3]);

add(a, b);
