var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function quadrante(a, b){
    if(a !== 0 && b !== 0){
        if(a > 0 && b > 0){
            console.log('primeiro')
        }else if (a > 0 && b < 0){
            console.log('quarto')
        }else if (a < 0 && b > 0){
            console.log('segundo')
        }else{
            console.log('terceiro')
        }
        return 1
    }else{
        return 0
    }
}

do{
    let entradas = lines.shift().split(' ')
    var a = parseInt(entradas[0])
    var b = parseInt(entradas[1].replace('\r',''))
}while(quadrante(a, b))