var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entradas = lines.shift().split(' ')
let count = 0
let soma = 0
let a = parseInt(entradas[count++])
let b = parseInt(entradas[count++])

do{
    if(b <= 0)
        b = parseInt(entradas[count++])
}while(b <= 0)

for(let i = 0 ; i <= b - 1; i++){
    soma += a
    a++
}

console.log(soma)
