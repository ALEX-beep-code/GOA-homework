
// p styler

function pstyler(element) {
    element.style.color = "#787887"
    element.style.fontSize = "13px"
    element.style.fontWeight = "400"
}

// 1

let firstquestion = document.getElementById("firstquestion")
let extrapar1 = document.createElement("p")
let arrow1 = document.getElementById("arrow1")
let p1 = firstquestion.querySelector(".p1")
let counter1 = 0

extrapar1.textContent = "You can invite up to 7 members!"
pstyler(extrapar1)
extrapar1.style.marginTop = "12px"

firstquestion.addEventListener("click", function() {
    if (counter1 % 2 == 0) {
        p1.style.fontWeight = "700"
        arrow1.style.transform = "rotate(180deg)"
        firstquestion.append(extrapar1)
    }
    else {
        p1.style.fontWeight = "400"
        arrow1.style.transform = "rotate(0deg)"
        extrapar1.remove()
    }

    counter1++
})

// 2

let secondquestion = document.getElementById("secondquestion")
let extrapar2 = document.createElement("p")
let arrow2 = document.getElementById("arrow2")
let p2 = secondquestion.querySelector(".p1")
let counter2 = 0

extrapar2.textContent = "You can invite up to 7 members!"
pstyler(extrapar2)
extrapar2.style.marginTop = "12px"

secondquestion.addEventListener("click", function() {
    if (counter2 % 2 == 0) {
        p2.style.fontWeight = "700"
        arrow2.style.transform = "rotate(180deg)"
        secondquestion.append(extrapar2)
    }
    else {
        p2.style.fontWeight = "400"
        arrow2.style.transform = "rotate(0deg)"
        extrapar2.remove()
    }

    counter2++
})

// 3

let thirdquestion = document.getElementById("thirdquestion")
let extrapar3 = document.createElement("p")
let arrow3 = document.getElementById("arrow3")
let p3 = thirdquestion.querySelector(".p1")
let counter3 = 0

extrapar3.textContent = "You can invite up to 7 members!"
pstyler(extrapar3)
extrapar3.style.marginTop = "12px"

thirdquestion.addEventListener("click", function() {
    if (counter3 % 2 == 0) {
        p3.style.fontWeight = "700"
        arrow3.style.transform = "rotate(180deg)"
        thirdquestion.append(extrapar3)
    }
    else {
        p3.style.fontWeight = "400"
        arrow3.style.transform = "rotate(0deg)"
        extrapar3.remove()
    }

    counter3++
})

// 4

let fourthquestion = document.getElementById("fourthquestion")
let extrapar4 = document.createElement("p")
let arrow4 = document.getElementById("arrow4")
let p4 = fourthquestion.querySelector(".p1")
let counter4 = 0

extrapar4.textContent = "You can invite up to 7 members!"
pstyler(extrapar4)
extrapar4.style.marginTop = "12px"

fourthquestion.addEventListener("click", function() {
    if (counter4 % 2 == 0) {
        p4.style.fontWeight = "700"
        arrow4.style.transform = "rotate(180deg)"
        fourthquestion.append(extrapar4)
    }
    else {
        p4.style.fontWeight = "400"
        arrow4.style.transform = "rotate(0deg)"
        extrapar4.remove()
    }

    counter4++
})
