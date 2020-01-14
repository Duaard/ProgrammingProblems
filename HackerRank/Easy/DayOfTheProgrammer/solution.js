'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function() {
  inputString = inputString.split('\n');

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function isLeapYear(year) {
  // Identifies if the year is of Julian calendar
  // Leap years are divisible by 4
  if (year >= 1700 && year <= 1917) {
    if (year % 4 == 0) {
      return true;
    }
  }
  // If the year is of Gregorian Calendar
  // Leap years are divisible by 400
  // or divisible by 4 and not 100
  else {
    if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
      return true;
    }
  }
  return false;
}

// Complete the dayOfProgrammer function below.
function dayOfProgrammer(year) {
  let daysPerMonth = [];
  for (let i = 0; i < 12; i++) {
    // February
    if (i == 1) {
      if (year == 1918) {
        daysPerMonth.push(15);
      } else if (isLeapYear(year)) {
        daysPerMonth.push(29);
      } else {
        daysPerMonth.push(28);
      }
    }
    // 31 days
    else if ((i < 7 && i % 2 == 0) || (i >= 7 && i % 2 != 0)) {
      daysPerMonth.push(31);
    }
    // 30 days
    else {
      daysPerMonth.push(30);
    }
  }
  // Find the 256th day of the given year
  let numOfDays = 0;
  let answer;
  for (let i = 0; i < 12; i++) {
    if (numOfDays + daysPerMonth[i] < 256) {
      numOfDays += daysPerMonth[i];
    } else {
      numOfDays = 256 - numOfDays;
      answer = numOfDays + '.0' + (i + 1) + '.' + year;
      break;
    }
  }
  return answer;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const year = parseInt(readLine().trim(), 10);

  const result = dayOfProgrammer(year);

  ws.write(result + '\n');

  ws.end();
}
