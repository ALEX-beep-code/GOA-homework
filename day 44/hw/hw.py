#powers of 2

#https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python

def powers_of_two(n):
    new = []
    for i in range(n + 1):
        if n < 0:
            break
        new.append(2**i)
    return new

# Reversed Words

#https://www.codewars.com/kata/51c8991dee245d7ddf00000e

def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)

# L1: Set Alarm

# https://www.codewars.com/kata/568dcc3c7f12767a62000038

def set_alarm(employed, vacation):
    return employed == True and vacation == False

# Correct the mistakes of the character recognition software

# https://www.codewars.com/kata/577bd026df78c19bca0002c0

def correct(s):
    new = ""
    for i in range(len(s)):
        if s[i] == "5":
            new += "S"
        elif s[i] == "0":
            new += "O"
        elif s[i] == "1":
            new += "I"
        else:
            new += s[i]
    return new

#Student's Final Grade

#https://www.codewars.com/kata/5ad0d8356165e63c140014d4

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and projects >= 5:
        return 90
    if exam > 50 and projects >= 2:
        return 75
    return 0
    
#Count Odd Numbers below n

# https://www.codewars.com/kata/59342039eb450e39970000a6

def odd_count(n):
    return n // 2

# Find Multiples of a Number

# https://www.codewars.com/kata/58ca658cc0d6401f2700045f

def find_multiples(integer, limit):
    numbers = []
    for i in range(integer, limit + 1, integer):
        numbers.append(i)
    return numbers

# https://www.codewars.com/kata/50654ddff44f800200000007

# Short Long Short

def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

# Is it a palindrome?

# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# To square(root) or not to square(root)

# https://www.codewars.com/kata/57f6ad55cca6e045d2000627

def square_or_square_root(arr):
    result = []

    for i in arr:
        root = int(i ** 0.5)

        if root * root == i:
            result.append(root)
        else:
            result.append(i ** 2)

    return result