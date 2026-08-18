# 1) ახსენით რა არის dictionary-ში key, value და item. მოიყვანეთ თითოეულის მაგალითი.

# Key — სახელია, Value — მისი მნიშვნელობა, ხოლო Item — Key და Value ერთად, მაგალითად: "name": "Alex".

# 2) შექმენით ფუნქცია student_info, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს მასში არსებული ელემენტების რაოდენობას.

def student_info(student):
    return len(student)

# 3) შექმენით ფუნქცია get_student_name, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს "name" key-ის შესაბამის value-ს.

def get_student_name(names):
    return names["name"]

# 4) შექმენით ფუნქცია get_student_age, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს "age" key-ის შესაბამის value-ს.

def get_student_name(ages):
    return ages["age"]

# 5) შექმენით ფუნქცია count_products, რომელიც მიიღებს პროდუქტების dictionary-ს და დააბრუნებს მასში არსებული პროდუქტების რაოდენობას.

def count_products(products):
    return len(products)

# 6) შექმენით ფუნქცია get_price, რომელიც მიიღებს პროდუქტების dictionary-ს და პროდუქტის სახელს და დააბრუნებს შესაბამის ფასს.

def get_price(product_name , products):
    return product_name[products]


# 7) შექმენით ფუნქცია create_student, რომელსაც ექნება name, lastname, age, weight, height, grades, passed_test პარამეტრები. თქვენმა ფუნქციამ უნდა შექმნას dict შესაბამისი key-value ებით.

# 8) შექმენით ფუნქცია print_student, რომელიც მიიღებს მოსწავლის dictionary-ს, რომელსაც ექნება name, lastname, age, weight, height, grades, passed_test გასაღებები.
#   - თქვენმა ფუნქციამ უნდა დაპრინტოს მოსწავლის შესახებ ინფორმაცია შემდეგი ფორმატით:
  
# -- Student Info --
# Name: Zaza
# Lastname: Dumbadze
# Age: 16
# Weight: 78.5
# Height: 1.78
# Grades: 9, 10, 8, 10, 9, 10, 10
# Passed_test: True 
# --- -- -- -- -- --- 