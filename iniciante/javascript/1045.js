var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

const sortSimples = function(a, b, c){
    let array = [a, b, c]
    for(let i = 0; i < array.length - 1; i++ ){
        for(let j = i + 1; j < array.length; j++ ){
            if(array[j] > array[i]){
                let aux = array[i]
                array[i] = array[j]
                array[j] = aux
            }
        }

    }
    return array
}

let entrada = lines.shift().split(' ')
let a = parseFloat(entrada[0])
let b = parseFloat(entrada[1])
let c = parseFloat(entrada[2])
let sort = sortSimples(a, b, c)

a = sort[0]
b = sort[1]
c = sort[2]

if(a >= (b + c)){
    console.log('NAO FORMA TRIANGULO')
}else{
    if(Math.pow(a, 2) == (Math.pow(b,2) + Math.pow(c,2) )){
        console.log('TRIANGULO RETANGULO')
    }
    if(Math.pow(a, 2) > (Math.pow(b,2) + Math.pow(c,2) )){
        console.log('TRIANGULO OBTUSANGULO')
    }
    if(Math.pow(a, 2) < (Math.pow(b,2) + Math.pow(c,2) )){
        console.log('TRIANGULO ACUTANGULO')
    }
    if(a == b && b == c){
        console.log('TRIANGULO EQUILATERO')
    }
    if((a == b && b != c) || (b == c && b != a) || (a == c && b != c) ){
        console.log('TRIANGULO ISOSCELES')
    }

}
