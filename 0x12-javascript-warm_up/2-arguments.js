#!/usr/bin/node
const psNumber = process.argv.length;
if (psNumber <= 2) {
  console.log('No argument');
} else if (psNumber === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
