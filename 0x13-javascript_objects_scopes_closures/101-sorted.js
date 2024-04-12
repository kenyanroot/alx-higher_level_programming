#!/usr/bin/node
// Script that inverts a dictionary to group user IDs by their occurrence counts.

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).forEach(key => {
  const value = dict[key];
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(key);
});

console.log(newDict);
