var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numero1 = parseInt(lines.shift())
let numero2 = parseInt(lines.shift())

let maior
let menor
let somaPrimos13 = 0

if (numero1 < numero2){
    menor = numero1
    maior = numero2
    for(let i = menor; i <= maior; i++ ){
        if(i % 13 !== 0)
            somaPrimos13 += i
    }
}else{
    menor = numero2
    maior = numero1
    for(let i = menor; i <= maior; i++ ){
        if(i % 13 !== 0)
            somaPrimos13 += i
    }
}

console.log(somaPrimos13)
