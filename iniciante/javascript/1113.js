var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function crescenteDecrescente(a, b){
    if(a < b){
        console.log('Crescente')
        return 1
    }else if (a > b){
        console.log('Decrescente')
        return 1
    }else{
        return 0
    }
}

do{
    let entradas = lines.shift().split(' ')
    var a = parseInt(entradas[0])
    var b = parseInt(entradas[1].replace('\r',''))

}while (crescenteDecrescente(a, b))