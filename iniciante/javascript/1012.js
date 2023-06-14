var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numeros = lines.shift().split(' ')
let a = Number(numeros[0])
let b = Number(numeros[1])
let c = Number(numeros[2])


const areaTrianguloRetangulo = (a, b) => (a * b)/2
const areaCirculo = a => 3.14159 * Math.pow(a,2)
const areaTrapezio = (a, b, c) => ((a + b) * c)/2
const areaQuadrado = a => Math.pow(a, 2)
const areaRetangulo = (a, b) => a * b


console.log(`TRIANGULO: ${areaTrianguloRetangulo(a, c).toFixed(3)}`)
console.log(`CIRCULO: ${areaCirculo(c).toFixed(3)}`)
console.log(`TRAPEZIO: ${areaTrapezio(a, b, c).toFixed(3)}`)
console.log(`QUADRADO: ${areaQuadrado(b).toFixed(3)}`)
console.log(`RETANGULO: ${areaRetangulo(a, b).toFixed(3)}`)
