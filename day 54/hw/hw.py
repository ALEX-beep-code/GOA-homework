# 1) https://www.codewars.com/kata/5648b12ce68d9daa6b000099

def number(bus_stops):
    people = 0

    for stop in bus_stops:
        people += stop[0]
        people -= stop[1]

    return people

# 2) https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    vowels = "AEIOUaeiou"
    result = ""

    for letter in string_:
        if letter not in vowels:
            result += letter

    return result

# 3) https://www.codewars.com/kata/54ba84be607a92aa900000f1

def is_isogram(string):
    return len(string) == len(set(string.lower()))

# 4) https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    length = len(s)
    middle = length // 2

    if length % 2 == 0:
        return s[middle - 1:middle + 1]
    else:
        return s[middle]

# 5) https://www.codewars.com/kata/55908aad6620c066bc00002a

def xo(s):
    return s.lower().count("x") == s.lower().count("o")

# 6) https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(st):
    result = ""
    count = 1

    for letter in st:
        result += letter.upper() + letter.lower() * (count - 1) + "-"
        count += 1

    return result[:-1]

# 7) https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x):
    result = []

    for name in x:
        if len(name) == 4:
            result.append(name)

    return result

# 8) https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

def reverse_words(s):
    words = s.split(" ")
    result = []

    for word in words:
        result.append(word[::-1])

    return " ".join(result)

# 9) https://www.codewars.com/kata/539ee3b6757843632d00026b

def capitals(word):
    result = []

    for i in range(len(word)):
        if word[i] == word[i].upper():
            result.append(i)

    return result

# 10) https://www.codewars.com/kata/580a4734d6df748060000045

def is_sorted_and_how(arr):
    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            ascending = False
        if arr[i] < arr[i + 1]:
            descending = False

    if ascending:
        return "yes, ascending"
    elif descending:
        return "yes, descending"
    else:
        return "no"