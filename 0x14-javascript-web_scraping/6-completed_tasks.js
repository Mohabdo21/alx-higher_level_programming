#!/usr/bin/node
// Import request module
const request = require('request');

// Get API URL from CL args
const apiUrl = process.argv[2];

// Make GET request
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};
    for (let i = 0; i < tasks.length; i++) {
      const task = tasks[i];
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    }
    console.log(completedTasksByUser);
  }
});
