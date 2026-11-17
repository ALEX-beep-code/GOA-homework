// 1)დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება თავის ასაკს და დაადგენს არის თუ არა 18 წლის ან უფრო მეტის. თუ არის, გამოპრინტეთ "Adult", თუარადა - "Minor". გამოიყენე ternary operator

let age = prompt("Enter your age:");

let result = age >= 18 ? "Adult" : "Minor";

console.log(result);


// 2) დაწერეთ ფუნქცია სახელად countBs, რომელიც იღებს სტრიქონს თავის ერთადერთ არგუმენტად და აბრუნებს სტრიქონში დიდი "B" სიმბოლოების რაოდენობას. გამოიყენე function expression

let countBs = function(string){
    let counter = 0
    for(let i = 0;i < string.length; i++){
        if(string[i] == "B"){
            counter += 1
        }
    }
    return counter
}

// 3) შექმენი ცვლადი number. თუ რიცხვი 10-დან 100-ის ჩათვლით არის, გამოიტანე "In Range", სხვა შემთხვევაში "Out of Range". გამოიყენე ternary

let number = prompt("enter a num")

let result2 = number >= 10 && number <= 100 ? "In Range" : "Out of Range";

console.log(result);


// 4)შექმენით Arrow Function, რომელსაც გადაეცემა ადამიანის ასაკი.

// თუ ასაკი 18 ან მეტია, დააბრუნოს "You can get a driving license", სხვა შემთხვევაში "You are too young".

let check = (age) => {age < 18 ? "You are too young" : "You can get a driving license"}
