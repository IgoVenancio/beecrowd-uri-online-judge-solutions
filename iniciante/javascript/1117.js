const { count } = require('console')

var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')


let media = 0
let countNotas = 0

while(true){

    let nota = parseFloat(lines.shift().replace('\r', ''))
    if(nota >= 0 && nota <= 10){
        media += nota
        countNotas++
    }else{
        console.log('nota invalida')
    }
    if(countNotas == 2)
        break
}

console.log(`media = ${(media/countNotas).toFixed(2)}`)

