#!/usr/bin/node

const secondBiggestInteger = (arr = []) => {
  if (arr.length <= 1) {
    console.log(0);
    return;
  }

  const sortedArr = arr.sort((a, b) => b - a);

  console.log(sortedArr[1]);
};

const args = process.argv.slice(2).map(Number);
secondBiggestInteger(args);
