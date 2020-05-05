#!/usr/bin/node
const array = process.argv.slice(2).sort(function (a, b) { return a - b });
const aLength = array.length;
if (aLength <= 1) {
  console.log(0);
} else {
  console.log(array[aLength - 2]);
}
