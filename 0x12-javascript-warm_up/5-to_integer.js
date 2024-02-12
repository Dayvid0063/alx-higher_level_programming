#!/usr/bin/node

// Convert the 1st cmd line arg to an int
const num = +process.argv[2];

// Check if the converted value is a valid number
if (!isNaN(num)) {
    console.log("My number:", num);
} else {
    console.log("Not a number");
}
