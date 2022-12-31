var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function areaDoCirculo(raio){
    const pi = 3.14159
    return pi * Math.pow(raio,2)
}

let raio = Number(lines.shift());

console.log(`A=${areaDoCirculo(raio).toFixed(4)}`)
