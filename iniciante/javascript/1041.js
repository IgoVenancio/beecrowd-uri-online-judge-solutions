var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let entrada = lines.shift().split(' ')
let p1 = parseFloat(entrada[0])
let p2 = parseFloat(entrada[1])

const coordenada = function(a, b){
    if(a == 0 && b == 0){
        return 'Origem'
    }else if(a == 0 && b != 0){
        return 'Eixo Y'
    }else if(a != 0 && b == 0){
        return 'Eixo X'
    }else if(a > 0 && b > 0){
        return 'Q1'
    }else if(a > 0 && b < 0){
        return 'Q4'
    }else if(a < 0 && b > 0){
        return 'Q2'
    }else if(a < 0 && b < 0){
        return 'Q3'
    }
    
}

console.log(coordenada(p1, p2))
