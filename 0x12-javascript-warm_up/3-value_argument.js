#!/usr/bin/node
const count = process.argv.length;
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (count === 3) {
  console.log(process.argv[2]);
}
