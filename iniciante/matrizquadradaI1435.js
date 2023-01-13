var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift())
let recebe = 1
let fora = 0
let dentro = 0
let entradaLimite = entrada
let saida = []
let count = 0
let matriz

while(entrada !== 0){

    matriz = new Array(entrada)

    for(let i = 0; i < entrada; i++)
        matriz[i] = new Array(entrada)

    while(count < entrada){

        for(let i = fora; i < entradaLimite; i++){
            for(let j = dentro; j < entradaLimite; j++){
    
                matriz[i][j] = recebe.toString().padStart(3)
            }
        }
        recebe++
        fora++
        dentro++
        entradaLimite--
        count++

    }

    for(let i = 0; i < entrada; i++){
        for(let j = 0; j < entrada; j++ ){
            saida[j] = matriz[i][j]
        }
        console.log(`${saida.toString().replace(/,/g,' ').trimEnd()}`)
    }

    console.log()

    entrada = parseInt(lines.shift())
    recebe = 1
    fora = 0
    dentro = 0
    entradaLimite = entrada
    count = 0

}
