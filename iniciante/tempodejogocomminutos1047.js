var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function relogio(a, b, c, d){
    let horaInicio = a
    let minInicio = b
    let horaFinal = c
    let minFinal = d
    let countHora = 0
    let countMinuto = 0
    
    //Minutos
    while(true){
        minInicio++
        countMinuto++

        if(countMinuto == 60){
            countHora++
            countMinuto = 0
        }

        if(minInicio == minFinal){
            break
        }

        if(minInicio == 59){
            minInicio = -1
            horaInicio++
        }

    }
    
    //Horas
    while(true){
        if(horaInicio == horaFinal){
            break
        }

        horaInicio++
        countHora++
        
        if(horaInicio == 24){
            horaInicio = 0
        }

    }

    return `O JOGO DUROU ${countHora} HORA(S) E ${countMinuto} MINUTO(S)`
}

let entrada = lines.shift().split(' ')
let a = parseInt(entrada[0])
let b = parseInt(entrada[1])
let c = parseInt(entrada[2])
let d = parseInt(entrada[3])

console.log(relogio(a, b, c, d))
