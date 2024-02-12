#!/usr/bin/node
/**
 * factorial - A Funcion returns a factorial of number given by CL arg
 * @param {number} n -  A number to calculate its factorial
 * @returns {number} - factorial of n
 */
function factorial (n) {
  if (!n || n < 2) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])));
