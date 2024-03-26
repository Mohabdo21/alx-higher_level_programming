#!/usr/bin/node
// Import filesystem module
const fs = require('fs');

// Get the file path and the string to write
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
