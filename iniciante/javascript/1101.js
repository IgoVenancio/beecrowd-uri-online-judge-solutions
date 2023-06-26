var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function soma(a, b){
    let menor
    let maior
    let soma = 0
    let saida = []
    let count
    if(a < b){
        menor = a
        maior = b
    }else{
        menor = b
        maior = a
    }
    
    for(let i = menor, count = 0; i <= maior; i++, count++){
        soma += i
        saida[count] = i
        if(i == 0)
            return 0
    }
    console.log(`${saida.join(' ')} Sum=${soma}`)
    return 1
}


do{
    entradas = lines.shift().split(' ')
    a = parseInt(entradas[0])
    b = parseInt(entradas[1].replace('\r',''))
}while(soma(a, b) != 0)
