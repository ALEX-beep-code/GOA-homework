// 6) შექმენი ვებგვერდი სათაურით, პარაგრაფით და ღილაკით.
// - ღილაკზე დაჭერისას გვერდის ფონი გახდეს შავი.
// - ტექსტის ფერი გახდეს თეთრი.
// - მეორე დაჭერაზე ყველაფერი დაუბრუნდეს საწყის მდგომარეობას.

let body = document.body
let para = document.createElement("p")
para.innerHTML = "JS best"
body.append(para)
let button = document.getElementById("but")

button.addEventListener("click" , function(){
    body.style.backgroundColor = "black"
    para.style.color = "white"
})

