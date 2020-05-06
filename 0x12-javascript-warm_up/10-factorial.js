#!/usr/bin/node
const intRegex = /^[0-9]*?.[0-9]*$/;
const a = process.argv[2];

function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

if (intRegex.test(a)) {
  console.log(factorial(parseInt(a)));
} else {
  console.log(1);
}
