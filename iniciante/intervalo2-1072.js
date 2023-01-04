var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let qtdEntradas = parseInt(lines.shift())
let countEntrada = 0
let dentro = 0
let fora = 0
while(countEntrada++ < qtdEntradas){
    let entrada = parseInt(lines.shift())
    if (entrada >= 10 && entrada <= 20){
        dentro++
    }else{
        fora++
    }
}

console.log(`${dentro} in`)
console.log(`${fora} out`)
