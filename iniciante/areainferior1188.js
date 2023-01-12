var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function operacaoMatriz(matriz, operacao, qtdLinhas, qtdColunas){
    let soma = 0
    let media = 0
    let countMedias = 0
    let colunas = qtdColunas
    let inicio = 1
    let final = qtdColunas - 1

    if(operacao === 'S'){
        for(let i = qtdLinhas - 1; i > (qtdLinhas/2) - 1; i-- ){
            for(let j = inicio; j < final; j++)
                soma += matriz[i][j]
            inicio++
            final--
        }
        return soma
        }

    if(operacao === 'M'){
        for(let i = qtdLinhas - 1; i > (qtdLinhas/2) - 1; i-- ){
            for(let j = inicio; j < final; j++){
                media += matriz[i][j]
                countMedias++
            }
            inicio++
            final--    
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
