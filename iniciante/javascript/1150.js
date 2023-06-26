var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let x = parseInt(lines.shift())
let z = parseInt(lines.shift())
let i = 0
let soma = 0

while(z <= x){
    z = parseInt(lines.shift())
}

do{
    i++
    soma += x
    x++
}while(soma < z)

console.log(i)