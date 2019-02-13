#!/usr/bin/node
// Prints "c is fun" x number of times

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
