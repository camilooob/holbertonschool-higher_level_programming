#!/usr/bin/node
const fs = require('fs');
const text1 = fs.readFileSync(process.argv[2], 'utf8');
const text2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], text1 + text2, 'utf-8');
