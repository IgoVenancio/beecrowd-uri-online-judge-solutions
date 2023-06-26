var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let idade
let somaIdades = 0
let countIdades = 0

do{
    idade = parseFloat(lines.shift())
    if(idade >= 0){
        somaIdades += idade
        countIdades++ 
    } 
    
}while(idade > 0)

console.log(`${(somaIdades/countIdades).toFixed(2)}`)