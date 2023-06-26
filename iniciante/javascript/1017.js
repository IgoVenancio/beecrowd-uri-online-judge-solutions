var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let entrada1 = parseInt(lines.shift())
let entrada2 = parseInt(lines.shift())

const calcularLitros = function (a, b){
    return (a * b)/12
}

console.log(`${calcularLitros(entrada1, entrada2).toFixed(3)}`)