var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

const intervalo = function (a){
    if(a >= 0 && a <= 25){
        return 'Intervalo [0,25]'
    }else if (a > 25 && a <= 50){
        return 'Intervalo (25,50]'
    }else if (a > 50 && a <= 75){
        return 'Intervalo (50,75]'
    }else if (a > 75 && a <= 100){
        return 'Intervalo (75,100]'
    }else{
        return 'Fora de intervalo'
    }

}

let entrada = parseFloat(lines.shift())

console.log(intervalo(entrada))
