// 1)დაწერეთ ფუქნცია, სახელად sayHello, რომელიც დაპრინტავს - "Hello, World".

function sayHello() {
    console.log("hello , world")
}

sayHello()

// 2)დაწერეთ ფუნქცია, სახელად greet, რომელიც პარამეტრა მიიღებს სახელს და დაპრინტავს - "გამარჯობა, [სახელი]"

function greet(name) {
    console.log("hello" , name)
}

greet("ალექს")

// 3)დაწერეთ ფუნქცია, სახელად sum, რომელიც არგუმენტებად მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს. შედეგი გამოიტანეთ ტერმინალში.

function sum(num1 , num2) {
    return num1 + num2
}

console.log(sum(11,12))

// 4)დაწერეთ ფუნქცია, სახელად calculateArea, რომელიც არგუმენტად მიიღებს ოთხკუთხედის სიგრესა და სიგანეს და დააბრუნებს მის ფართობს. შედეგი გამოიტანეთ ტერმინალში.

function calculateArea(length) {
    return console.log(length ** 2)
}

// 5)დაწერეთ ფუნქცია, რომელიც მიიღებს ორ არგუმენტს და დააბრუნებს მათ შორის უდიდესს.

function biggest(n1 , n2) {
    if(n1 > n2){
        return n1
    }
    return n2
}

console.log(biggest(3 , 2))

// 6)დაწერეთ ფუქნცია, რომელიც პარამეტრად მიიღებს იმ რაოდენობას, რამდენჯერად უნდა გამოკონსოლდეს "Hello, World".

//?

// 7)დაწერეთ ფუქნცია, სახელად celsiusToFahrenheit, რომელიც პარამეტრად მიიღებს ცელსიუსს და გადაიყვანს ფარენჰეიტში. ფორმულა - (Celsius * 9/5) + 32

function celsiusToFahrenheit(c){
    return (c * 9/5) + 32
}