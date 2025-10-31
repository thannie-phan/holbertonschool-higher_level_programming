#!/usr/bin/node
// process.argv contains all args. use slice 2 to ignore the first 2 items node and script
const userArguments = process.argv.slice(2);

if (userArguments.length === 0) {
  console.log('No argument');
} else if (userArguments.length === 1) {
  console.log(userArguments);
} else {
  console.log('Arguments found');
}
