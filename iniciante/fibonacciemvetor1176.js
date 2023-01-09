var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function fibonacci(x){
    let fibo = []
    let a = 0
    let b = 1

    if(x === 0){
        return fibo[x] = x
    }

    fibo[0] = 0

    for(let i = 1; i <= x; i++){
        fibo[i] = a + b
        a = fibo[i]
        b = fibo[i - 1]
    }
    return fibo[x]
}

let entrada = parseInt(lines.shift())
let count = 0

while(count++ < entrada){
    let numero = parseInt(lines.shift())
    console.log(`Fib(${numero}) = ${fibonacci(numero)}`)
}
