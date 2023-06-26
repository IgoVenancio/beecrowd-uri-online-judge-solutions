var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function relogio(a, b, c, d, e, f, g, h){
    let diaInicio = a
    let horaInicio = b
    let minInicio = c
    let segundoInicio = d
    let diaFinal = e
    let horaFinal = f
    let minFinal = g
    let segundoFinal = h
    let countDia = 0
    let countHora = 0
    let countMinuto = 0
    let countSegundo = 0

    //Segundo
    while(true){
        segundoInicio++
        countSegundo++

        if(countSegundo == 60){
            countMinuto++
            countSegundo = 0
        }

        if(segundoInicio == segundoFinal){
            break
        }

        if(segundoInicio == 59){
            segundoInicio = -1
            minInicio++
        }

    }

    //Minuto
    while(true){

        if(minInicio == minFinal){
            break
        }

        minInicio++
        countMinuto++

        if(countMinuto == 60){
            countHora++
            countMinuto = 0
        }

        if(minInicio == 59){
            minInicio = -1
            horaInicio++
        }

    }
    
    //Hora
    while(true){
        
        if(horaInicio == horaFinal){
            break
        }
        
        horaInicio++
        countHora++

        if(countHora == 24){
            countDia++
            countHora = 0
        }

        if(horaInicio == 23){
            horaInicio = -1
            diaInicio++
        }

    }
    //Dia
    while(true){
        if(diaInicio == diaFinal){
            break
        }

        diaInicio++
        countDia++ 

    }

   
    return `${countDia} dia(s)\n${countHora} hora(s)\n${countMinuto} minuto(s)\n${countSegundo} segundo(s)`
}


let entrada1 = lines.shift().split(' ')
let entrada2 = lines.shift().split(' : ')
let entrada3 = lines.shift().split(' ')
let entrada4 = lines.shift().split(' : ')

let a = parseInt(entrada1[1].replace('\r',''))
let b = parseInt(entrada2[0])
let c = parseInt(entrada2[1])
let d = parseInt(entrada2[2].replace('\r',''))
let e = parseInt(entrada3[1].replace('\r',''))
let f = parseInt(entrada4[0])
let g = parseInt(entrada4[1])
let h = parseInt(entrada4[2].replace('\r',''))

console.log(relogio(a, b, c, d, e, f, g, h))






