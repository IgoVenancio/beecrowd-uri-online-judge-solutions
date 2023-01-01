var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function consumo(a, b){
    return a / b
}

let entrada1 = parseInt(lines.shift())
let entrada2 = parseFloat(lines.shift())

console.log(`${consumo(entrada1, entrada2).toFixed(3)} km/l`)
