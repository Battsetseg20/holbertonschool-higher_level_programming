#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArgs[0]; i++) {
    let square = '';
    for (let j = 0; j < myArgs[0]; j++) {
      square += 'X';
    } console.log(square);
  }
}
