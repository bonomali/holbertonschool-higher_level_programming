#!/usr/bin/node
// Prints the second biggest number in an array

let arr = [];

if (process.argv.length <= 3) {
  console.log('0');
} else {
  for (let count = 2; count < process.argv.length; count++) {
    arr.push(process.argv[count]);
  }
  arr.sort();
  arr.reverse();
  console.log(arr[1]);
}
