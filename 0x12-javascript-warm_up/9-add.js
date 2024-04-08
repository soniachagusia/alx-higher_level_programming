#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const arg = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);
if (!isNaN(arg) && Number.isInteger(arg) && !isNaN(arg2) && Number.isInteger(arg2)) {
  console.log(add(arg, arg2));
} else {
  console.log('NaN');
}
