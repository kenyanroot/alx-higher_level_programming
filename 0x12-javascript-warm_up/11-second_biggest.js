#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let nums = process.argv.slice(2).map(Number); // Convert arguments to numbers
  nums = nums.sort((a, b) => a - b); // Sort numbers in ascending order
  console.log(nums[nums.length - 2]); // Output the second largest number
}
