var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numeroFuncionario = Number(lines.shift());
let horasTrabalhadas = Number(lines.shift());
let valorPorHora = Number(lines.shift());

const calcularSalario = (a, b) => (a * b)

console.log(`NUMBER = ${numeroFuncionario}`)
console.log(`SALARY = U$ ${calcularSalario(horasTrabalhadas, valorPorHora).toFixed(2)}`)
