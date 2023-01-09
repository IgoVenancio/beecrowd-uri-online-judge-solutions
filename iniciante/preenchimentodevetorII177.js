var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift())
let count = 0

while(count < 1000 - 1 ){
    for(let i = 0; i < entrada && count < 1000; i++)
        console.log(`N[${count++}] = ${i}`)
}
