#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let step = 0; step < times; step++) {
    console.log('C is fun');
  }
}
