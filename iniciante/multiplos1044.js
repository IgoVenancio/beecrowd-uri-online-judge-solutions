var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = lines.shift().split(' ')
let a = parseFloat(entrada[0])
let b = parseFloat(entrada[1])


const eMultiplo = function(a, b){
    
    if(a >= b){
        if(a % b === 0){
            return true
        }else{
            return false
        }
        
    }else{
        if(b % a === 0){
            return true
        }else{
            return false
        }
    }

}

if(eMultiplo(a, b)){
    console.log('Sao Multiplos')
}else{
    console.log('Nao sao Multiplos')
}
