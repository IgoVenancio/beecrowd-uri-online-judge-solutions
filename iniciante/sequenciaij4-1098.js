var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let i
let j
let contador = 1

for(i = 0, j = 1, contador; i <= 2; j++, contador++){
    if(Number.isInteger(j) || Number.isInteger(i)){
        console.log(`I=${i.toFixed(0)} J=${j.toFixed(0)}`)
    }else{
        console.log(`I=${i.toFixed(1)} J=${j.toFixed(1)}`)
    }
    
    if(contador == 3){
        i += 0.2
        j = 0 + i
        contador = 0
    }
}
