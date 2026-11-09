let skeleton = document.body 

let header = document.createElement("h1")
header.innerText = "Welcome to my blog"
skeleton.append(header)

let unorderedlist = document.createElement("ul")
skeleton.append(unorderedlist)

let listitem1 = document.createElement("li")
unorderedlist.append(listitem1)

let listitem2 = document.createElement("li")
unorderedlist.append(listitem2)

let listitem3 = document.createElement("li")
unorderedlist.append(listitem3)

let listitem4 = document.createElement("li")
unorderedlist.append(listitem4)

let link1 = document.createElement("a")
link1.innerText = "Home"
link1.href = "https://alta.ge/"
listitem1.append(link1)

let link2 = document.createElement("a")
link2.innerText = "about me"
link2.href = "https://alta.ge/"
listitem2.append(link2)

let link3 = document.createElement("a")
link3.innerText = "blog posts"
link3.href = "https://alta.ge/"
listitem3.append(link3)

let link4 = document.createElement("a")
link4.innerText = "contact"
link4.href = "https://alta.ge/"
listitem4.append(link4)

let header2 = document.createElement("h2")
header2.innerText = "introduction"
skeleton.append(header2)

let p1 = document.createElement("p")
p1.innerText = "this is a place where i share my thoughts and expiriences. stay tuned for updates!"
skeleton.append(p1)

let header3 = document.createElement("h2")
header3.innerText = "about me"
skeleton.append(header3)

let p2 = document.createElement("p")
p2.innerText = "im a passionate writer and a developer who enjoys sharing knowledge on various subjects"
skeleton.append(p2)

let header4 = document.createElement("h2")
header4.innerText = "Latest blog posts"
skeleton.append(header4)

let header5 = document.createElement("h3")
header5.innerText = "My first blog post!"
skeleton.append(header5)

let p3 = document.createElement("p")
p3.innerText = "Welcome to my first blog post here ill be discussing web devlopment basics and more"
skeleton.append(p3)

let link5 = document.createElement("a")
link5.innerText = "READ MORE"
link5.href = "https://alta.ge/"
skeleton.append(link5)

let header6 = document.createElement("h2")
header6.innerText = "Exploring HTML elements"
skeleton.append(header6)

let p4 = document.createElement("p")
p4.innerText = "In this post we will dive deeper into HTML, such as block-level and inline elements!"
skeleton.append(p4)

let link6 = document.createElement("a")
link6.innerText = "READ MORE"
link6.href = "https://alta.ge/"
skeleton.append(link6)

let header7 = document.createElement("h2")
header7.innerText = "Navigation"
skeleton.append(header7)

let navigation = document.createElement("ul")
skeleton.append(navigation)

let listitem6 = document.createElement("li")
navigation.append(listitem6)

let listitem7 = document.createElement("li")
navigation.append(listitem7)

let listitem8 = document.createElement("li")
navigation.append(listitem8)

let link8 = document.createElement("a")
link8.innerText = "Home"
link8.href = "https://alta.ge/"
listitem6.append(link8)

let link9 = document.createElement("a")
link9.innerText = "about me"
link9.href = "https://alta.ge/"
listitem7.append(link9)

let link10 = document.createElement("a")
link10.innerText = "Blog posts"
link10.href = "https://alta.ge/"
listitem8.append(link10)

let p5 = document.createElement("p")
p5.innerText = "@Copyright reserved my blog"
skeleton.append(p5)
