var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let a = parseInt(lines.shift())
let b = parseInt(lines.shift().replace('\r',''))

let menor
let maior

if (a <= b){
    menor = a
    maior = b
    
}else{
    menor = b
    maior = a
}

for(let i = ++menor; i < maior; i++ ){
    if(i % 5 == 2 || i % 5 == 3 )
        console.log(i)
}
