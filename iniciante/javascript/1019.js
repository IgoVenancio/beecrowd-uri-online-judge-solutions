var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift())
let horas = parseInt(entrada / 3600)
entrada %= 3600
let minutos = parseInt(entrada / 60)
entrada %= 60
let segundos = entrada
console.log(`${horas}:${minutos}:${segundos}`)
