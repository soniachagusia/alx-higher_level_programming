#!/usr/bin/node
const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const contentOfFile1 = fs.readFileSync(sourceFilePath1, 'utf8');
const contentOfFile2 = fs.readFileSync(sourceFilePath2, 'utf-8');

fs.writeFileSync(destinationFilePath, contentOfFile1 + contentOfFile2);
