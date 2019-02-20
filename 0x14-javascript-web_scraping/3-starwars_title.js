#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches
// the given integer
const request = require('request');

const url = 'http://swapi.co/api/films/' + process.argv[2] + '/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
