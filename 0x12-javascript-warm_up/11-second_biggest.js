#!/usr/bin/node
const array = [...new Set(process.argv.slice(2))];
const aLength = array.length;
if (aLength <= 1) {
  console.log('0');
} else {
  console.log(array.sort()[array.length - 2]);
}
