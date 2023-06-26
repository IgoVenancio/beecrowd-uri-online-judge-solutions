var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let entradas = lines.shift().split(' ')
let a = parseFloat(entradas[0])
let b = parseFloat(entradas[1])
let c = parseFloat(entradas[2])

let delta = Math.pow(b, 2) - 4 * a * c
let r1 = (-b + Math.sqrt(delta))/(2 * a)
let r2 = (-b - Math.sqrt(delta))/(2 * a)

if(a == 0 || delta < 0){
    console.log(`Impossivel calcular`)
}else{
    console.log(`R1 = ${r1.toFixed(5)}`)
    console.log(`R2 = ${r2.toFixed(5)}`)
}


