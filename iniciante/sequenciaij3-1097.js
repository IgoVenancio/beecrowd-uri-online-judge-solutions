var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let i
let j
let incremento = 8

for(i = 1, j = 7; i <= 9; j--){
    console.log(`I=${i} J=${j}`)
    if(j == (incremento - 3)){
        incremento += 2
        j = incremento
        i += 2
    }
}
