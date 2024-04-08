#!/usr/bin/node
const size = Number(process.argv[2]);
if (!isNaN(size) && Number.isInteger(size)) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
