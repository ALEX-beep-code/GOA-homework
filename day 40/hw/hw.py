# Sum of positive

# https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            result += arr[i]
    return result

# String repeat

# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e

def repeat_str(repeat, string):
    if repeat < 0:
        repeat = repeat * -1
    return repeat * string

# Remove First and Last Character

# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

def remove_char(s):
    return s[1:-1]

#square(n) sum

#4) https://www.codewars.com/kata/515e271a311df0350d00000f

def square_sum(numbers):
    numbers2 = []
    for i in range(len(numbers)):
        numbers3 = numbers[i] ** 2
        numbers2.append(numbers3)
    return sum(numbers2)

# Find the smallest integer in the array

# https://www.codewars.com/kata/55a2d7ebe362935a210000b2

def find_smallest_int(arr):
    smallest = arr[0]
    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
    return smallest

#Grasshopper - Summation

#https://www.codewars.com/kata/55d24f55d7dd296eb9000030

def summation(num):
    total = 0
    for i in range(1 , num + 1):
        total += i
    return total

#Counting sheep...

#https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    counter = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            counter += 1
    return counter

#Remove String Spaces

#https://www.codewars.com/kata/57eae20f5500ad98e50002c5

def no_space(x):
    new = []
    for i in range(len(x)):
        if x[i] != " ":
            new.append(x[i])
    return "".join(new)

#Keep Hydrated!

#https://www.codewars.com/kata/582cb0224e56e068d800003c

def litres(time):
    return int(time * 0.5)

#Century From Year

#https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return (year // 100) + 1
