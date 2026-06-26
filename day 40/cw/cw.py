# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    return str(num)

# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

def make_negative( number ):
    if number > 0:
        number = -number
        return number
    else:
        return number
    
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"