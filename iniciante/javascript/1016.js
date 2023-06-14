var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let tempo = parseInt(lines.shift())
const calcularTempo = a => a * 2

console.log(`${calcularTempo(tempo)} minutos`)
