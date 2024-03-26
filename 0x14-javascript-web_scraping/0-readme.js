#!/usr/bin/node
//reads and prints the content of a file

const fs = require('fs');
if (process.argv.length <= 2) {
    process.exit(1);
}

// Reads file
fs.readFile(process.argv[2], (err, data) => {
    if (err) {
        console.error(err);
    } else {
        console.log(data.toString('utf-8'));
    }
});
