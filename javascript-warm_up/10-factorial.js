#!/usr/bin/node

function factorial (number) {
  if (isNaN(number) || number <= 1) { // if is not number or number is <= 1
    return 1;
  }
  return number * factorial(number - 1);
}

const input = parseInt(process.argv[2]);
console.log(factorial(input));
