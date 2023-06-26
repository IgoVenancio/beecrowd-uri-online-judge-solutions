var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function somaParesConsecutivos(a, b = 5){
    let soma = 0
    let count = 0
    for(let i = a;count < b; i++ ){
        if(i % 2 === 0){
            soma += i
            count++
        }
    }
    return soma
}

do{
    var entrada = parseInt(lines.shift())
    if(entrada !== 0)
        console.log(somaParesConsecutivos(entrada))
}while(entrada != 0)