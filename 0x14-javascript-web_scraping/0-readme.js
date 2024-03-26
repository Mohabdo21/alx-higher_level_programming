#!/usr/bin/node
// Import the filesystem module
const fs = require('fs');

// Get the file path from CL arg
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf8', (err, data) => {
  // If reading error occurred
  if (err) {
    console.log(err);
  } else {
    // Print file content
    console.log(data);
  }
});
