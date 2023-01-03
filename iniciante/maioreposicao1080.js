var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')


let countEntradas = 0
let maior = 0
let posicao = 0

while(countEntradas++ < 100){
    let entrada = parseInt(lines.shift())
    if(entrada > maior){
        maior = entrada
        posicao = countEntradas
    }
}

console.log(maior)
console.log(posicao)

