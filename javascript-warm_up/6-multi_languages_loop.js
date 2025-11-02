#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let index = 0; // create counter index and use let so value can change unlike const

while (index < languages.length) {
  console.log(languages[index]);
  index++;
}
