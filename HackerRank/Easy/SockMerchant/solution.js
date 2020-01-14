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

// Complete the sockMerchant function below.
function sockMerchant(n, ar) {
  // Use a hash to track occurence
  let sockMap = {};
  ar.map(sock => {
    // If the sock is already in the map
    // add a number of occurence
    if (sock in sockMap) {
      sockMap[sock]++;
    }
    // If the sock isn't in the map
    // create an instance of it
    else {
      sockMap[sock] = 1;
    }
  });

  let pair = 0;
  // For every instance of sock that has more than 2
  // occurence, divide by and floor to get the total pairs
  for (const key of Object.keys(sockMap)) {
    if (sockMap[key] >= 2) {
      pair += Math.floor(sockMap[key] / 2);
    }
  }

  return pair;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine(), 10);

  const ar = readLine()
    .split(' ')
    .map(arTemp => parseInt(arTemp, 10));

  let result = sockMerchant(n, ar);

  ws.write(result + '\n');

  ws.end();
}
