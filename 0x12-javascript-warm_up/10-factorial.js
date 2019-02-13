#!/usr/bin/node
// Prints a factorial

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else if (num < 0) {
    return -1;
  }
  return (num * factorial(num - 1));
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));
