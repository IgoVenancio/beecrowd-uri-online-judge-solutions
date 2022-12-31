var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const pi = 3.14159

const volumeEsfera = a => (4/3 * pi * Math.pow(a,3))

console.log(`VOLUME = ${volumeEsfera(parseFloat(lines)).toFixed(3)}`)
