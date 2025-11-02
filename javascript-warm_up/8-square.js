#!/usr/bin/node
const firstArg = process.argv[2];
const count = parseInt(firstArg);

if (isNaN(count)) {
  console.log('Missing size');
} else {
  let current = 0;
  while (count < current) {
    console.log('C is fun');
    current++;
  }
}
