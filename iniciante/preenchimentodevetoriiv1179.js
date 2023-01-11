var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let vetorPar = []
let vetorImpar = []
let countPar = 0
let countImpar = 0
let countEntradas = 0

while(countEntradas++ < 15){
    let numero = parseInt(lines.shift())
    if(numero % 2 === 0){
        vetorPar[countPar] = numero
        countPar++
    }else{
        vetorImpar[countImpar] = numero
        countImpar++
    }
    if(countPar == 5){
        for (let i = 0; i < countPar; i++) {
            console.log(`par[${i}] = ${vetorPar[i]}`)
        }
        countPar = 0
    }

    if(countImpar == 5){
        for (let i = 0; i < countImpar; i++) {
            console.log(`impar[${i}] = ${vetorImpar[i]}`)      
        }
        countImpar = 0
    }
}

if(countImpar != 0){
    for (let i = 0; i < countImpar; i++) {
        console.log(`impar[${i}] = ${vetorImpar.shift()}`)      
    }
}
if(countPar != 0){
    for (let i = 0; i < countPar; i++) {
        console.log(`par[${i}] = ${vetorPar.shift()}`)
    }
}
