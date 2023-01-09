var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let testes = parseInt(lines.shift())

while(testes--){
    let numero = parseInt(lines.shift())
    let soma = 0
    for(let i = 1; i < numero; i++){
        if(numero % i === 0)
            soma += i
    }
    if(soma == numero){
        console.log(`${numero} eh perfeito`)
    }else{
        console.log(`${numero} nao eh perfeito`)

    }
}
