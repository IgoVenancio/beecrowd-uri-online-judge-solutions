var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let soma = 0
let j = 1

for(let i = 1; i <= 100; i+=2){
    soma +=(1/i)
}

console.log(soma.toFixed(2))