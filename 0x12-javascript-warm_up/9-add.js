#!/usr/bin/node

const a = process.argv[2];
const b = process.argv[3];
let c;
const suma = (a, b) => {
  c = parseInt(a) + parseInt(b);
  console.log(c);
};

suma(a, b);
