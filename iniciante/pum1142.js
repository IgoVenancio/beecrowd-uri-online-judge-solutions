let input = require('fs').readFileSync('/dev/stdin', 'utf8');
let lines = input.split('\n');

let entrada = parseInt(lines.shift());
let saida = [];
let count = 0;
let countPum = 0;
let j = 0;

for(let i = 1; ; i++){
    if(count++ < 3){
        saida[j++] = i;
    }else{
        saida[j++] = 'PUM';
        count = 0;
        countPum++;
        j = 0;
        console.log(saida.join(' '));
    }
    if(countPum == entrada)
        break;
}
