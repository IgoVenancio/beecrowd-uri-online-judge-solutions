var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let dividendo = parseFloat(lines.shift())
let count = 0
let divisor = 2.0
while(count < 100){
    console.log(`N[${count++}] = ${dividendo.toLocaleString('en-US', {minimumFractionDigits: 4, useGrouping: false })}`)
    dividendo /= divisor
}
