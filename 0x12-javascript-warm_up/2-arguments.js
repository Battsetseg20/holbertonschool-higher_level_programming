#!/usr/bin/node
const myArgs = process.argv.length;
console.log(myArgs === 2 ? 'No argument' : myArgs === 3 ? 'Argument found' : 'Arguments found');
/*
if (myArgs === 2)
    console.log('No argument')
else if (myArgs === 3)
    console.log('Argument found')
else if (myArgs > 3)
    console.log('Arguments found')
*/
