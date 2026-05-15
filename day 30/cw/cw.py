word = str(input("Enter a word"))
up_counter = 0
low_counter = 0
for i in range(len(word)):
    if word[i] == word[i].upper():
        up_counter += 1
    else:
        low_counter += 1

print(up_counter)
print(low_counter)