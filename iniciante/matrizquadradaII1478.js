var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift())
let saida = []
let matriz
let inicioColuna
let contagem

while(entrada !== 0){
    
    inicioColuna = 0

    //Criar a matriz
    matriz = new Array(entrada)

    for(let i = 0; i < entrada; i++)
        matriz[i] = new Array(entrada)
    //-------------------------------------

        //Preencher matriz triangular superior
        for(let i = 0 ; i < entrada; i++){
            contagem = 1
            for(let j = inicioColuna; j < entrada; j++){
                matriz[i][j] = contagem.toString().padStart(3)
                contagem++
            }
            inicioColuna++
        }

        //Preencher matriz triangular inferior
        inicioColuna = 0
        for(let i = 0 ; i < entrada; i++){
            contagem = 1
            for(let j = inicioColuna; j < entrada; j++){
                matriz[j][i] = contagem.toString().padStart(3)
                contagem++
            }
            inicioColuna++
        }
        

    //Imprimir matriz
    for(let i = 0; i < entrada; i++){
        for(let j = 0; j < entrada; j++ ){
            saida[j] = matriz[i][j]
        }
        console.log(`${saida.toString().replace(/,/g,' ').trimEnd()}`)
    }

    console.log()

    entrada = parseInt(lines.shift())

}
