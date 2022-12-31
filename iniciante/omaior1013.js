var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numeros = lines.shift().split(' ')
let a = parseInt(numeros[0])
let b = parseInt(numeros[1])
let c = parseInt(numeros[2])


function maior(a, b, c){
    let resultado = (a + b + Math.abs(a - b))/2
    return (resultado + c + Math.abs(resultado - c))/2
}

let resultado = maior(a, b, c)

console.log(`${resultado} eh o maior`)
