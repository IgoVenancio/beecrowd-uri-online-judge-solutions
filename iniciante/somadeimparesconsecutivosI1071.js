var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numero1 = parseInt(lines.shift())
let numero2 = parseInt(lines.shift())
let somaImpar = 0

if (numero1 > numero2){
    numero2++
    while(numero2 < numero1){
        if (numero2 % 2 !== 0)
            somaImpar += numero2
            numero2++
    }
}else{
    numero1++
    while(numero1 < numero2){
        if (numero1 % 2 !== 0)
            somaImpar += numero1
        numero1++
    }
}

console.log(somaImpar)
