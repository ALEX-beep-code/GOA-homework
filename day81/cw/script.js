let btn = document.getElementById("btn")
let result = document.getElementById("result")
let userInput = prompt("Enter something")

btn.addEventListener("click", function() {
    result.innerHTML = userInput
})