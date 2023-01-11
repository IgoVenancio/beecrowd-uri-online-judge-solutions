var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entradas = parseInt(lines.shift())
let count = 0
let numeroAtual
let numeroAnterior

numeroAnterior = parseInt(lines.shift())
count++
entradas--
    while (entradas--) {
        numeroAtual = parseInt(lines.shift())
        if(numeroAtual !== numeroAnterior)
            count++
        numeroAnterior = numeroAtual
    }
console.log(count)
