#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOcurrences = 0;
  for (let step = 0; step < list.length; step++)
  {
    if (list[step] === searchElement) {
      numOcurrences += 1;
    }
  }
  return numOcurrences;
}
