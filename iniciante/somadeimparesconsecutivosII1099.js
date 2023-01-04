var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function imprimirSomaImparesConsecutivos(a, b){
    let maior
    let menor
    let soma = 0
    if(a <= b){
        menor = a
        maior = b
        for(let i = ++menor; i < maior; i++){
            if(i % 2 !== 0)
                soma += i
        }
    }else{
        menor = b
        maior = a
        for(let i = ++menor; i < maior; i++){
            if(i % 2 !== 0)
                soma += i
        }
    }
    console.log(soma)
}

let countEntradas = 0
let qtdEntradas = parseInt(lines.shift())

while(countEntradas++ < qtdEntradas){
    let entradas = lines.shift().split(' ')
    let entrada1 = parseInt(entradas[0])
    let entrada2 = parseInt(entradas[1].replace('\r',''))
    imprimirSomaImparesConsecutivos(entrada1,entrada2)
}
