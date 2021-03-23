#!/usr/bin/node
/* Write a script that imports an array and computes a new array.
You must use a map.
*/
const list = require('./100-data.js').list; // import list from file
console.log(list); // print initial list
const list1 = list.map((x, i) => { return x * i; }); // value * index in the list
console.log(list1);
