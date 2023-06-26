var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let entrada = Number(lines.shift())

console.log('NOTAS:')
console.log(`${parseInt(entrada / 100)} nota (s) de R$ 100.00`)
entrada %= 100
console.log(`${parseInt(entrada / 50)} nota (s) de R$ 50.00`)
entrada %= 50
console.log(`${parseInt(entrada / 20)} nota (s) de R$ 20.00`)
entrada %= 20
console.log(`${parseInt(entrada / 10)} nota (s) de R$ 10.00`)
entrada %= 10
console.log(`${parseInt(entrada / 5)} nota (s) de R$ 5.00`)
entrada %= 5
console.log(`${parseInt(entrada / 2)} nota (s) de R$ 2.00`)
entrada %= 2
console.log('MOEDAS:')
console.log(`${parseInt(entrada / 1)} moeda (s) de R$ 1.00`)
entrada %= 1.00
console.log(`${parseInt(entrada / 0.50)} moeda (s) de R$ 0.50`)
entrada %= 0.50
console.log(`${parseInt(entrada / 0.25)} moeda (s) de R$ 0.25`)
entrada %= 0.25
console.log(`${parseInt(entrada / 0.10)} moeda (s) de R$ 0.10`)
entrada %= 0.10
console.log(`${parseInt(entrada / 0.05)} moeda (s) de R$ 0.05`)
entrada %= 0.05
console.log(`${(entrada / 0.01).toFixed(0)} moeda (s) de R$ 0.01`)
