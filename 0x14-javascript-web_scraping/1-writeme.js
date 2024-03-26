#!/usr/bin/node
// writes a string to a file

const fs = require('fs');
if (process.argv.length > 3) {
  process.exit(1);
}

// Writes to file
fs.readFile(process.argv[2], process.argv[3], 'utf-8', x => {
  if (x) {
    console.log(x);
  }
});
