#lower()
#upper()

#uppercase A
#lowercase a

word = "heLLo"
word = word.lower()
print(word)

#hello

word = word.upper()
print(word)

#HELLO


#title()
#capitalize()

sentence = "python is good"
sentence = sentence.title()
print(sentence)

sentence = "python is good"
sentence = sentence.capitalize()
print(sentence)

#strip()

l = "      iceberg        "
print(l.strip())

winadadeba = " me viyeneb pythons"
print(winadadeba.split())


winadadeba2 = "vashli,msxali,atami"
print(winadadeba2.split(","))

g = "abcdefg"
print(g.find("e"))

g = ["a" , "b" , "c" , "d"]
print(g.index("c"))

i = "i love goa"
print(i.replace("goa", "GOA"))

g.insert(1,"p")
print(g)

lost_element = g.pop(3)
print(lost_element , g)

arr = ["a" , "b" , "b" , "b" , "c"]
print(arr.count("b"))

list1 = [1 , 2 , 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

string = "hEllO World"

#capitalize()
#find()
#title()
#upper()
#lower()

#/

print(string)

#swapcase()

string = string.swapcase()
print(string)

#count()

string = string.lower()
print(string.count("l"))

#strip

#lstrip

l = "      iceberg"
print(l.lstrip())

#rstrip()

l = "iceberg       "
print(l.rstrip())

#islower()

sent = "word"
print(sent.islower())

#isupper()

sent = "WORD"
print(sent.isupper())

#casefold()
# w != W

word1 = "HELLO"
word2 = "hello"
print(word1.casefold() == word2.casefold())

#join()
words = ["hi" , "hello"]
result = " ".join(words)
print(result)