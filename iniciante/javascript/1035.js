var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function aceitoOuNaoAceito(a, b, c ,d){
    if ( b > c && d > a && (c + d) > (a + b) && c > 0 && d > 0 && (a % 2 == 0)){
        return 'Valores aceitos'
    }else{
        return 'Valores nao aceitos'
    }

}

let entrada = lines.shift().split(' ')

console.log(aceitoOuNaoAceito(parseInt(entrada[0]), parseInt(entrada[1]), parseInt(entrada[2]), parseInt(entrada[3])))
