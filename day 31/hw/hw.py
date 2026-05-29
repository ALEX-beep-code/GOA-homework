# 1) შექმენით სტრინგი ზედმეტი სფეისებით დასაწყისში და ბოლოში. strip მეთოდის გამოყენებით მოაშორეთ ზედმეტი სფეისები

arr = "    hi    "
arr = arr.strip()

# 2) მომხმარებელს შემოატანინეთ სახელი ზედმეტი სფეისებით. მოაშორეთ ზედმეტი სფეისები და დაპრინტეთ შედეგი

name = str(input("Enter your name with extra spaces"))
print(name.strip())

# 3) მომხმარებელს შემოატანინეთ სიტყვა. შეამოწმეთ იწყება თუ არა "A" ასოთი startswith მეთოდის გამოყენებით

sentence = (str(input("Enter a sentence")))
print(sentence.startswith("A"))

# 4) მომხმარებელს შემოატანინეთ ვებსაიტის მისამართი. შეამოწმეთ იწყება თუ არა "https"-ით

Site_URL = str(input("Enter your site URL"))
print(Site_URL.startswith("https"))

# 5) მომხმარებელს შემოატანინეთ ფაილის სახელი. შეამოწმეთ მთავრდება თუ არა .py-ზე endswith მეთოდის გამოყენებით

File_Name = str(input("Enter your file"))
print(File_Name.endswith("py"))

# 6) მომხმარებელს შემოატანინეთ ელფოსტა. შეამოწმეთ მთავრდება თუ არა "@gmail.com"-ზე

email = str(input("Enter your email"))
print(email.endswith("@gmail.com"))

# 7) შექმენით ტექსტი. `replace()` მეთოდის გამოყენებით შეცვალეთ სიტყვა "dog" სიტყვით "cat"

Text = "dogs are better than cows"
print(Text.replace("dogs" , "Cats"))

# 8) მომხმარებელს შემოატანინეთ წინადადება. ყველა სფეისი შეცვალეთ "-" სიმბოლოთი

sentence = str(input("Enter a sentece"))
print(sentence.replace(" " , "-"))

# 9) მომხმარებელს შემოატანინეთ ტელეფონის ნომერი ფორმატით "599-12-34-56". replace მეთოდის გამოყენებით წაშალეთ ყველა "-" სიმბოლო

Number = str(input("Enter your number"))
print(Number.replace("-" , " "))

# 10) მომხმარებელს შემოატანინეთ ტექსტი ზედმეტი სფეისებით. ჯერ strip მეთოდით მოაშორეთ ზედმეტი სფეისები, შემდეგ შეამოწმეთ იწყება თუ არა ტექსტი "Hello" სიტყვით

Text = str(input("Enter a text"))
Text = Text.strip()
print(Text.startswith("Hello"))

# 11) მომხმარებელს შემოატანინეთ პაროლი. შეამოწმეთ:
# - იწყება თუ არა დიდი ასოთი
# - მთავრდება თუ არა ციფრით "1"

password = str(input("Enter the password"))

if password[0] == password[0].upper():
    starts_with_upper = True
else:
    starts_with_upper = False

if password[0] == password.endswith("1"):
    starts_with_1 = True

# 12) მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - მოაშოროს ზედმეტი სფეისები
# - ყველა სფეისი შეცვალოს "_" სიმბოლოთი
# - შეამოწმოს მთავრდება თუ არა "." სიმბოლოზე
# - თუ არ მთავრდება, ბოლოში დაამატოს "."

sentence = str(input("Enter a sentence"))
sentence = sentence.strip()
sentence = sentence.replace(" " , "-")
if sentence.endswith(".") == False:
    sentence = sentence + "."

# 13) მომხმარებელს შემოატანინეთ სრული სახელი (სახელი, გვარი, მამის სახელი). `split()` მეთოდის გამოყენებით:
# - ცალ-ცალკე გამოიტანეთ თითოეული ნაწილი
# - დაითვალეთ რამდენი სიტყვაა შეყვანილ ტექსტში

user_info = str(input("Enter your name , surname and fathers name"))
user_info = user_info.split()
name = user_info[0]
surname = user_info[1]
fathers_name = user_info[2]
count = len(user_info)

#თუ თავდაპირველი ტექსტი იგულისხმეთ მაშინ count = len(sentence) იქნება 82 ხაზის შემდეგ 

# 14) მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - დაყოს ტექსტი სიტყვებად
# - გამოიტანოს ყველაზე გრძელი სიტყვა
# - გამოიტანოს ყველაზე მოკლე სიტყვა

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]
shortest = words[0]

for i in range(len(words)):
    if len(words[i]) > len(longest):
        longest = words[i]
    elif len(words[i]) < len(shortest):
        shortest = words[i]

print("Longest word:", longest)
print("Shortest word:", shortest)


# 15) მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13"). split მეთოდის გამოყენებით:
# - გადააქციეთ ისინი integer-ებად
# - იპოვეთ ჯამი
# - იპოვეთ ყველაზე დიდი და ყველაზე პატარა რიცხვი

numbers = str(input("Enter some numbers"))
numbers = numbers.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
Sum = 0
for i in range(len(numbers)):
    Sum += numbers[i]
print("Sum equals to - " + str(Sum))
smallest_number = numbers[0]
biggest_number = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > biggest_number:
        biggest_number = numbers[i]
    elif numbers[i] < smallest_number:
        smallest_number = numbers[i]