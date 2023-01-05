var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let a = parseInt(lines.shift().replace('\r',''))
let alcool = 0
let gasolina = 0
let diesel = 0

while(a != 4){
    a = parseInt(lines.shift().replace('\r',''))
    if(a == 1)
        alcool++
    if(a == 2)
        gasolina++
    if(a == 3)
        diesel++
}

console.log('MUITO OBRIGADO')
console.log(`Alcool: ${alcool}`)
console.log(`Gasolina: ${gasolina}`)
console.log(`Diesel: ${diesel}`)
