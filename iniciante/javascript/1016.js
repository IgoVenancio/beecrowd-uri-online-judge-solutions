var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let tempo = parseInt(lines.shift())
const calcularTempo = a => a * 2

console.log(`${calcularTempo(tempo)} minutos`)