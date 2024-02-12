#!/usr/bin/node
/**
 * add - Function add two numbers
 *
 * @param {number} a - First CL arg
 * @param {number} b - Second CL arg
 * @returns {number} - The Sum of Args
 */
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
