var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function operacaoMatriz(matriz, operacao,operacaoLinha, qtdLinhas, qtdColunas){
    let soma = 0
    let media = 0
    let linha = operacaoLinha

    if(operacao === 'S'){
        for(let i = 0; i < qtdColunas; i++ )
            soma += matriz[i][linha]
        return soma
        }

    if(operacao === 'M'){
        for(let i = 0; i < qtdColunas; i++ )
            media += matriz[i][linha]
        return media /= qtdColunas
    }

}

let linhas = 12
let colunas = 12
let matriz = new Array(colunas)

for(let i = 0; i < colunas; i++)
    matriz[i] = new Array(linhas)

let entradaLinha = parseInt(lines.shift().replace('\r',''))
let operacao = lines.shift().replace('\r','')

for(let i = 0; i < colunas; i++){
    for(let j = 0; j < linhas; j++){
        matriz[i][j] = parseFloat(lines.shift().replace('\r',''))
    }
}

console.log(operacaoMatriz(matriz,operacao,entradaLinha,linhas,colunas).toFixed(1))

