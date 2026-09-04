# # 1. — 5 ქულა
# # მომხმარებელს შეაყვანინე ორი რიცხვი და დაბეჭდე:
# # •    ჯამი 
# # •    სხვაობა 
# # •    ნამრავლი 
# # •    / 
# # •    // 
# # •    % 
# # ________________________________________

# user_number1 = int(input("enter a number"))
# user_number2 = int(input("enter a number"))
# print(user_number1 + user_number2)
# print(user_number1 - user_number2)
# print(user_number1 * user_number2)
# print(user_number1 / user_number2)
# print(user_number1 // user_number2)
# print(user_number1 % user_number2)


# # 2. — 5 ქულა
# # მომხმარებელს შეაყვანინე რიცხვი.
# # დაბეჭდე:
# # •    Positive — თუ დადებითია 
# # •    Zero — თუ ნულია 
# # •    Negative — თუ უარყოფითია 
# # ________________________________________

# user_number = int(input("enter a number"))
# if user_number > 0:
#     print("positive")
# if user_number == 0:
#     print("Zero")
# if user_number < 0:
#     print("Negative")


# # 3. — 5 ქულა
# # მომხმარებელს შეაყვანინე ორი რიცხვი.
# # შეამოწმე:
# # •    ორივე რიცხვი 10-ზე მეტია თუ არა; 
# # •    რომელიმე მათგანი 100-ზე მეტია თუ არა; 
# # •    პირველი მეორეზე მეტია თუ არა. 
# # გამოიყენე and და or.

# user_number1 = int(input("enter a number"))
# user_number2 = int(input("enter a number"))
# if user_number1 > 10 and user_number2 > 10:
#     print("true")
# else:
#     print("false")
# if user_number1 > 100 or user_number2 > 100:
#     print("true")
# else:
#     print("false")
# if user_number1 > user_number2:
#     print("true")
# else: 
#     print("false")

# 4. — 10 ქულა
# მომხმარებელს შეაყვანინე ქულა.
# დაბეჭდე:
# •    A — 90 ან მეტი 
# # •    B — 70 ან მეტი 
# # •    C — 50 ან მეტი 
# # •    Failed — 50-ზე ნაკლები

# user_number = int(input("enter a number"))
# if user_number >= 90:
#     print("A")
# elif user_number >= 70:
#     print("B")
# elif user_number >= 50:
#     print("C")
# else:
#     print("failed")

# 5. — 10 ქულა
# შექმენი:
# balance = 1000
# მომხმარებელს შეაყვანინე თანხა.
# თუ თანხა დადებითია, შეამოწმე ბალანსი:
# •    თუ თანხა ბალანსზე ნაკლები ან ტოლია → Withdrawal successful 
# •    თუ მეტია → Insufficient balance 
# # თუ თანხა 0 ან უარყოფითია:
# # Invalid amount

# balance = 1000
# user_amount = int(input("enter a number"))
# if user_amount > 0:
#     if user_amount == balance or user_amount < balance:
#         print("widthdrawal successful")
#     elif user_amount > balance:
#         print("insufficient balance")
#     else:
#         print("invalid amount")

# # 6. — 7 ქულა
# მომხმარებელს შეაყვანინე n.
# while loop-ის გამოყენებით დათვალე 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი.
# ________________________________________

# n = int(input("enter a number"))
# result = 0
# i = 2
# while i < n:
#     result += i
#     i += 2

# print(result)


# 7. — 8 ქულა
# მომხმარებელს მუდმივად შეაყვანინე რიცხვები.
# •    დადებითი → დაამატე total-ში 
# •    უარყოფითი → გამოტოვე 
# •    0 → break 
# •    ბოლოს დაბეჭდე total 
# მაგალითად:
# 5
# -3
# 10
# -2
# 7
# 0
# შედეგი:
# 22

# total = 0
# while 1 > 0:
#     user_number = int(input("enter a number"))
#     if user_number > 0:
#         total += user_number
#     elif user_number == 0:
#         break

# print(total)

# 8. — 5 ქულა
# მოკლედ ახსენი:
# •    რა არის set; 
# •    რით განსხვავდება list-ისა და tuple-ისგან; 
# •    როდის გამოვიყენებდით set-ს რეალურ სიტუაციაში. 
# ________________________________________

