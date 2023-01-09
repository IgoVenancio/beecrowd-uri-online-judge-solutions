var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let count = 0

while(count++ < 10){
    let numero = parseInt(lines.shift())

    if(numero <= 0){
        console.log(`X[${count - 1}] = ${1}`)
    }else{
        console.log(`X[${count - 1}] = ${numero}`)
    }
}
