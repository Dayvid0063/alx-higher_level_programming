#!/usr/bin/node
// Prints all characters of a Star Wars movie:
const request = require('request');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(link, (x, response, body) => {
  if (x) {
    console.log(x);
  } else {
    const characters = JSON.parse(body).characters;

    for (const char of characters) {
      request.get(char, (x, response, body) => {
        if (x) {
          console.log(x);
        } else {
          const info = JSON.parse(body);
          console.log(info.name);
        }
      });
    }
  }
});
