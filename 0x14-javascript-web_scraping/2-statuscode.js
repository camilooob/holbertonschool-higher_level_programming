#!/usr/bin/node
const Request = require('request');
Request.get(process.argv[2]).on('response', function (response) {
  console.log('code:', response.statusCode);
});
