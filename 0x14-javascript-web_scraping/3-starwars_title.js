#!/usr/bin/node
// Import request module
const request = require('request');

// Get the movie ID
const movieId = process.argv[2];

// Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make the GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
