#!/usr/bin/node
let i;
const intRegex = /^[0-9]*.[0-9]*$/;

if (intRegex.test(process.argv[2])) {
  for (i = 0; i <= (parseInt(process.argv[2]) - 1); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
