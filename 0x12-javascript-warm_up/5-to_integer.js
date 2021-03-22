#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) { // isNaN determines whether value is Not-A-Number
  console.log('Not a number');
} else {
  console.log('My number: ' + myArgs[0]);
}
