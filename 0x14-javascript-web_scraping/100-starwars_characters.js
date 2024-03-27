#!/usr/bin/node
// Import request module
const request = require('request');

// Get the movie ID from CL args
const movieID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make the GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    characterUrls.forEach((characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
