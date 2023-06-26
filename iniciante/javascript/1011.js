var input = require('fs').readFileSync('stdin', 'utf8');
var lines = parseFloat(input.split('\n'));
console.log('VOLUME = ' + (4/3 * 3.14159 * lines * lines * lines).toFixed(3))