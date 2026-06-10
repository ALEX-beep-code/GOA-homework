# 1) ახსენით რას აკეთებს `return` ბრძანება ფუნქციაში და მოიყვანეთ მარტივი მაგალითი.

# return - არის keyword - ი რომელიც გამოიყენება ფუნქციაში მდებარე კოდისთვის ფუნქციის გარეთ მდებარე კოდთან ინტერაქციის საშვალების მისაცემად

def my_function(number):
    result = number * 2
    return result

result = my_function(12)
print(result)

# 2) შექმენით ფუნქცია `greet()`, რომელიც აბრუნებს (return) ტექსტს: `"Hello, World!"`. გამოიძახეთ ფუნქცია და დაპრინტეთ შედეგი.

def greet():
    greeting = "Hello world"
    return greeting

greetin = greet()
print(greetin)
# 3) შექმენით ფუნქცია `square(number)`, რომელიც აბრუნებს რიცხვის კვადრატს. შეამოწმეთ რამდენიმე მნიშვნელობაზე.

def square(number):
    square = number * number
    return square

print(square(2))

# 4) შექმენით ფუნქცია `add(a, b)`, რომელიც აბრუნებს ორი რიცხვის ჯამს. მომხმარებელს შემოატანინეთ ორი რიცხვი და გამოიყენეთ ფუნქცია.


def add(a , b):
    Sum = a + b
    print(Sum)
    return Sum

num_1 = int(input("Enter a number"))
num_2 = int(input("Enter a number"))

add(num_1 , num_2)


# 5) შექმენით ფუნქცია `is_even(number)`, რომელიც აბრუნებს `True`-ს თუ რიცხვი ლუწია და `False`-ს თუ კენტია.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(1))

# 6) შექმენით ფუნქცია `count_vowels(text)`, რომელიც აბრუნებს სტრინგში ხმოვანი ასოების რაოდენობას.

def largest(numbers):
    largest_num = numbers[0]

    for i in range(len(numbers)):
        if largest_num < numbers[i]:
            largest_num = numbers[i]

    return largest_num

largest_number = largest([1, 15, 12, 92])
print("largest is : ", largest_number)

# 8) შექმენით ფუნქცია `sum_list(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს ყველა ელემენტის ჯამს.

def sum_list(numbers):
    Sum = 0
    for i in range(len(numbers)):
        Sum += numbers[i]

    return Sum

Sum_of_numbers = sum_list([12 , 13 , 14])
print("Sum of numbers is : " , Sum_of_numbers)

# 9) შექმენით ფუნქცია `count_letter(text, letter)`, რომელიც აბრუნებს რამდენჯერ გვხვდება კონკრეტული ასო სტრინგში.

def count_letter(text , letter):
    counter = 0
    text = text.lower()
    letter = letter.lower()
    for char in text:
        if char == letter:
            counter += 1

    return counter

amount = count_letter("Dogg" , "g")
print("The amount is : " , amount)

# 10) შექმენით ფუნქცია `filter_even(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს მხოლოდ ლუწი რიცხვების სიას.

def filter_even(numbers):
    even_list = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_list.append(numbers[i])

    return even_list

even_list = filter_even([12 , 1 , 3 , 6 , 3 , 8])
print(even_list)

# 11) მომხმარებელს შემოატანინეთ სახელი. შექმენით ფუნქცია `format_name(name)`, რომელიც აბრუნებს სახელს title ფორმატში (პირველი ასო დიდი, დანარჩენი პატარა).

def format_name(name):
    name = name.title()
    return name

Name = input("Enter your name: ")
Name = format_name(Name)
print(Name)