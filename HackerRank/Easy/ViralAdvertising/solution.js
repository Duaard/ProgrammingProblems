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

function recursive(n, cumulative) {
  if (n == 1) {
    return 2;
  } else if (cumulative) {
    return Math.floor((recursive(n - 1) * 3) / 2) + recursive(n - 1, true);
  } else {
    return Math.floor((recursive(n - 1) * 3) / 2);
  }
}

// Complete the viralAdvertising function below.
function viralAdvertising(n) {
  return recursive(n, true);
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine(), 10);

  let result = viralAdvertising(n);

  ws.write(result + '\n');

  ws.end();
}
