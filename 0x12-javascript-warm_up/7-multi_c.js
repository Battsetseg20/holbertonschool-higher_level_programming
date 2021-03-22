#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) {
  console.log('Missins number of occurencies');
} else {
  let i = 0;
  for (i = 0; i < myArgs[0]; i++) {
    console.log('C is fun');
  }
}