#სეტი არის დაულაგებელი მიმდევრობა რომელიც თაფლის გან და ლისტის გან ყველაზე მეტად განსხვავდება იმით რომ ინდექსები არააქ და დუპლიკატებს შლის სეტი ყველაზე ხშირად მაშინ გამოიყენება როდესაც დუპლიკატების წაშლა გვჭირდება

# 9. — 5 ქულა
# შექმენი ფუნქცია:
# unique_letters(text)
# რომელიც დააბრუნებს ტექსტში არსებულ უნიკალურ სიმბოლოებს set-ის სახით.
# მაგალითად:
# unique_letters("banana")
# შედეგი უნდა შეიცავდეს:
# {'b', 'a', 'n'}
# ________________________________________

# def unique_letters(text):
#     return set(text)

# print(unique_letters("hello"))

# 10. — 5 ქულა
# შექმენი ფუნქცია:
# common_elements(first, second)
# რომელიც დააბრუნებს ორივე set-ში არსებულ საერთო ელემენტებს.
# აკრძალულია: intersection().
# გამოიყენე ციკლი და პირობა.

def common_elemts(first , second):
    first = list(first)
    second = list(second)
    common = []
    for i in range(len(first)):
        if first[i] in second:
            common.append(first[i])
    common = set(common)
    return common

print(common_elemts({1 , 2 , 3 , 4} , {2 , 4 , 5}))

# 11. — 5 ქულა
# მოცემულია:
# students = {
#     "Giorgi": 80,
#     "Nika": 45,
#     "Ana": 92,
#     "Luka": 30
# }
# შექმენი ფუნქცია:
# count_passed_students(students)
# რომელიც items()-ის გამოყენებით დაითვლის, რამდენ მოსწავლეს აქვს 50 ან მეტი ქულა.
# ________________________________________

# students = {
#      "Giorgi": 80,
#      "Nika": 45,
#      "Ana": 92,
#      "Luka": 30
# }

# def count_passed_students(students):
#     count = 0
#     for name , i in students.items():
#         if i > 50:
#             count += 1

#     return count

# print(count_passed_students(students))

# 12. — 5 ქულა
# შექმენი ფუნქცია:
# find_expensive_products(products)
# რომელიც მიიღებს პროდუქტების dictionary-ს და items()-ის გამოყენებით დაბეჭდავს მხოლოდ იმ პროდუქტებს, რომელთა ფასი 100-ზე მეტია.
# ________________________________________

# products = {
#      "Apple": 80,
#      "strawberry": 150,
#      "banana": 120 ,
#      "berry": 90
# }

# def find_expensive_products(products):
#     count = 0
#     for  product , i in products.items():
#         if i > 100:
#             count += 1

#     return count

# print(find_expensive_products(products))
    

# 13. — 5 ქულა
# შექმენი ფუნქცია:
# create_student(name, lastname, age, weight, height, grades, passed_test)
# ფუნქციამ უნდა შექმნას და დააბრუნოს dictionary შესაბამისი key-value წყვილებით.
# მაგალითად:
# name
# lastname
# age
# weight
# height
# grades
# passed_test

# def create_student(name , lastname , age , weight , height , grades , passed_test):
#     student = {
#         "name": name,
#         "lastname" : lastname,
#         "age" : age,
#         "weight": weight,
#         "height": height,
#         "grades": grades,
#         "passed_test": passed_test 
#     }
#     return student


# შექმენი პატარა Student Management Program.
# პროგრამაში გქონდეს:

students = {
    "Giorgi": 85,
    "Nika": 45,
    "Ana": 92
}

# პროგრამამ:
# 1.    while loop-ით მომხმარებელს ჰკითხოს მოსწავლის სახელი; 
# 2.    თუ სახელი არის "exit" → გამოიყენოს break; 
# 3.    თუ მოსწავლე არსებობს → დაბეჭდოს მისი ქულა; 
# 4.    თუ ქულა 50 ან მეტია → დაბეჭდოს Passed; 
# 5.    წინააღმდეგ შემთხვევაში → Failed; 
# 6.    თუ მოსწავლე dictionary-ში არ არსებობს → დაბეჭდოს Student not found. 
# ამ დავალებაში მოწმდება:
# dictionary + while + if/else + break + ფუნქციონალური ლოგიკა.

i = 0
while 1 > 0:
    user_request = str(input("enter your request"))
    if user_request == "exit":
        break
    if user_request in students:
        print(students.get(user_request))
        if students.get(user_request) >= 50:
            print("passed")
        else: print("failed")
    if user_request not in students:
        print("student not found")

