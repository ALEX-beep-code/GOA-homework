# 1) ახსენით რა არის `tuple` და რით განსხვავდება ის `list`-ისგან.

# tuple - მნიშვნელობების კოლექცია და ასევე მიმდევრობა. მის და ლისტის შორის განსხვავება არის თაფლის შეცვლა არ შეიძლება ხოლო ლისტის კი

# 2) მოიფიქრეთ, რომელ რეალურ სიტუაციებში გამოიყენებდით `tuple`-ს `list`-ის ნაცვლად.

#დაბადების თარიღი

birth_date = 10 , 10 , 2011

# 3) შექმენით ფუნქცია first_and_last(items), რომელიც მიიღებს `tuple`-ს და დააბრუნებს ახალ `tuple`-ს, რომელიც შეიცავს მხოლოდ პირველ და ბოლო ელემენტს.

def first_and_last(items):
    first_last = items[0] , items[-1]
    return first_last 

# 4) შექმენით ფუნქცია middle_element(items), რომელიც მიიღებს კენტსიგრძიან tuple-ს და დააბრუნებს მის შუა ელემენტს.

def middle_element(items):
    return items[len(items) // 2]


# 5) შექმენით ფუნქცია count_occurrences(items, value), რომელიც მიიღებს tuple-ს და ნებისმიერ მნიშვნელობას, შემდეგ კი დააბრუნებს რამდენჯერ გვხვდება ეს მნიშვნელობა tuple-ში. არ გამოიყენოთ count() მეთოდი.

def count_occurrences(items , value):
    count = 0
    for occurences in items:
        if occurences == value:
            count += 1
    return count

# 6) შექმენით ფუნქცია contains_duplicates(items), რომელიც მიიღებს tuple-ს და დააბრუნებს True, თუ მასში რომელიმე ელემენტი მეორდება, წინააღმდეგ შემთხვევაში კი False.

def contains_duplicates(items):
    i2 = 1
    for i in range(len(items)):
        for j in range(i + 1 , len(items)):
            if items[i] == items[j]:
                return True
    return False

# 7) შექმენით ფუნქცია swap_edges(items), რომელიც მიიღებს მინიმუმ ორი ელემენტისგან შემდგარ tuple-ს და დააბრუნებს ახალ tuple-ს, სადაც პირველი და ბოლო ელემენტები ადგილებს გაცვლიან.

def swap_edges(items):
    if len(items) < 2:
        return items
    
    lst = list(items)
    lst[0], lst[-1] = lst[-1], lst[0]
    return tuple(lst)

# 8) მოიძიეთ ინფორმაცია index() მეთოდზე და შექმენით ფუნქცია first_position(items, value), რომელიც დააბრუნებს გადაცემული მნიშვნელობის პირველ ინდექსს.

def first_position(items , value):
    return items.index(value)

# 9) შექმენით ფუნქცია tuple_summary(numbers), რომელიც მიიღებს რიცხვების tuple-ს და დააბრუნებს შემდეგი ფორმატის ტექსტს:
# "რაოდენობა: X | ჯამი: Y | პირველი: A | ბოლო: B"

def tuple_summary(numbers):
    amount = len(numbers)
    summary = sum(numbers)
    first = numbers[0]
    last = numbers[-1]
    return f"Amount: {amount} // Sum: {summary} // First: {first} // Last: {last}"

# 10) შექმენით ფუნქცია reverse_tuple(items), რომელიც მიიღებს tuple-ს და დააბრუნებს მის შებრუნებულ ვერსიას. გამოიყენეთ slicing

def reverse_tuple(items):
    return items[::-1]