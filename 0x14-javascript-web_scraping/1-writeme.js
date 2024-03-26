#!/usr/bin/node
// writes a string to a file

const fs = require('fs');
if (process.argv.length > 3) {
  process.exit(1);
}

// Writes to file
fs.writeFile(process.argv[2], process.argv[3], x => {
  if (x) console.log(x);
});
