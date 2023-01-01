var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = lines.shift().split(' ')
let a = parseInt(entrada[0])
let b = parseInt(entrada[1])

const horas = function(a, b){
    if (a >= b){
        return 24 - a + b
    }else{
        return b - a
    }
}

console.log(`O JOGO DUROU ${horas(a, b)} HORA(S)`)
