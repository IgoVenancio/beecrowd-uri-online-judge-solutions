var input = require('fs').readFileSync('stdin', 'utf8')
var lines = input.split('\n')

function validadorDeSenha(a, b){
    if(a !== b){
        console.log('Senha Invalida')
        return 0
    }else{
        console.log('Acesso Permitido')
        return 1
    }
}

do{
    var senha = parseInt(lines.shift().replace('\r',''))
}while(validadorDeSenha(senha, 2002) != 1)