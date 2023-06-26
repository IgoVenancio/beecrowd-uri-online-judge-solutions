var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let a = parseInt(lines.shift())
let b = parseInt(lines.shift())
let soma = 0

while(b <= 0){
    b = parseInt(lines.shift())
}
for(let i = 0 ; i <= b - 1; i++){
    soma += a
    a++
}

console.log(soma)
