var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let countEntradas = 0
let countPositivos = 0
let somaPositivos = 0

while(countEntradas++ < 6){
    let entrada = parseFloat(lines.shift())
    if(entrada > 0){
        countPositivos++
        somaPositivos += entrada
    }
}

console.log(`${countPositivos} valores positivos`)
console.log((somaPositivos/countPositivos).toFixed(1))

