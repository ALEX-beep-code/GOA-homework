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

# Find the smallest integer in the array

# https://www.codewars.com/kata/55a2d7ebe362935a210000b2

def find_smallest_int(arr):
    smallest = arr[0]
    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
    return smallest