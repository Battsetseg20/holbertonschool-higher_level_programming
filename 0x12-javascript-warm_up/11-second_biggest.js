#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const myArgs = process.argv.slice(2);
  const secondBig = myArgs.sort((a, b) => b - a)[1]; // sort backwards and get the second i
  console.log(secondBig);
}
