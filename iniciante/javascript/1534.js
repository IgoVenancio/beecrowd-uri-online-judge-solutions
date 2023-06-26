var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let entrada = parseInt(lines.shift())
let saida = []
let matriz
let recebe

while(entrada > 0){
    
    //Criar a matriz
    matriz = new Array(entrada)

    for(let i = 0; i < entrada; i++)
        matriz[i] = new Array(entrada)
    //-------------------------------------

    //Preencher matriz triangular superior
    for(let i = 0 ; i < entrada; i++){
        for(let j = 0; j < entrada; j++){
            if(i === j && (i + j !== entrada - 1)){
                recebe = 1
            }else if( i + j === entrada - 1){
                recebe = 2
            }else{
                recebe = 3
            }
            matriz[i][j] = recebe.toString()
        }
    }

    //Imprimir matriz
    for(let i = 0; i < entrada; i++){
        for(let j = 0; j < entrada; j++ ){
            saida[j] = matriz[i][j]
        }
        console.log(`${saida.toString().replace(/,/g,'').trimEnd()}`)
    }

    entrada = parseInt(lines.shift())

}
console.log()


