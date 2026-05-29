#1) მომხმარებელს მოთხოვეთ რაიმე წინადადება და რაიმე სიტყვა. გაიგეტ იწყება თუ არა ეს წინადადება ამ სიტყვით

sentence = str(input("enter a sentence"))
word = str(input("enter a word"))
print(sentence.startswith(word))

# 2) მომხმარებელს მოთხოვეთ რაიმე წინადადება და რაიმე სიტყვა. გაიგეტ მთავრდება თუ არა ეს წინადადება ამ სიტყვით

sentence = str(input("enter a sentence"))
word = str(input("enter a word"))
print(sentence.endswith(word))

# 3) მომხმარებელს მოთხოვეთ რაიმე ჩამოთვალოს თავისი საყვარელი ფერები(input ით). გამოიყენეთ split მეთოდი და დაპრინტეთ მიღებული სია 

colors = str(input("Enter your favourite colors"))
print(colors.split())

# 4) მომხმარებელს მოთხოვეთ შემოიყვანოს რიცხვები(input ით). გადაქციეთ ეს სტრინგი სიად ოღონდ ისე, რომ საბოლოო სია შეიცავდეს ინტეჯერებს 

numbers = str(input("enter some numbers"))
numbers = numbers.split()
arr = numbers.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(arr)

