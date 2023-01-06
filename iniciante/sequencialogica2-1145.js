var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entradas = lines.shift().split(' ')
let x = parseInt(entradas[0])
let y = parseInt(entradas[1].replace('\r',''))
let saida = []
let count = 0

for(let i = 1; i <= y; i++){
    if(count++ < x){
        saida[count-1] = i
    }else{
        console.log(saida.join(' '))
        count = 0
        i--
        saida = []
    }
    if (i == y){
        console.log(saida.join(' '))
    }
}
