#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches
// the given integer
const request = require('request');
let i = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let result = JSON.parse(body).results;
  for (let movie of result) {
    for (let character of movie.characters) {
      if (character.endsWith('18/')) {
        i++;
      }
    }
  }
  console.log(i);
});
