#task 1

i = 200
while i < 500:
    if i % 4 == 0:
        if i % 7 == 0:
            print(i)
    i = i + 1

for i in range (200 , 500):
    if i % 4 == 0 and i % 7 == 0:
        print(i)

#task 2

i = 300
while i < 1000:
    if i % 3 == 0:
        if i % 10 == 0:
            print(i)
    i = i + 1


for i in range (300 , 1000):
    if i % 3 == 0 and i % 10 == 0:
        print(i)

#task 3

for i in range (1 , 50):
    if i % 2 == 0:
        print ("even")
        if i % 3 == 0:
            print ("odd")

#task 4

positive = 0
negative = 0

for i in range(10):
    num = int(input("Enter a number 10 tries "))
    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive:", positive)
print("Negative:", negative)

#task 5

numberX = int(input("enter a number"))
if numberX % 2 == 0 and numberX % 3 == 0:
    print("good")
elif numberX % 2 == 0 and numberX % 3 != 0:
    print("two")
elif numberX % 2 != 0 and numberX % 3 != 0:
    print("3")
else:
    print("None")

#task 6

for i in range (1 , 100):
    if i % 3 == 0:
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    else:
        print(i)

#task 7

positive = 0
negative = 0
num = int(input("Enter a number again (0 if you wanna stop):"))
while num != 0:
    if num > 0:
        positive = positive + 1
    if num < 0:
        negative = negative + 1
    print("you entered this number ->", num)
    num = int(input("Enter a number again (0 if you wanna stop):"))

print ("positive" + " " + str(positive))
print ("negative" + " " + str(negative))

#task 8

X = int(input("enter a number"))
Y = 1
while X > Y:
    if Y % 4 != 0:
        print(Y)
    Y = Y + 1

Z = int(input("enter a number"))
for i in range (1 , Z):
    if i % 4 != 0:
        print(i)

#task 9

inputs = 0
while  inputs < 5:
    number = int(input("enter a number 5 tries"))
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
     
    inputs = inputs + 1

for i in range(5):
    num = int(input("enter a number again 5 tries"))
    
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")



