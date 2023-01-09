var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let count = 0

while(count++ < 100){
    let numero = parseFloat(lines.shift())
    if(numero <= 10)
        console.log(`A[${count - 1}] = ${numero.toFixed(1)}`)
}
