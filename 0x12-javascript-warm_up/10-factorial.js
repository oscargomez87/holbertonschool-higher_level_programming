#!/usr/bin/node
const factNumber = parseInt(process.argv[2]);
if (isNaN(factNumber)) {
  console.log(1);
} else {
  console.log(factorial(factNumber));
}
function factorial (a) {
  if (a > 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}
