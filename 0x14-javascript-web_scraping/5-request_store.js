#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf-8', function (err, data) {
      if (err) { console.log(err); } else { console.log(data); }
    });
  }
});
