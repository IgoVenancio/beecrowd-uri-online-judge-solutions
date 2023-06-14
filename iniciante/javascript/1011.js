let input = require('fs').readFileSync('/dev/stdin', 'utf8');
let lines = parseFloat(input.split('\n'));
let volume = 4/3 * 3.14159 * Math.pow(lines,3)
console.log('VOLUME = ' + volume.toFixed(3))
