#!/usr/bin/node

const myVar = process.argv.slice(2);

if (myVar.length === 1) {
  console.log(myVar[0] + ' is undefined');
} else if (myVar.length > 1) {
  console.log(myVar[0] + ' is ' + myVar[1]);
} else {
  console.log('undefined is undefined');
}
