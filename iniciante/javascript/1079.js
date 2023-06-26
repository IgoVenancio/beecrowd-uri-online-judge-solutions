var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

let entrada = parseInt(lines.shift())
let countEntradas = 0

while(countEntradas++ < entrada){
    let valores = lines.shift().split(' ')
    let mediaPonderada = (parseFloat(valores[0]) * 2 + parseFloat(valores[1]) * 3 + parseFloat(valores[2].replace('\r', '')) * 5)/10
    console.log(mediaPonderada.toFixed(1))
}