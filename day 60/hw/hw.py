# 1) შექმენით ფუნქცია get_student_grade, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. get() მეთოდის გამოყენებით მიიღეთ მითითებული მოსწავლის ქულა და დაბეჭდეთ იგი. თუ მოსწავლე dictionary-ში არ არსებობს, დაბეჭდეთ Student not found.

def get_student_grade(students , student):
    if students.get(student) is None:
        return print(f"student not found")
    return print(students.get(student))

# 2) შექმენით ფუნქცია get_product_price, რომელიც მიიღებს პროდუქტების dictionary-ს და პროდუქტის სახელს. get() მეთოდის გამოყენებით მოძებნეთ პროდუქტის ფასი. თუ პროდუქტი არ არსებობს, დააბრუნეთ 0.

def get_product_price(products, product):
    if products.get(product) == None:
        return 0

    return products.get(product)

# 3) შექმენით ფუნქცია remove_student, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. pop() მეთოდის გამოყენებით წაშალეთ მითითებული მოსწავლე dictionary-დან და დაბეჭდეთ მისი ქულა. თუ მოსწავლე არ არსებობს, დაბეჭდეთ Student not found.

def remove_student(students , student):
    if student not in students:
        return print(f"student not found")
    return print(students.pop(student))

# 4) შექმენით ფუნქცია remove_last_item, რომელიც მიიღებს ნებისმიერ dictionary-ს. popitem() მეთოდის გამოყენებით წაშალეთ dictionary-ის ბოლო დამატებული ელემენტი და დაბეჭდეთ წაშლილი key და value.

def remove_last_item(dictionary):
    item = dictionary.popitem()
    print(item[0], item[1])

# 5) შექმენით ფუნქცია remove_items_until_empty, რომელიც მიიღებს dictionary-ს. while ციკლისა და popitem() მეთოდის გამოყენებით სათითაოდ წაშალეთ ყველა ელემენტი dictionary-დან და ყოველ ჯერზე დაბეჭდეთ წაშლილი ელემენტი.

def remove_items_until_empty(dictionary):
    while dictionary:
        item = dictionary.popitem()
        print(item)

# 6) შექმენით ფუნქცია clear_cart, რომელიც მიიღებს კალათის dictionary-ს, სადაც key არის პროდუქტის სახელი, ხოლო value — რაოდენობა. clear() მეთოდის გამოყენებით გაასუფთავეთ კალათა და დაბეჭდეთ საბოლოო dictionary.

def clear_cart(cart):
    cart.clear()
    print(cart)

# 7) შექმენით ფუნქცია copy_students, რომელიც მიიღებს მოსწავლეების dictionary-ს. copy() მეთოდის გამოყენებით შექმენით მისი ასლი და დააბრუნეთ ახალი dictionary.

def copy_students(students):
    return students.copy()

# 8) შექმენით ფუნქცია update_copy, რომელიც მიიღებს პროდუქტების dictionary-ს. copy() მეთოდის გამოყენებით შექმენით dictionary-ის ასლი. ასლში შეცვალეთ ერთი პროდუქტის ფასი და შემდეგ დაბეჭდეთ როგორც ორიგინალი dictionary, ასევე მისი ასლი. შეამოწმეთ შეიცვალა თუ არა ორიგინალი.

def update_copy(products):
    copy_products = products.copy()

    copy_products["apple"] = 10

    print(products)
    print(copy_products)

# 9) შექმენით ფუნქცია safe_remove, რომელიც მიიღებს dictionary-ს და key-ს. ჯერ get() მეთოდის გამოყენებით შეამოწმეთ არსებობს თუ არა ეს key. თუ არსებობს, pop() მეთოდის გამოყენებით წაშალეთ იგი და დაბეჭდეთ მისი value. წინააღმდეგ შემთხვევაში დაბეჭდეთ Key not found.

def safe_remove(dictionary, key):
    if dictionary.get(key) is None:
        return print("Key not found")

    print(dictionary.pop(key))

# 10) შექმენით ფუნქცია copy_and_clear, რომელიც მიიღებს dictionary-ს. copy() მეთოდის გამოყენებით შექმენით მისი ასლი, შემდეგ clear() მეთოდის გამოყენებით გაასუფთავეთ ორიგინალი dictionary. დაბეჭდეთ ორივე dictionary და შეადარეთ შედეგები.

def copy_and_clear(dictionary):
    copy_dictionary = dictionary.copy()

    dictionary.clear()

    print(dictionary)
    print(copy_dictionary)

# 11) შექმენით ფუნქცია manage_students, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. get() მეთოდით მოძებნეთ მოსწავლე. თუ მისი ქულა 50-ზე ნაკლებია, pop() მეთოდით წაშალეთ იგი dictionary-დან. თუ მოსწავლე არ არსებობს, დაბეჭდეთ Student not found.

def manage_students(students, student):
    if student not in students:
        return print("Student not found")

    if students.get(student) < 50:
        return print(students.pop(student))
    
# 12) შექმენით ფუნქცია backup_dictionary, რომელიც მიიღებს dictionary-ს. copy() მეთოდის გამოყენებით შექმენით სარეზერვო ასლი. შემდეგ clear() მეთოდით გაასუფთავეთ ორიგინალი dictionary. დააბრუნეთ სარეზერვო ასლი.

def backup_dictionary(dictionary):
    backup = dictionary.copy()
    dictionary.clear()
    return backup