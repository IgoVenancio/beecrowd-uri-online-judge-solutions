var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function fatorial(a){
    if(a == 1)
        return 1
    else{
        return a * fatorial(a - 1)
    }
}

let x = parseInt(lines.shift())

console.log(fatorial(x))
