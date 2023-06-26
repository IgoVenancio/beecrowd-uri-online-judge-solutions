var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function calcularSalario(a){
    let salario
    let reajuste
    let percentual

    if(a >= 0  && a <= 400.00){
        salario = a + 0.15 * a
        reajuste = 0.15 * a
        percentual = '15 %'
    }
    if(a >= 400.01  && a <= 800.00){
        salario = a + 0.12 * a
        reajuste = 0.12 * a
        percentual = '12 %'
    }
    if(a >= 800.01  && a <= 1200.00){
        salario = a + 0.10 * a
        reajuste = 0.10 * a
        percentual = '10 %'
    }
    if(a >= 1200.01  && a <= 2000.00){
        salario = a + 0.07 * a
        reajuste = 0.07 * a
        percentual = '7 %'
    }
    if(a > 2000.00){
        salario = a + 0.04 * a
        reajuste = 0.04 * a
        percentual = '4 %'
    }

    return `Novo salario: ${salario.toFixed(2)}\nReajuste ganho: ${reajuste.toFixed(2)}\nEm percentual: ${percentual}`
}

let entrada = parseFloat(lines.shift())

console.log(calcularSalario(entrada))

