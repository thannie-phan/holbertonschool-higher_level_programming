#!/usr/bin/node
// process.argv contains all args. use slice 2 to ignore the first 2 items node and script
const userArguments = process.argv.slice(2);

console.log(`${userArguments[0]} is ${userArguments[1]}`);
