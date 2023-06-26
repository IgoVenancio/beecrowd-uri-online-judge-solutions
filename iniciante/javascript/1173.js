var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let count = 0
let numero = parseInt(lines.shift())

while(count++ < 10){
    console.log(`N[${count - 1}] = ${numero}`)
    numero *= 2
}
