#!/usr/bin/node
const count = process.argv.length;
if (count === 2) {
	console.log("No argument");
}else if (count === 3) {
	console.log(process.argv[2]);
}
