# 1) https://www.codewars.com/kata/5a03b3f6a1c9040084001765

def angle(n):
    return (n - 2) * 180

# 2) https://www.codewars.com/kata/55d1d6d5955ec6365400006d

def round_to_next5(n):
    return ((n + 4) // 5) * 5

# 3) https://www.codewars.com/kata/57a049e253ba33ac5e000212

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 4) https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9

def row_weights(array):
    team1 = 0
    team2 = 0
    for i in range(len(array)):
        if i % 2 == 0:
            team1 += array[i]
        else:
            team2 += array[i]
    return team1 , team2

# 5) https://www.codewars.com/kata/59a96d71dbe3b06c0200009c

def generate_shape(n):
    return "\n".join(["+" * n] * n)

# 6) https://www.codewars.com/kata/556196a6091a7e7f58000018

def largest_pair_sum(numbers):
    numbers.sort()
    return numbers[-1] + numbers[-2]

# 7) https://www.codewars.com/kata/59377c53e66267c8f6000027

def alphabet_war(fight):
    left = fight.count("w") * 4 + fight.count("p") * 3 + fight.count("b") * 2 + fight.count("s")
    right = fight.count("m") * 4 + fight.count("q") * 3 + fight.count("d") * 2 + fight.count("z")

    if left > right:
        return "Left side wins!"
    if right > left:
        return "Right side wins!"
    return "Let's fight again!"

# 8) https://www.codewars.com/kata/57f759bb664021a30300007d

def switcheroo(x):
    result = ""
    for letter in x:
        if letter == "a":
            result += "b"
        elif letter == "b":
            result += "a"
        else:
            result += letter
    return result

# 9) https://www.codewars.com/kata/544a54fd18b8e06d240005c0

def find_smallest(numbers, to_return):
    smallest = min(numbers)

    if to_return == "value":
        return smallest
    else:
        return numbers.index(smallest)