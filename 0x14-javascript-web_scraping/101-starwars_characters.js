#!/usr/bin/node
// Import modules
const request = require('request');
const util = require('util');

// Convert request.get to a function returns a promise
const getRequest = util.promisify(request.get);

// Get movie ID from CL args
const movieID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make the GET request
getRequest(url)
  .then((response) => {
    const movie = JSON.parse(response.body);
    const characterUrls = movie.characters;

    // Create array of promises
    const promises = characterUrls.map((characterUrl) =>
      getRequest(characterUrl)
    );

    // Wait for all promises to resolve
    return Promise.all(promises);
  })
  .then((responses) => {
    responses.forEach((response) => {
      const character = JSON.parse(response.body);
      console.log(character.name);
    });
  })
  .catch((error) => {
    console.log(error);
  });
