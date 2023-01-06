var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift().replace('\r',''))
let saida = []
let saida2 = []
let count = 0
let countEntrada = 0
let j
let z
let i

for(i = 1, z = 1, j = 0 ;countEntrada < entrada; ){

    if(count++ < 3){
        if(count == 1){
            saida2[j] = z
            saida[j++] = z
            i = z
        }else{
            saida[j] = saida[j - 1] * i
            saida2[j] = saida[j] + 1
            i = saida[j - 1]
            j++
        }
    }else{
        z++
        count = 0
        countEntrada++
        j = 0
        console.log(saida.join(' '))
        console.log(saida2.join(' '))
    }
}
