var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')


function calcularTempoDeCrescimentoPopulacional(a, b, c, d){
    let popA = a
    let popB = b
    let taxaA = c
    let taxaB = d
    let countAnos = 0

    while((popA <= popB)){
        popA += parseInt((popA * taxaA)/100)
        popB += parseInt((popB * taxaB)/100) 
        countAnos++
        if(countAnos > 100){
            return `Mais de 1 seculo.`
        }
        
    }
        return `${countAnos} anos.`
}


let testes = parseInt(lines.shift())

do{
    let entradas = lines.shift().split(' ')
    let popA = parseInt(entradas[0])
    let popB = parseInt(entradas[1])
    let taxaA = parseFloat(entradas[2])
    let taxaB = parseFloat(entradas[3])

    console.log(calcularTempoDeCrescimentoPopulacional(popA, popB, taxaA, taxaB))

}while(--testes > 0)