#!/usr/bin/node
/* Write a function that returns the reversed version of a list:
Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/
exports.esrever = function (list) {
  const rev = list.map(list.pop, [...list]);
  return rev;
};
