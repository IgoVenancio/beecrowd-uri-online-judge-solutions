var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada1 = lines.shift().split(' ')
let entrada2 = lines.shift().split(' ')

const valorAPagar = (array1, array2) => (Number(array1[1]) * Number(array1[2]) + Number(array2[1]) * Number(array2[2]))

console.log(`VALOR A PAGAR: R$ ${valorAPagar(entrada1, entrada2).toFixed(2)}`)
