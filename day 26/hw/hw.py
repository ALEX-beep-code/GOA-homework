# 1) ახსენით რას აკეთებს append მეთოდი და მოიყვანეთ მაგალითი

#append - ამატებს სიის ბოლოში ელემნტს

# 2) შექმენით ცარიელი სია. append მეთოდის გამოყენებით დაამატეთ მასში 5 სხვადასხვა რიცხვი და დაპრინტეთ სია

arr = []
arr.append(0)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)

# 3) შექმენით სია სიტყვებით. remove მეთოდის გამოყენებით წაშალეთ ერთ-ერთი სიტყვა და დაპრინტეთ შედეგი

arr = ["hi" , "hello" , "hallo"]
arr.remove("hello")
print(arr)

# 4) ახსენით განსხვავება remove და pop მეთოდებს შორის

#remove ბოლომდე შლის რაიმე ელემენტს ხოლო pop - ი იგივეს აკეთებს მაგრამ ასევე წაშლილი მნიშვნელობის მნიშვნელობას იმახსოვრებს

# 5) შექმენით სია რიცხვებით. pop მეთოდის გამოყენებით ამოიღეთ ბოლო ელემენტი და დაპრინტეთ როგორც ამოღებული ელემენტი, ასევე განახლებული სია

arr = [1 , 2 , 3,  5,  6,  7]
array = arr.pop(2)
print(arr) 
print(array)

# 6) შექმენით სია. insert მეთოდის გამოყენებით ჩასვით ახალი ელემენტი სიის შუაში

arr = [1 , 2 , 3, 5 , 6]
arr.insert(3 , 4)

# 7) შექმენით რიცხვების სია. sort მეთოდის გამოყენებით დაალაგეთ ეს სია და დაბეჭდეთ შედეგი

arr = ["b" , "c" , "a" , "d" , "o"]
arr.sort()
print(arr)

# 8) ახსენით როგორ მუშაობს reverse მეთოდი და მოიყვანეთ მაგალითი

#reverse მეთოდი ატრიალებს ცხრილს მაგალითად ცხრილი თუ არი 1 , 2 , 3
#reverse - ით იქნება 3, 2, 1

arr = [1 , 2 , 3]
arr.reverse()
print(arr)

# 9) შექმენით სია სიტყვებით. reverse მეთოდის გამოყენებით შეცვალეთ ელემენტების რიგი

arr = ["hi" , "salam" , "hallo" , "hello"]
arr.reverse()
print(arr)

# 10) შექმენით სია და გამოიყენეთ clear მეთოდი. რა შედეგი მიიღეთ?

arr = ["wax" , "1" , "2" , "hi"]
arr.clear()
print(arr)

#მივიღეთ [] რადგან ეს მეთოდი შლის ყველა ელემენტს

# 11) შექმენით სია რიცხვებით. გამოიყენეთ index მეთოდი, რომ იპოვოთ კონკრეტული რიცხვის ინდექსი

arr = [1 , 2 , 3 , 4 , 5 , 6]
(arr.index(2))

# #12) შექმენით სია სიტყვებით. მომხმარებელს მოთხოვეთ რაიმე სიტყვა.
#   - თუ ეს სიტყვა არის სიაში იპოვეთ რომელ ინდექსზე დგას ეს სიტყვა
#   - სხვა შემთხვევაში დაპრინტეთ 'ვერ მოიძებნდა'

word = str(input("enter a word "))
arr = ["hello" , "hi" , "salami" , "goodbye" , "bye"]
if word in arr:
    print(arr.index(word))
elif word not in arr:
    print("ვერ მოიძებნა")

# 13) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 10 რიცხვი და დაამატეთ ისინი ამ სიაში.

arr = []
i = 0
while i < 10:
     number = int(input("enter ur number"))
     arr.append(number)
     i += 1

# 14) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 7 რიცხვი და დაამატეთ ისინი ამ სიაში. დაპრინტეთ ამ რიცხვებიდან უდიდესი და უმცირესი რიცხვები

arr = []
i = 0
while i < 7:
     num = int(input("enter your number"))
     arr.append(num)
     i += 1
arr.sort()
print(arr)
smallest = arr[0]
largest = arr[-1]
print("Largest is " + str(largest))
print("smallest is " + str(smallest))

# 15) (|HARD|) შექმენით ცარიელი სია. მომხმარებელს სათითაოდ მოთხოვეთ 10 რიცხვი. სიაში დაამატეთ რიცხვი თუ: 
#   - დადებითია და არის ლუწი
#   - უარყოფითია და არის კენტი
# საბოლოოდ გაიგეთ ამ რიცხვების საშუალო

arr = []
user_numbers = []

i = 0
while i < 10:
    number = int(input("enter a number"))
    user_numbers.append(number)
    i += 1

for i in range(len(user_numbers)):
    if user_numbers[i] > 0 and user_numbers[i] % 2 == 0:
        arr.append(user_numbers[i])

    elif user_numbers[i] < 0 and user_numbers[i] % 2 != 0:
        arr.append(user_numbers[i])

sum_of_numbers = 0
for i in range(len(arr)):
    sum_of_numbers += arr[i]

print(sum_of_numbers)

average = sum_of_numbers / len(arr)
print(average)

#ძალიან სახალისო იყო ამის კეთება ;))