#!/usr/bin/node
// Prints a square

const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
}
for (let count = 0; count < size; count++) {
  console.log('X'.repeat(size));
}
