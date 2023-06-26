var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let entrada = parseInt(lines.shift())
let saida = []

while(entrada !== 0){
    let i
    let j

    for(i = 1, j = 0; i <= entrada; i++){
        saida[j++] = i
    }
    console.log(saida.join(' '))
    saida = []
    entrada = parseInt(lines.shift())
}

