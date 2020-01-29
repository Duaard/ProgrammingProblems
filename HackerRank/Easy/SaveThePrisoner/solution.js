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

// Complete the saveThePrisoner function below.
function saveThePrisoner(n, m, s) {
  //  Get the modulo to know the minimum increase
  let mod = m % n;

  if (mod == 0) {
    // If mod is 0, set it to max number
    mod = n;
  }

  // Let the seat number be the mod + starting position
  // -1 to accomodate the starting position at 1 not 0
  let seatnumber = s + mod - 1;

  if (seatnumber % n == 0) {
    // The seatnumber is divisible by n meaning it is n
    seatnumber = n;
  } else {
    // Cap the seat number by number of prisoners
    seatnumber = seatnumber % n;
  }

  return seatnumber;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const t = parseInt(readLine(), 10);

  for (let tItr = 0; tItr < t; tItr++) {
    const nms = readLine().split(' ');

    const n = parseInt(nms[0], 10);

    const m = parseInt(nms[1], 10);

    const s = parseInt(nms[2], 10);

    let result = saveThePrisoner(n, m, s);

    ws.write(result + '\n');
  }

  ws.end();
}
