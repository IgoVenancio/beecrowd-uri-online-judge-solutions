var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let countEntradas = 0
let countCobaias = 0
let countCoelhos = 0
let countRatos = 0
let countSapos = 0
let percentCoelhos
let percentRatos
let percentSapos

let qtdEntrada = parseInt(lines.shift())

while(countEntradas++ < qtdEntrada){
    let entradas = lines.shift().split(' ')
    if(entradas[1].replace('\r', '') === 'C')
        countCoelhos += parseInt(entradas[0])
    if(entradas[1].replace('\r', '') === 'R')
        countRatos += parseInt(entradas[0])
    if(entradas[1].replace('\r', '') === 'S')
        countSapos += parseInt(entradas[0])
}

countCobaias = countCoelhos + countRatos + countSapos
percentCoelhos = (countCoelhos * 100)/countCobaias
percentRatos = (countRatos * 100) / countCobaias
percentSapos = (countSapos * 100) / countCobaias


console.log(`Total: ${countCobaias} cobaias`)
console.log(`Total de coelhos: ${countCoelhos}`)
console.log(`Total de ratos: ${countRatos}`)
console.log(`Total de sapos: ${countSapos}`)
console.log(`Percentual de coelhos: ${percentCoelhos.toFixed(2)} %`)
console.log(`Percentual de ratos: ${percentRatos.toFixed(2)} %`)
console.log(`Percentual de sapos: ${percentSapos.toFixed(2)} %`)





