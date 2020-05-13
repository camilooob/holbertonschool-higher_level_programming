#!/usr/bin/node
const fs = require('fs');
fs.writeFileSync(process.argv[2], process.argv[3], 'utf-8', function (err, data) {
  if (err) { console.log(err); } else { console.log(data); }
});
