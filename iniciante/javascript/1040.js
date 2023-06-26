var input = require('fs').readFileSync('stdin','utf8')
var lines = input.split('\n')

let entrada = lines.shift().split(' ')
let nota1 = parseFloat(entrada[0])
let nota2 = parseFloat(entrada[1])
let nota3 = parseFloat(entrada[2])
let nota4 = parseFloat(entrada[3])

const media = function(a, b, c, d){
    return (a * 2 + b * 3 + c * 4 + d * 1)/10
}

let resultado = media(nota1, nota2, nota3, nota4)

console.log(`Media: ${resultado.toFixed(1)}`)

if(resultado >= 7.0){
    console.log('Aluno aprovado.')
}else if(resultado < 5.0){
    console.log('Aluno reprovado.')
}else if(resultado >= 5.0 && resultado <= 6.9){
    console.log('Aluno em exame.')
    let nota5 = parseFloat(lines.shift())
    console.log(`Nota do exame: ${nota5.toFixed(1)}`)
    let mediaFinal = (nota5 + resultado)/2
    if( mediaFinal < 5){
        console.log('Aluno reprovado.')
        console.log(`Media final: ${mediaFinalto.Fixed(1)}`)
    }else{
        console.log('Aluno aprovado.')
        console.log(`Media final: ${mediaFinal.toFixed(1)}`)
    }

}
