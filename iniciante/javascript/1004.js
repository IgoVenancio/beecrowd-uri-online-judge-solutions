var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let a = Number(lines.shift());
let b = Number(lines.shift());
let  produto = (a,b) => a * b

console.log(`PROD = ${produto(a, b)}`)