var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function operacaoMatriz(matriz, operacao, qtdLinhas, qtdColunas){
    let soma = 0
    let media = 0
    let countMedias = 0
    if(operacao === 'S'){
        for(let i = 0; i < qtdLinhas - 1; i++ ){
            for(let j = 0; j < qtdColunas - 1; j++)
                soma += matriz[i][j]
            qtdColunas--
        }
        return soma
        }

    if(operacao === 'M'){
        for(let i = 0; i < qtdLinhas - 1; i++ ){
            for(let j = 0; j < qtdColunas - 1; j++){
                media += matriz[i][j]
                countMedias++
            }
            qtdColunas--
                
        }
        return media /= countMedias
    }

}

let linhas = 12
let colunas = 12
let matriz = new Array(colunas)

for(let i = 0; i < colunas; i++)
    matriz[i] = new Array(linhas)

let operacao = lines.shift().replace('\r','')

for(let i = 0; i < colunas; i++){
    for(let j = 0; j < linhas; j++){
        matriz[i][j] = parseFloat(lines.shift().replace('\r',''))
    }
}

console.log(operacaoMatriz(matriz,operacao,linhas,colunas).toFixed(1))
