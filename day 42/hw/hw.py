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
    s = s.split()
    new = []
    for i in range(len(s)):
        new.append(s[i * -1])

    return new

print(reverse_words("hello lol"))