var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let a = Number(lines.shift());
let b = Number(lines.shift());
let  media = (a,b) => (a * 3.5 +  b * 7.5)/11

console.log(`MEDIA = ${media(a, b).toFixed(5)}`)