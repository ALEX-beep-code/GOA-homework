# 1) ახსენით რას აკეთებს lower მეთოდი და მოიყვანეთ მაგალითი

#lower მეთოდი აქცევს ყველა upper_case ასოებს მოცემულ სტრინგში lower_case - ად მაგ:

arr = "hEllO"
print(arr.lower())

# 2) შექმენით სტრინგი დიდი ასოებით. lower მეთოდის გამოყენებით გადააკეთეთ ყველა ასო პატარად და დაპრინტეთ შედეგი

arr = "ALEX"
arr = arr.lower()
print(arr)

# 3) ახსენით რას აკეთებს upper მეთოდი და მოიყვანეთ მაგალითი

#lower მეთოდი აქცევს ყველა lower_case ასოებს მოცემულ სტრინგში upper_case - ად მაგ:

arr = "alex"
print(arr.upper())

# 4) მომხმარებელს შემოატანინეთ სიტყვა. upper მეთოდის გამოყენებით გადააკეთეთ ეს სიტყვა დიდ ასოებად

word = str(input("enter a word"))
print(word.upper())

# 5) ახსენით რას აკეთებს title მეთოდი და მოიყვანეთ მაგალითი

#title მეთოდი აქცევს პირველ ასოს სტრინგში upper_case - ად და დანარჩენ ასოებს აქცევს lower_case - ად მაგ:

arr = "hEllO"
print(arr.title())

# 6) შექმენით სტრინგების სია. გამოიყენეთ title მეთოდი თითოეულ სტრინგზე

arr = ["alEx" , "lUka"]
for i in range (len(arr)):
    print(arr[i].title())

# 7) შექმენით სტრინგი, სადაც შერეული იქნება დიდი და პატარა ასოები. swapcase მეთოდის გამოყენებით შეცვალეთ ასოების ზომები და დაპრინტეთ შედეგი

arr = "RaNdOM"
print(arr.swapcase())

# 8) შექმენით სტრინგი. count მეთოდის გამოყენებით დაითვალეთ რამდენჯერ გვხვდება კონკრეტული ასო

arr = "alexandre"
print(arr.count("a"))

# 9) მომხმარებელს შემოატანინეთ წინადადება და ერთი სიმბოლო. count მეთოდის გამოყენებით გაიგეთ რამდენჯერ გვხვდება ეს სიმბოლო წინადადებაში

word = str(input("enter another word"))
symbol = str(input("enter a symbol"))
print(word.count(symbol))

# 10) მომხმარებელს შემოატანინეთ სახელი და გვარი. title მეთოდის გამოყენებით სწორ ფორმატში დაპრინტეთ ორივე.

user_info = []

for i in range(1):
    user_info.append(str(input("enter your name")))
if user_info[0] == user_info[0]:
    user_info.append(str(input("enter your surname")))

for i in range(len(user_info)):
    print(user_info[i].title())

# 11) მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც). დათვალეთ ხმოვნების რაოდენობა.

sentence = input("enter a sentence: ")
sentence = sentence.lower()
count = 0
vowels = "aeiou"
current_number = 0
different_i = 0

for i in range(len(sentence)):
        current_number = i
        for different_i in range(len(vowels)):
            if sentence[current_number] == vowels[different_i]:
                count += 1

print(count)

# 12) მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც).
#   - გაიგეთ დიდი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ პატარა ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ ხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ თანხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ სფეისების პროცენტული რაოდენობა სტრინგში

sentence = input("enter a sentence: ")

upper = 0
lower = 0
vowels = 0
consonants = 0
spaces = 0

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = "abcdefghijklmnopqrstuvwxyz"
vowel_letters = "aeiouAEIOU"

for i in range(len(sentence)):

    for i2 in range(len(upper_letters)):
        if sentence[i] == upper_letters[i2]:
            upper += 1

    for i2 in range(len(lower_letters)):
        if sentence[i] == lower_letters[i2]:
            lower += 1

            for i3 in range(len(vowel_letters)):
                if sentence[i] == vowel_letters[i3]:
                    vowels += 1

            is_vowel = 0
            for i3 in range(len(vowel_letters)):
                if sentence[i] == vowel_letters[i3]:
                    is_vowel = 1

            if is_vowel == 0:
                consonants += 1

    if sentence[i] == " ":
        spaces += 1

Sum = len(sentence)

print("Uppercase :", upper * 100 / Sum)
print("Lowercase :", lower * 100 / Sum)
print("Vowels :", vowels * 100 / Sum)
print("Consonants :", consonants * 100 / Sum)
print("Spaces :", spaces * 100 / Sum)