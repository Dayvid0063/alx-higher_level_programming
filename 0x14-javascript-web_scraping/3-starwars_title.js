#!/usr/bin/node
// Prints the title of a Star Wars movie
const request = require('request');
const link = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(link + id, (x, body) => {
  if (x) {
    console.log(x);
  } else {
    console.log(JSON.parse(body).title);
  }
});
