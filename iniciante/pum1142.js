var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift().replace('\r',''))
let saida = []
let count = 0
let countPum = 0
let j = 0
let saida2 = []

//Preenche o array saida
for(let i = 1; ; i++){
    if(count++ < 3){
        saida[j++] = i
    }else{
        saida[j++] = 'PUM'
        count = 0
        countPum++
    }
    if(countPum == entrada)
        break
}

//Imprime as saídas: array saida2
countPum = 0
j = 0
for(let i = 0; ; i++){
    saida2[j++] = saida[i]
    if(saida[i] === 'PUM'){
        console.log(saida2.join(' '))
        j = 0
        countPum++
    }
    if(countPum == entrada)
        break
    
}
