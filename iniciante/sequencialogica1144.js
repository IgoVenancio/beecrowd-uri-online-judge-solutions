var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines[0])

for(let i = 1; i <= entrada; i++){
    console.log((i) + ' ' + (i * i) + ' ' + (i * i * i))
    console.log((i) + ' ' + (i * i + 1) + ' ' + (i * i * i + 1))
}
