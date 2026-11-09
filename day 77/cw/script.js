let body = document.body
body.style.display = "flex"
body.style.flexDirection = "column"
body.style.justifyContent = "center"
body.style.alignItems = "center"
body.style.minHeight = "100vh"
body.style.textAlign = "center"
body.style.backgroundColor = "#FAFAFA"
body.style.overflowX = "hidden"

let logo = document.createElement("img")
logo.style.marginTop = "80px"
logo.src = "assets/logo.svg"
body.append(logo)


let card1 = document.createElement("div")
card1.style.width = "100%"
card1.style.display = "flex"
card1.style.justifyContent = "space-between"
card1.style.alignItems = "center"
card1.style.flexDirection = "row"
body.append(card1)

let leftimgstack = document.createElement("img")
leftimgstack.src = "assets/desktop/image-hero-left.png"
card1.append(leftimgstack)

let card1div = document.createElement("div")
card1div.style.width = "540px"
card1div.style.height = "304px"
card1div.style.display = "flex"
card1div.style.flexDirection = "column"
card1div.style.justifyContent = "center"
card1div.style.alignItems = "center"
card1div.style.marginTop = "88px"
card1div.style.marginBottom = "88px"
card1.append(card1div)

let header = document.createElement("h1")
header.innerHTML = "Group Chat for Everyone"
header.style.marginBottom = "34px"
header.style.fontWeight = "900"
header.style.fontSize = "64px"
header.style.color = "#28283D"
header.style.textAlign = "center"
card1div.append(header)

let p1 = document.createElement("p")
p1.innerHTML = "Meet makes it easy to connect with others face-to-face virtually and collaborate across any device."
p1.style.marginBottom = "34px"
p1.style.textAlign = "center"
p1.style.color = "#87879D"
p1.style.fontWeight = "500"
p1.style.fontSize = "18px"
card1div.append(p1)

let card1divmini = document.createElement("div")
card1divmini.style.display = "flex"
card1divmini.style.alignItems = "center"
card1divmini.style.justifyContent = "center"
card1divmini.style.width = "348px"
card1divmini.style.height = "58px"
card1divmini.style.gap = "45px"
card1div.append(card1divmini)

let button1 = document.createElement("button")
button1.style.width = "193px"
button1.style.height = "58px"
button1.style.borderRadius = "29px"
button1.style.backgroundColor = "#71C0D4"
button1.style.border = "0px"
button1.style.fontSize = "16px"
button1.style.fontWeight = "900"
card1divmini.append(button1)

let butspan1 = document.createElement("span")
butspan1.innerHTML = "Download"
butspan1.style.color = "White"
button1.append(butspan1)

let butspan2 = document.createElement("span")
butspan2.innerHTML = "v1.3"
butspan2.style.color = "#8FE3F9"
butspan2.style.marginLeft = "4px"
button1.append(butspan2)

let button2 = document.createElement("button")
button2.innerHTML = "What is it?"
button2.style.backgroundColor = "#B18BDD"
button2.style.width = "139px"
button2.style.height = "58px"
button2.style.border = "0"
button2.style.borderRadius = "39px"
button2.style.color = "White"
button2.style.fontSize = "16px"
button2.style.fontWeight = "900"
card1divmini.append(button2)

let rightimgstack = document.createElement("img")
rightimgstack.src = "assets/desktop/image-hero-right.png"
card1.append(rightimgstack)

let zero1 = document.createElement("p")
zero1.innerHTML = "01"
zero1.style.width = "56px"
zero1.style.height = "56px"
zero1.style.fontWeight = "900"
zero1.style.color = "#87879D"
zero1.style.fontSize = "16px"
zero1.style.borderRadius = "50%"
zero1.style.backgroundColor = "#FAFAFA"
zero1.style.border = "solid 1px #87879D"
zero1.style.display = "flex"
zero1.style.justifyContent = "center"
zero1.style.alignItems = "center"
zero1.style.marginBottom = "64px"
body.append(zero1)

let photodiv2 = document.createElement("div")
photodiv2.style.display = "flex"
photodiv2.style.justifyContent = "center"
photodiv2.style.alignItems = "center"
photodiv2.style.width = "1110px"
photodiv2.style.height = "242px"
photodiv2.style.gap = "30px"
body.append(photodiv2)

