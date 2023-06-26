let soma = 0
let j = 1

for(let i = 1; i <= 39; i+=2){
    soma +=(i/j)
    j *= 2
}

console.log(soma.toFixed(2))