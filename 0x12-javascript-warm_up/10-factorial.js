#!/usr/bin/node
function fact (n) {
  if (n === 0) { return 1; } else { return n * fact(n - 1); }
}
const arg = Number(process.argv[2]);
if (!isNaN(arg) && Number.isInteger(arg)) {
  console.log(fact(arg));
} else {
  console.log(1);
}
