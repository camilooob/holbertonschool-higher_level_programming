#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const newDict = {};
request.get(url, function (err, response, body) {
  if (err == null) {
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (newDict[todos[i].userId] === undefined) { newDict[todos[i].userId] = 0; }
        newDict[todos[i].userId] += 1;
      }
    }
    console.log(newDict);
  }
});
