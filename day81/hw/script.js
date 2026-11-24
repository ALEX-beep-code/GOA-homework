// 1)1. ტექსტის შეცვლა
// შექმენი HTML-ში ერთი პარაგრაფი და ერთი ღილაკი.
// - ღილაკზე დაჭერისას პარაგრაფის ტექსტი შეიცვალოს.
// - ახალი ტექსტი იყოს: "Hello, JavaScript!"

let p1 = document.getElementById("p1")
let bt1 = document.getElementById("button1")

bt1.addEventListener("click" , function(){
    p1.innerHTML = "Hello JS"
})

// 2) შექმენი პარაგრაფი და ღილაკი.
// - ღილაკზე დაჭერისას პარაგრაფი დაიმალოს.
// - გამოიყენე style.display.

let p2 = document.getElementById("p2")
let bt2 = document.getElementById("button2")

bt2.addEventListener("click" , function(){
    p2.style.display = "none"
})

// 3) შექმენი პარაგრაფი და ღილაკი.
// - პირველ დაჭერაზე პარაგრაფი დაიმალოს.
// - მეორე დაჭერაზე ისევ გამოჩნდეს.
// - გამოიყენე if/else.

let p3 = document.getElementById("p3")
let bt3 = document.getElementById("button3")

bt3.addEventListener("click", function(){
    if(p3.style.display === "none"){
        p3.style.display = "block"
    }
    else{
        p3.style.display = "none"
    }
})

// 4)  შექმენი ერთი div ელემენტი და ღილაკი.
// - ღილაკზე დაჭერისას div-ის ფონი გახდეს ლურჯი.
// - მეორე დაჭერაზე გახდეს ყვითელი.

let div1 = document.getElementById("div1")
let bt4 = document.getElementById("button4")
div1.style.width = "100px"
div1.style.height = "100px"

bt4.addEventListener("click" , function(){
    if(div1.style.backgroundColor != "blue"){
        div1.style.backgroundColor = "blue"
    }
    else{
        div1.style.backgroundColor = "yellow"
    }
})


// 5) შექმენი Like ღილაკი და პარაგრაფი, სადაც გამოჩნდება მოწონებების რაოდენობა.
// - ყოველ დაჭერაზე Like-ების რაოდენობა გაიზარდოს ერთით.
// - რაოდენობა დაიწყოს 0-დან.

let p4 = document.getElementById("p4")
let bt5 = document.getElementById("button5")

let likes = 0

bt5.addEventListener("click", function(){
    likes++
    p4.innerHTML = likes
})

// 6) შექმენი ვებგვერდი სათაურით, პარაგრაფით და ღილაკით.
// - ღილაკზე დაჭერისას გვერდის ფონი გახდეს შავი.
// - ტექსტის ფერი გახდეს თეთრი.
// - მეორე დაჭერაზე ყველაფერი დაუბრუნდეს საწყის მდგომარეობას.

// other file

// 7) შექმენი სურათი და ღილაკი.
// - ღილაკზე დაჭერისას სურათი შეიცვალოს სხვა სურათით.
// - გამოიყენე src ატრიბუტი.

let image = document.getElementById("ax")
let buttonX = document.getElementById("button6")

buttonX.addEventListener("click", function(){
    image.src = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=600"
})

// 8) შექმენი სამი ღილაკი:
// - Increase
// - Decrease
// - Reset
// შექმენი პარაგრაფი, რომელშიც გამოჩნდება რიცხვი.
// - Increase ზრდის რიცხვს ერთით.
// - Decrease ამცირებს რიცხვს ერთით.
// - Reset აბრუნებს რიცხვს 0-ზე.

let number = 0

let p = document.getElementById("number")
let increase = document.getElementById("increase")
let decrease = document.getElementById("decrease")
let reset = document.getElementById("reset")

increase.addEventListener("click", function(){
    number++
    p.innerHTML = number
})

decrease.addEventListener("click", function(){
    number--
    p.innerHTML = number
})

reset.addEventListener("click", function(){
    number = 0
    p.innerHTML = number
})

// 9) შექმენი პარაგრაფი და ორი ღილაკი:
// - Increase Font
// - Decrease Font

let par = document.getElementById("fonter")
let inc = document.getElementById("inc")
let dec = document.getElementById("dec")
let size = 16

inc.addEventListener("click" , function(){
    size += 2
    par.style.fontSize = size + "px"
})

dec.addEventListener("click" , function(){
    size -= 2
    par.style.fontSize = size + "px"
})

// პირველი ღილაკი ზრდის ტექსტის ზომას 2px-ით, მეორე ამცირებს 2px-ით

// 10) შექმენი სამი კითხვა და თითოეულ კითხვას დაუმატე პასუხი.
// - პასუხები თავდაპირველად დამალული უნდა იყოს.
// - კითხვაზე დაჭერისას შესაბამისი პასუხი გამოჩნდეს.
// - ხელახლა დაჭერისას დაიმალოს.

let a1 = document.getElementById("a1")
let a2 = document.getElementById("a2")
let a3 = document.getElementById("a3")

a1.addEventListener("click", function(){
    if(a1.innerHTML == "?"){
        a1.innerHTML = "A programming language"
    }
    else{
        a1.innerHTML = "?"
    }
})

a2.addEventListener("click", function(){
    if(a2.innerHTML == "?"){
        a2.innerHTML = "A markup language"
    }
    else{
        a2.innerHTML = "?"
    }
})

a3.addEventListener("click", function(){
    if(a3.innerHTML == "?"){
        a3.innerHTML = "A styling language"
    }
    else{
        a3.innerHTML = "?"
    }
})