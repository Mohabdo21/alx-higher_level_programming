#!/usr/bin/node
// Import request module
const request = require('request');

// Get the API URL from CL args
const apiUrl = process.argv[2];

// Define the character ID for Wedge Antilles
const wedgeAntillesId = '18';

// Make the GET request
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Count the number of the movies where character ID is present
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes(`/people/${wedgeAntillesId}`)) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
