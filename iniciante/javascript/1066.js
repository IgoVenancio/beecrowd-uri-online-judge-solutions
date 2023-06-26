var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let countEntradas = 0
let countPares = 0
let countImpares = 0
let countNegativos = 0
let countPositivos = 0

while(countEntradas++ < 5){
    let entrada = parseInt(lines.shift())
    if(entrada % 2 === 0){
        countPares++
    }
    if(entrada % 2 !== 0){
        countImpares++
    }
    if(entrada > 0){
        countPositivos++
    }
    if(entrada < 0){
        countNegativos++
    }

}

console.log(`${countPares} valor(es) par(es)`)
console.log(`${countImpares} valor(es) impar(es)`)
console.log(`${countPositivos} valor(es) positivo(s)`)
console.log(`${countNegativos} valor(es) negativo(s)`)


