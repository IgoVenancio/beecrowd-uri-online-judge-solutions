var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function fatorial(a){
    if(a == 1)
        return 1
    else{
        return a * fatorial(a - 1)
    }
}

let x = parseInt(lines.shift())

console.log(fatorial(x))
