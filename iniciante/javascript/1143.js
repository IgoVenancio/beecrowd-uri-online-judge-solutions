var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift());

for(let i = 1; i <= entrada; i++){
    console.log((i) + ' ' + (Math.pow(i,2)) + ' ' + (Math.pow(i,3)));
}