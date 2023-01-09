var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let count = 20
let saida = []

while(--count > -1){
    let numero = parseFloat(lines.shift())
    saida[count] = numero
}

for(let i = 0; i < saida.length; i++){
    console.log(`N[${i}] = ${saida[i]}`)
}
