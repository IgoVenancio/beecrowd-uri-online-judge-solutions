var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');


function proximoVivo(array, atual){
    for(let i = atual + 1; i < array.length; i++){
        if(array[i] != -1)
            return i     
    }
    for(let i = 0; i < atual - 1; i++){
        if(array[i] != -1)
            return i     
    }

}

//Mata e retorna o próximo vivo
function matar(array, passo, atual){
    let matei = atual

    for(let i = 0; i < passo - 1 ; i++){
        matei = proximoVivo(array, matei)  
    }
    array[matei] = -1
    return proximoVivo(array, matei)
}

//Função principal: chama a função matar e retorna o último sobrevivente do círculo
function sobrevivente(array, passo, atual = 0){
    let atual1 = atual
    let countVivos = 0

    if(passo == 1)
        return array.length - 1

    while(countVivos++ < array.length - 1){
        atual1 = matar(array, passo, atual1)
    }
    return atual1
}


let repeticoes = parseInt(lines.shift().replace('\r',''))
let countEntradas = 0

while(countEntradas++ < repeticoes){
    let entradas = lines.shift().split(' ')
    
    let qtdIndividuos = parseInt(entradas[0])
    let salto = parseInt(entradas[1].replace('\r',''))
    let circulo = []

    for(let i = 0; i < qtdIndividuos; i++)
        circulo[i] = i
    //Soma-se 1 ao final pois a lógica tem como base o array: 0, 1, 2 ...
    console.log(`Case ${countEntradas}: ${sobrevivente(circulo,salto) + 1}`)

}
