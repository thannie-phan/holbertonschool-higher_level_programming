#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number); // parseInt only works on a single string. for every num in arrays to be turned into int we need map(Number). if want to convert everything into string we use map(String)
  const sortedNumbers = numbers.sort((a, b) => b - a); // sort no from biggest to smallest
  console.log(sortedNumbers[1]); // sortedNumbers[0] is the biggest so [1] is second biggest
}
