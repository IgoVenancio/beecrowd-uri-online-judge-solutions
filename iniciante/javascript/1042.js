var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let entrada = lines.shift().split(' ')

const sortSimples = function(a, b, c){
    let array = [a, b, c]
    for(let i = 0; i < array.length - 1; i++ ){
        for(let j = i + 1; j < array.length; j++ ){
            if(array[j] < array[i]){
                let aux = array[i]
                array[i] = array[j]
                array[j] = aux
            }
        }

    }
    return array
}

const print = function(array1, array2){
    array1.forEach(e => {
        console.log(e)
    })
    console.log()
    array2.forEach(e => {
        console.log(e)
    })
}

let sort = sortSimples(parseInt(entrada[0]), parseInt(entrada[1]), parseInt(entrada[2]))

print(sort, entrada)
