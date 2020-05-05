#!/usr/bin/node
const aLength = process.argv.slice(2).length;
const array = [...new Set(process.argv.slice(2))];
console.log(array)
if (aLength <= 1) {
  console.log('0');
} else {
  console.log(array.sort()[array.length - 2]);
}
