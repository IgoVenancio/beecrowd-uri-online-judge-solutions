var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let a = Number(lines.shift());
let b = Number(lines.shift());
const soma = (a,b) => a + b

console.log(`SOMA = ${soma(a, b)}`)
