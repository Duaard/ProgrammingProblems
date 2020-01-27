'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
  inputString += inputStdin;
});

process.stdin.on('end', _ => {
  inputString = inputString
    .replace(/\s*$/, '')
    .split('\n')
    .map(str => str.replace(/\s*$/, ''));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function getInverse(num) {
  // Convert num to string then to array
  num = [...`${num}`];
  let inverseArr = [];
  num.map(x => {
    inverseArr.push(x);
  });
  let inverse = '';
  while (inverseArr.length > 0) {
    inverse = inverse.concat(inverseArr.pop());
  }
  return parseInt(inverse);
}

// Complete the beautifulDays function below.
function beautifulDays(i, j, k) {
  let days = 0;
  for (let day = i; day <= j; day++) {
    if (Math.abs(day - getInverse(day)) % k == 0) days++;
  }
  return days;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const ijk = readLine().split(' ');

  const i = parseInt(ijk[0], 10);

  const j = parseInt(ijk[1], 10);

  const k = parseInt(ijk[2], 10);

  let result = beautifulDays(i, j, k);

  ws.write(result + '\n');

  ws.end();
}
