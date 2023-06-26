var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let countEntradas = 0
let countPares = 0

while(countEntradas++ < 5){
    let entrada = parseInt(lines.shift())
    if(entrada % 2 ===0){
        countPares++
    }
}

console.log(`${countPares} valores pares`)