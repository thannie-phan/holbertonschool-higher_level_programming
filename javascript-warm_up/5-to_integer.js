#!/usr/bin/node
const firstArg = process.argv[2];

// convert firstArg from str to num and store in convertedNumber
const convertedNumber = parseInt(firstArg);

// if convertedNumber isNan aka is not a number
if (isNaN(convertedNumber)) {
    console.log('Not a number');
} else {
    console.log(`My number: ${convertedNumber}`);
}
