var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let entrada = lines.shift().split(' ')
let valores = [0.0, 4.00, 4.50, 5.00, 2.00, 1.50]

console.log(`Total: R$ ${(valores[parseInt(entrada[0])] * entrada[1]).toFixed(2)}`)
