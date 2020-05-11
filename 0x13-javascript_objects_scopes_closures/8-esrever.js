#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  for (let step = list.length - 1; step >= 0; step--) {
    revList.push(list[step]);
  }
  return revList;
};
