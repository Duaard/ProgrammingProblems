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

// Complete the countingValleys function below.
function countingValleys(n, s) {
  let valleyCount = 0;
  let altitude = 0;

  let charArray = [...s];

  charArray.forEach(step => {
    if (step == 'U') {
      altitude++;
    } else {
      altitude--;
    }
    // If the altitude is 0 and the last step was going up
    // Increase valleyCount by 1
    if (altitude == 0 && step == 'U') {
      valleyCount++;
    }
  });

  return valleyCount;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine(), 10);

  const s = readLine();

  let result = countingValleys(n, s);

  ws.write(result + '\n');

  ws.end();
}
