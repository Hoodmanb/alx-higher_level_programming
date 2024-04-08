#!/usr/bin/node

function add (a, b) {
  a = Number(process.argv[2]);
  b = Number(process.argv[3]);
  return console.log(a + b);
}
add();
