# 1) https://www.codewars.com/kata/59cfc000aeb2844d16000075

def capitalize(s):
    s = list(s)
    s2 = s.copy()
    arr = []
    for i in range(0 , len(s) , 2):
        s[i] = s[i].upper()
    s = "".join(s)
    arr.append(s)
    for i in range(1 , len(s2) , 2):
        s2[i] = s2[i].upper()
    s2 = "".join(s2)
    arr.append(s2)
    return arr

# 2) https://www.codewars.com/kata/5aff237c578a14752d0035ae

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    mult = []
    for i in range(len(ages)):
        mult.append(ages[i] ** 2)
    total = sum(mult)
    root = (total ** 0.5) / 2
    return int(root)

# 3) https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c

def even_numbers(arr,n):
    empty = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            empty.append(arr[i])
    pos = len(empty) - n
    return empty[pos:]

# 4) https://www.codewars.com/kata/59a96d71dbe3b06c0200009c

def generate_shape(n):
    emp = []
    for i in range(n):
        emp.append("+" * n)
    emp = "\n".join(emp)
    return emp

# 5) https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3

def sort_gift_code(code):
    code = list(code)
    code.sort()
    code = "".join(code)
    return code

# 6) https://www.codewars.com/kata/5b39e3772ae7545f650000fc\

def remove_duplicate_words(s):
    s = s.split()
    emp = []
    for word in s:
        if word not in emp:
            emp.append(word)
    return " ".join(emp)

# 7) https://www.codewars.com/kata/59706036f6e5d1e22d000016

def word_value(word):
    total = 0

    for letter in word:
        total += ord(letter) - 96

    return total

# 8) https://www.codewars.com/kata/5680781b6b7c2be860000036

def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    result = []

    for i in range(len(word)):
        if word[i] in vowels:
            result.append(i + 1)

    return result

# 9) https://www.codewars.com/kata/556196a6091a7e7f58000018

def largest_pair_sum(numbers): 
    largest = max(numbers)
    numbers.remove(max(numbers))
    largest2 = max(numbers)
    return largest + largest2

# 10) https://www.codewars.com/kata/580755730b5a77650500010c 

def sort_my_string(s):
    even = ""
    odd = ""

    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]

    return even + " " + odd