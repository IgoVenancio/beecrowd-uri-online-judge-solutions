var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift())

for(let i = 2; i < 10000; i++){
    if(i % entrada == 2)
        console.log(i)
}
