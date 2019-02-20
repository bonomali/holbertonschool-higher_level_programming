#!/usr/bin/node
// Computes the number of tasks completed by user id
const request = require('request');
let endResult = {};

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let result = JSON.parse(body);
  for (let item of result) {
    if (item.completed === true) {
      if (item.userId in endResult) {
        endResult[item.userId] = endResult[item.userId] + 1;
      } else {
        endResult[item.userId] = 1;
      }
    }
  }
  console.log(endResult);
});
