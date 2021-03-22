#!/usr/bin/node
function add (a, b) {
  return (isNaN(a) || isNaN(b) ? 'NaN' : Number(a) + Number(b));
}
console.log(add(process.argv[2], process.argv[3]));
