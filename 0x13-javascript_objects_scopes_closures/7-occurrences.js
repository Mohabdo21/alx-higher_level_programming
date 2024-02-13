#!/usr/bin/node

/**
 * This function counts the number of occurrences of a specific element in a list.
 *
 * @param {Array} list - The list in which to search.
 * @param {*} searchElement - The element to count occurrences of.
 * @returns {number} The number of occurrences of the search element in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
