var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let a = Number(lines.shift());
let b = Number(lines.shift());
let c = Number(lines.shift());
let d = Number(lines.shift());
let  diferenca = (a, b, c, d) => (a * b - c * d)

console.log(`DIFERENCA = ${diferenca(a, b, c, d)}`)