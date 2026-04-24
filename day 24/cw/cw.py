text = str(input("enter your text"))
print(len(text))

numbers = [1 , 2.34 , 9 , 76 , 17.3 , 31 , 900 , 31.1]
for i in range(len(numbers)):
    if numbers[i] % 3 == 0:
        print(numbers[i])