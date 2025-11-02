#!/usr/bin/node
const firstArg = process.argv[2];
const size = parseInt(firstArg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let row = 0;
  while (row < size) {
    console.log('X'.repeat(size)); // use repeat to get the number of X we need to print instead of writing another loop
    row++;
  }
}
