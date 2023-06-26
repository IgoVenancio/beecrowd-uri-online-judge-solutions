var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')


let entrada1 = lines.shift().replace('\r','')
let entradas = lines.shift().split(' ')
let count = 0

for(let i = 0; i < entradas.length; i++){
    if(entradas[i] == entrada1){
        count++
    }
        
}

console.log(count)