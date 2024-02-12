#!/usr/bin/node

// Define module that exports an obj
module.exports = {
  // The method callDayv takes two param
  callDayv: function (v, theFunction) {
    // Loop v times
    for (let u = 0; u < v; u++) {
      // Execute the given function
      theFunction();
    }
  }
};
