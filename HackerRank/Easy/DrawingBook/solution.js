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
    .trim()
    .split('\n')
    .map(str => str.trim());

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the pageCount function below.
 */
function pageCount(n, p) {
  let result;

  // Get the page number and divide the number of pages by 2
  // If more than half, start from the back
  if (p >= Math.floor(n / 2) + 1) {
    // Divide both by 2 and get the difference
    result = Math.floor(n / 2) - Math.floor(p / 2);
  }
  // else start from the front
  else {
    result = Math.floor(p / 2);
  }
  return result;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine(), 10);

  const p = parseInt(readLine(), 10);

  let result = pageCount(n, p);

  ws.write(result + '\n');

  ws.end();
}
