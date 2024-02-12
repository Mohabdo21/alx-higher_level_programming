#!/usr/bin/node
/**
 * Function finds the second large number in an array
 * @param {Array} numbers - Array of Numbers
 * @returns {number} The second largest number in the array
 */

function findSecondLargest (numbers) {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (const num of numbers) {
    const n = Number(num);

    if (n > max) {
      [secondMax, max] = [max, n];
    } else if (n < max && n > secondMax) {
      secondMax = n;
    }
  }
  return secondMax;
}

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(findSecondLargest(args));
}
