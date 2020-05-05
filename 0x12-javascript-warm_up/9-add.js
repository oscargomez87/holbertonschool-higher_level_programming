#!/usr/bin/node
const firstNumber = parseInt(process.argv[2]);
const secondNumber = parseInt(process.argv[3]);
add(firstNumber, secondNumber);
function add (a, b) {
  console.log(a + b);
}
