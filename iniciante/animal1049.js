var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let palavra1 = lines.shift().replace('\r','');
let palavra2 = lines.shift().replace('\r','');
let palavra3 = lines.shift().replace('\r','');

const animal = {
    vertebrado:{
        ave: {carnivoro: 'aguia',onivoro:'pomba'},
        mamifero: {onivoro: 'homem', herbivoro: 'vaca'}
    },
    invertebrado:{
        inseto:{hematofago: 'pulga', herbivoro: 'lagarta'},
        anelideo: {hematofago: 'sanguessuga', onivoro: 'minhoca'}
    }
         
};

console.log(animal[palavra1][palavra2][palavra3]);
