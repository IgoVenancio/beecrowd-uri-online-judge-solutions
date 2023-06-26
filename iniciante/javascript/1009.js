var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let nomeVendedor = lines.shift();
let salarioFixo = Number(lines.shift());
let montanteVendas = Number(lines.shift());
const porcentagemVendas = 0.15

const calcularSalario = (a, b) => (a + b * porcentagemVendas)

console.log(`TOTAL = R$ ${calcularSalario(salarioFixo, montanteVendas).toFixed(2)}`)