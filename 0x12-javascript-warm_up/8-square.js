#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let step = 0; step < size; step++) {
    console.log('X'.repeat(size));
  }
}
