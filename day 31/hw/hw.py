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