var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

function distanciaEntreDoisPontos(a, b, c, d){
    return Math.sqrt(Math.pow((c - a), 2) + Math.pow((d - b), 2))
}

let entrada1 = lines.shift().split(' ')
let entrada2 = lines.shift().split(' ')

console.log(`${distanciaEntreDoisPontos(parseFloat(entrada1[0]), parseFloat(entrada1[1]), parseFloat(entrada2[0]), parseFloat(entrada2[1])).toFixed(4)}`)
