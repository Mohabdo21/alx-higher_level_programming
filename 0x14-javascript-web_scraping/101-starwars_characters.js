#!/usr/bin/node
// Import needed modules
const { promisify } = require('util');
const request = require('request');

// Convert request.get to a function that returns a promise
const getRequest = promisify(request.get);

async function getMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  try {
    const response = await getRequest(url);
    const movie = JSON.parse(response.body);
    const characterUrls = movie.characters;

    // Use async/await for cleaner Promise handling
    const characters = await Promise.all(
      characterUrls.map((characterUrl) =>
        getRequest(characterUrl).then((response) => JSON.parse(response.body))
      )
    );

    characters.forEach((character) => console.log(character.name));
  } catch (error) {
    console.error(error);
  }
}

const movieId = process.argv[2];

if (movieId) {
  getMovieCharacters(movieId);
} else {
  console.error('Please provide a movie ID as an argument.');
}
