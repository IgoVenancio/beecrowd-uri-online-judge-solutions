var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

function positivo(a){
    if(a > 0 ){
        return 1
    }
    return 0
}

let countEntradas = 0
let countPositivo = 0

while(countEntradas < 6){
    let entrada = lines.shift()
    countPositivo += positivo(entrada)
    countEntradas++
}

console.log(countPositivo+' valores positivos')