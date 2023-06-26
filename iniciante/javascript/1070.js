var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let count = 0
let entrada = parseInt(lines.shift())

while(count < 6 ){
    if(entrada % 2 != 0){
        console.log(entrada)
        count++
    }
    entrada++
}