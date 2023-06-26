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
    if(countNotas == 2){
        console.log(`media = ${(media/countNotas).toFixed(2)}`)
        do{
            console.log('novo calculo (1-sim 2-nao)')
            var menu = parseInt(lines.shift().replace('\r', ''))
        }while(menu != 1 && menu != 2 )
        
        if(menu == 1){
            countNotas = 0
            media = 0
        }else{
            break
        }
    }

}



