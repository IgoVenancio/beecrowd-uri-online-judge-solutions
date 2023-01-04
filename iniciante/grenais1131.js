var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let qtdGrenais = 0
let qtdEmpates = 0
let vitoriasGremio = 0
let vitoriasInter = 0

do{
    let entradas = lines.shift().split(' ')
    var inter = parseInt(entradas[0])
    var gremio = parseInt(entradas[1].replace('\r',''))
    
    qtdGrenais++
    
    if(inter > gremio){
        vitoriasInter++
    }else{
        vitoriasGremio++
    }
    if(inter == gremio)
        qtdEmpates++
    console.log('Novo grenal (1-sim 2-nao)')
    var menu = parseInt(lines.shift().replace('\r',''))

}while(menu == 1)


console.log(`${qtdGrenais} grenais`)
console.log(`Inter:${vitoriasInter}`)
console.log(`Gremio:${vitoriasGremio}`)
console.log(`Empates:${qtdEmpates}`)

if(vitoriasInter > vitoriasGremio){
    console.log('Inter venceu mais')
}else if( vitoriasGremio > vitoriasInter){
    console.log('Gremio venceu mais')
}else{
    console.log('Nao houve vencedor')
}
