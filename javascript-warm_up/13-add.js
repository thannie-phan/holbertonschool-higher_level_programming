#!/usr/bin/node

function add (a, b) {
  return a + b;
}

module.exports.add = add; // makes the add function visible outside this file.
