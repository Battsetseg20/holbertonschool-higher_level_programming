#!/usr/bin/node
/* Write function that returns the number of occurrences in a list:
Prototype: exports.nbOccurences = function (list, searchElement)
*/
exports.nbOccurences = function (list, searchElement) {
  const countOccurences = list.reduce((nb, val) => (val === searchElement ? nb + 1 : nb), 0);
  return countOccurences;
};
