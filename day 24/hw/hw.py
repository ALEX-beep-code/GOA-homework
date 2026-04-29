# 1) ახსენით რა არის mutable და immutable?

# 1) mutable არის როცა რაიმე მიმდევრობას შეგვიძლია შევუცვალოთ ელემენტი მაგალითად ლისტში შევცვალოთ რომელიმე ელემენტი და immutable არის mutable -ის ანტონიმი ანუ შეცვლა არ შეიძლება მაგალითად სტრინგი რომელსაც ელემენტს ვერ შევუცვლით

# 2) ახსენით რას აკეთებს len ფუნქცია

# 2) len ფუნქცია ითვლის რაიმე მიმდევრობაში არსებული ელემენტების რაოდენობას

# 3) შექმენით ცვლადი სადაც შეინახავთ რაიმე სიტყვას. დაპრინტეთ რამდენი სიმბოლოა ამ სიტყვაში

word = "hello"
print(len(word))

# 4) შექმენით ცვლადი სადაც მომხმარებელს შემოაყვანინებთ რაიმე წინადადაებას. დაპრინტეთ სიმბოლოების რაოდენობა ამ წინადადებაში

sentence = str(input("write a sentence"))
print(len(sentence))

# 5) შექმენით სია სადაც შეინახავთ რიცხვებს. for loop ის გამოყენებით დაითვალეთ რამდენი დადებითი და რამდენი უარყოფითი რიცხვია ამ სიაში

positive = 0
negative = 0

numbers_list = [1 , 2 , 3 , -1 , -2 , -3]
for i in range (len(numbers_list)):
    if numbers_list[i] > 0:
        positive += 1
    elif numbers_list[i] < 0:
        negative += 1
print(positive)
print(negative)
    
# 6) შექმნეით სია სადაც შეინახავთ რიცხვებს. დაითვალეთ რამდენი რიცხვი არის ამ სიაში ისეთი, რომელიც იყოფა 5-ზე

array = [12 , 21 , 65 , 19 , 15 , 5]

counter = 0
for i in range (len(array)):
    if array[i] % 5 == 0:
        counter += 1
print(counter)

# 7) შექმენით სია სადაც შეინახავთ რიცხვებს. დაპრინტეთ მხოლოდ ისეთი რიცხვები, რომლებიც იყოფა 4-ზეც და 7-ზეც

array = [28 , 21 , 56 , 21 , 49 , 3]

counter = 0
for i in range (len(array)):
    if array[i] % 4 == 0 and array[i] % 7 == 0:
        print(array[i])

# 8) შექმენით სია სადაც შეინახავთ ნებისმიერ მნიშვნელობებს. დაპრინტეთ მხოლოდ ის ელემენტები, რომლებიც იმყოფებიან ლუწ ინდექსზე

array = [19 , 12 , 22 , 33 , 55 , 112]

for i in range(0 , len(array) , 2):
    print(array[i])

# 9) შექმენით სია სადაც შეინახავთ სიტყვებს. დაითვალეთ იმ სიტყვების რაოდენობა, რომელთა სიგრძეც მეტია 5-ზე

words_list = ["hello" , "hi" , "salam", "bye" , "goodbye"]
i = 0
counter = 0
for i in range (len(words_list)):
    if len(words_list[i]) > 5:
        counter += 1
print(counter) 

# 10) შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო

i = 0
sentence = "GOA is the best"
for i in range(len(sentence)):
    print()

# 11) შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო გარდა გამოტოვებისა

i = 0
sentence = "Python is fun"
for i in range(len(sentence)):
    if sentence[i] != " ":
        print(sentence[i])

# 12) შექმენით სია სადაც შეინახავთ სიტყვებს. for ლუპის გამოყენებით დაპრინტეთ: 'სიტყვა - სიგრძე'

i = 0
sentence_list = ["hex","circle","cool","blue","contact"]
for i in range(len(sentence_list)):
    print(sentence_list[i])