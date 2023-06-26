var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function divisao(a, b){
    if(b !== 0){
        console.log((a/b).toFixed(1))
        return 1
    }else{
        console.log('divisao impossivel')
        return 0
    }
}

let entrada = parseInt(lines.shift())
let count = 0

while(count++ < entrada){
    let entradas = lines.shift().split(' ')
    let a = parseInt(entradas[0])
    let b = parseInt(entradas[1].replace('\r',''))
    divisao(a,b)
}
