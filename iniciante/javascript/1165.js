var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let testes = parseInt(lines.shift())

while(testes--){
    let numero = parseInt(lines.shift())
    let count = 1
    for(let i = 2; i <= numero; i++){
        if(numero % i === 0)
            count++
        if(count > 2){
            console.log(`${numero} nao eh primo`)
            break
        }    
    }
    if(count == 2)
        console.log(`${numero} eh primo`)
}