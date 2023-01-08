var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function fibonacci(a){
    let saida = []
    let l = 0
    let j = 1
    if(a == 1){
        console.log(0)
    }else{
        saida[0] = 0
        for(let i = 1; i < a; i++){
            saida[i] = l + j
            l = saida[i - 1]
            j = saida[i]

        }
        console.log(saida.join(' '))
    }
    
}
let x = parseInt(lines.shift())

fibonacci(x)
