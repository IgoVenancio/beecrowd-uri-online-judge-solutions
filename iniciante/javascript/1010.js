var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var entrada1 = lines.shift().split(' ')
var entrada2 = lines.shift().split(' ')

var valorAPagar = parseInt(entrada1[1]) * parseFloat(entrada1[2]) + parseInt(entrada2[1]) * parseFloat(entrada2[2])

console.log(`VALOR A PAGAR: R$ ${valorAPagar.toFixed(2)}`)
