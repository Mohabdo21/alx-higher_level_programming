#!/usr/bin/node
// Import request and filesystem
const request = require('request');
const fs = require('fs');

// Get the URL and the file path from CL args
const url = process.argv[2];
const filePath = process.argv[3];

// Make the GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
