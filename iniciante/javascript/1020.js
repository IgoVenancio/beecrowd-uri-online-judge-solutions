var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift())

let ano = parseInt(entrada / 365)
entrada %= 365
let mes = parseInt(entrada / 30)
entrada %= 30
let dia = entrada

console.log(`${ano} ano(s)`)
console.log(`${mes} mes(es)`)
console.log(`${dia} dia(s)`)
