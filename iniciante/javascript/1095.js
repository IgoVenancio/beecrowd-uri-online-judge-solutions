var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let i
let j
for(i = 1, j = 60; j >= 0; i +=3, j -= 5 ){
    console.log(`I=${i} J=${j}`)
}