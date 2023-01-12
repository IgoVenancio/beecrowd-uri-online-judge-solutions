var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let posicao
let menorValor
let entrada = parseInt(lines.shift())
let valor = lines.shift().split(' ')

for(let i = 0; i < entrada; i++){
    if (menorValor == undefined || parseInt(valor[i]) < menorValor){
        menorValor = parseInt(valor[i])
        posicao = i
    }
}
    
console.log(`Menor valor: ${menorValor}`)
console.log(`Posicao: ${posicao}`)
