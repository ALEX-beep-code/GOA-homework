const  numbers = [5, 10, 15, 25, 35]
let counter = 0
for(let i = 0 ; i <= numbers.length - 1; i++ ){
    counter += numbers[i]
}

const numbers2 = [5, 10, 15, 26, 35, 38, 450]
let counter2 = 0
for(let i = 0 ; i <= numbers2.length-1; i++){
    if(numbers2[i] % 2 == 0){
        counter2 += numbers2[i]
    }
}

let number3 = 6
for(let i = 1; i < 11; i++){
    console.log(number3 * i)
}

let numbers4 = [12, 45, 7, 89, 23, 56]
biggest = numbers4[0]
for(let i = 0; i < numbers4.length - 1; i++){
    if(numbers4[i] > biggest){
        biggest = numbers4[i]
    }
}

console.log(biggest)

let names = ["Nika", "Giorgi", "Ana", "Luka"]
for(i = 0 ; i < names.length - 1; i++){
    if (names[i] == "Ana"){
        console.log("არის")
    }
    else{
        console.log("არ არის")
    }
}
