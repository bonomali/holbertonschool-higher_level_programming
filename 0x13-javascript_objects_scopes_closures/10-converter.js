#!/usr/bin/node
// Converts a number from base 10 to another base passed as an argument

exports.converter = function (base) {
  function convert (i) {
    return i.toString(base);
  }
  return convert;
};
