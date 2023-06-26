var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

// function somaSimples(a, b){
//     return a + b
// }

let a = Number(lines.shift());
let b = Number(lines.shift());
const soma = (a,b) => a + b

console.log(`SOMA = ${soma(a, b)}`)