let photodiv2img1 = document.createElement("img")
photodiv2img1.src = "assets/desktop/image-woman-in-videocall.jpg"
photodiv2img1.style.width = "255px"
photodiv2img1.style.height = "242px"
photodiv2img1.style.borderRadius = "20px"
photodiv2.append(photodiv2img1)

let photodiv2img2 = document.createElement("img")
photodiv2img2.src = "assets/desktop/image-women-videochatting.jpg"
photodiv2img2.style.width = "255px"
photodiv2img2.style.height = "242px"
photodiv2img2.style.borderRadius = "20px"
photodiv2.append(photodiv2img2)

let photodiv2img3 = document.createElement("img")
photodiv2img3.src = "assets/desktop/image-men-in-meeting.jpg"
photodiv2img3.style.width = "255px"
photodiv2img3.style.height = "242px"
photodiv2img3.style.borderRadius = "20px"
photodiv2.append(photodiv2img3)

let photodiv2img4 = document.createElement("img")
photodiv2img4.src = "assets/desktop/image-man-texting.jpg"
photodiv2img4.style.width = "255px"
photodiv2img4.style.height = "242px"
photodiv2img4.style.borderRadius = "20px"
photodiv2.append(photodiv2img4)

let bigdiv1 = document.createElement("div")
bigdiv1.style.width = "540px"
bigdiv1.style.height = "240px"
bigdiv1.style.display = "flex"
bigdiv1.style.flexDirection = "column"
bigdiv1.style.justifyContent = "center"
bigdiv1.style.alignItems = "center"
bigdiv1.style.textAlign = "center"
body.append(bigdiv1)

let p2 = document.createElement("p")
p2.innerHTML = "BUILT FOR MODERN USE"
p2.style.color = "#4D96A9"
p2.style.fontWeight = "900"
p2.style.fontSize = "16px"
p2.style.letterSpacing = "4px"
p2.style.marginTop = "80px"
p2.style.marginBottom = "16px"
bigdiv1.append(p2)

let header2 = document.createElement("h2")
header2.innerHTML = "Smarter meetings, all in one place"
header2.style.color = "#28283D"
header2.style.fontWeight = "900"
header2.style.fontSize = "40px"
header2.style.marginBottom = "32px"
bigdiv1.append(header2)

let p3 = document.createElement("p")
p3.innerHTML = "Send messages, share files, show your screen, and record your meetings — all in one workspace. Control who can join with invite-only team access, data encryption, and data export."
p3.style.color = "#87879D"
p3.style.fontWeight = "500"
p3.style.fontSize = "18px"
bigdiv1.append(p3)

let zero2 = document.createElement("p")
zero2.innerHTML = "02"
zero2.style.width = "56px"
zero2.style.height = "56px"
zero2.style.fontWeight = "900"
zero2.style.color = "#87879D"
zero2.style.fontSize = "16px"
zero2.style.borderRadius = "50%"
zero2.style.backgroundColor = "#FAFAFA"
zero2.style.border = "solid 1px #87879D"
zero2.style.display = "flex"
zero2.style.justifyContent = "center"
zero2.style.alignItems = "center"
zero2.style.marginBottom = "64px"
zero2.style.position = "relative"
zero2.style.top = "266px"
body.append(zero2)

let footerimage = document.createElement("div")
footerimage.style.backgroundImage = "url(assets/desktop/image-footer.jpg)"
footerimage.style.width = "1440px"
footerimage.style.height = "308px"
footerimage.style.marginTop = "184px"
footerimage.style.display = "flex"
footerimage.style.justifyContent = "center"
footerimage.style.alignItems = "center"
body.append(footerimage)

let mindiv = document.createElement("div")
mindiv.style.display = "flex"
mindiv.style.justifyContent = "center"
mindiv.style.alignItems = "center"
mindiv.style.width = "1110px"
mindiv.style.height = "88px"
footerimage.append(mindiv)

let lasthead = document.createElement("h2")
lasthead.innerHTML = "Experience more together"
lasthead.style.fontWeight = "900"
lasthead.style.color = "#FAFAFA"
lasthead.style.fontSize = "40px"
mindiv.append(lasthead)
