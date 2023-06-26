var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

//Condicao:
// | b - c | < a < b + c
// | a - c | < b < a + c
// | a - b | < c < a + b

let entrada = lines.shift().split(' ')
let a = parseFloat(entrada[0])
let b = parseFloat(entrada[1])
let c = parseFloat(entrada[2])

const eTriangulo = function(a, b, c){
    let regra1 = Math.abs(b - c) < a && a < (b + c);
    let regra2 = Math.abs(a - c) < b && b < (a + c)
    let regra3 = Math.abs(a - b) < c && c < (a + b)
    if(regra1 && regra2 && regra3){
        return true
    }else{
        return false
    }

}

if(eTriangulo(a, b, c)){
    console.log(`Perimetro = ${(a + b + c).toFixed(1)}`)
}else{
    console.log(`Area = ${(((a + b) * c)/2).toFixed(1)}`)
}