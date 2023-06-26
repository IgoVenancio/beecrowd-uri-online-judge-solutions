var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let qtdEntradas = parseInt(lines.shift())
let countEntrada = 0
let dado1
let dado2

while(countEntrada < qtdEntradas){
    let entrada = parseInt(lines.shift())
    if(entrada === 0){
        console.log('NULL')
    }else{
        if(entrada % 2 === 0){
            dado1 = 'EVEN'
        }else{
            dado1 = 'ODD'
        }
        if(entrada > 0){
            dado2 = 'POSITIVE'
        }else{
            dado2 = 'NEGATIVE'
        }

        console.log(`${dado1} ${dado2}`)    

    }
    countEntrada++
    
}




