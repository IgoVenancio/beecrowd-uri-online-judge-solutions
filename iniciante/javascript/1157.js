var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function divisores(a){
    for(let i = 1; i <= a; i++){
        if(a % i === 0)
            console.log(i)
    }
}

let x = parseInt(lines.shift())

divisores(x)