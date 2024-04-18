#!/usr/bin/node
const size = process.argv[2];
if (!size || isNaN(size)) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  let row = '';
  for (let y = 0; y < size; y++) {
    row += 'X';
  }
  console.log(row);
}
