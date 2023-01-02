var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function imprimirImposto(a){
    let imposto
    let taxas = ['Isento', '0.08', '0.18', '0.28']

    if (a >= 0.00 & a <= 2000.00){
         imposto = taxas[0]
         console.log(imposto)
    }else if (a >= 2000.01 && a <= 3000.0){
        imposto = (a - 2000.00) * parseFloat(taxas[1])
        console.log('R$ ' +imposto.toFixed(2))
    }else if (a >= 3000.01 && a <= 4500.00){
        imposto = (a - 3000) * parseFloat(taxas[2]) + 1000.00 * parseFloat(taxas[1])
        console.log('R$ ' +imposto.toFixed(2))
    }else{
        imposto = (a - 4500) * parseFloat(taxas[3]) + 1500.00 * parseFloat(taxas[2]) + 1000.00 * parseFloat(taxas[1])
        console.log('R$ ' +imposto.toFixed(2))
    }
    
}

let entrada = parseFloat(lines.shift())
imprimirImposto(entrada)
