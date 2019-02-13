#!/usr/bin/node
// Prints the addition of two numbers

function add (a, b) {
  console.log(a + b);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

add(a, b);
