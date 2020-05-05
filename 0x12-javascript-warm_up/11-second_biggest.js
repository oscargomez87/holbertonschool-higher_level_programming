#!/usr/bin/node
const args = process.argv.slice(2);
const array = [...new Set(args)];
const aLength = array.length;
if (aLength <= 1) {
  console.log(0);
} else {
  console.log(array[aLength - 2]);
}
