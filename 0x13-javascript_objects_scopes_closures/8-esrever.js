#!/usr/bin/node

/**
 * This function returns the reversed version of a list.
 *
 * @param {Array} list - The list to be reversed.
 * @returns {Array} The reversed list.
 */
exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
