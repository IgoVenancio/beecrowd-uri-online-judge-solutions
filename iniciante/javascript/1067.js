var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let count = 1
let entrada = parseInt(lines.shift())

while(count <= entrada){
    if(count % 2 != 0){
        console.log(count)
    }
    count++
}