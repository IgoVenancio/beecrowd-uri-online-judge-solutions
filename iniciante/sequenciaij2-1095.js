var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let i
let j
for(i = 1, j = 7; i <= 9; j--){
    console.log(`I=${i} J=${j}`)
    if(j == 5){
        j = 8
        i += 2
    }
}
