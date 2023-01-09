var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function somaImparesConsecutivos(a, b){
    let soma = 0
    let count = 0

    for(let i = a; count < b; i++){
        if(i % 2 !== 0){
            soma += i
            count++
        }
    }
    return soma
}

let repeticoes = parseInt(lines.shift())
let countRepeticoes = 0

while(countRepeticoes++ < repeticoes){
    let entradas = lines.shift().split(' ')
    let a = parseInt(entradas[0])
    let b = parseInt(entradas[1].replace('\r',''))
    console.log(somaImparesConsecutivos(a, b))
}
