#!/usr/bin/node
// Import request module
const request = require('request');

// Get the URL from CL args
const url = process.argv[2];

// Make a GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Print the status code
    console.log('code:', response.statusCode);
  }
});
