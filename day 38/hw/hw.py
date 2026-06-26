# 1) აღსენით დღეს ნასწავლი 3 ფუნქცია: `min()`, `max()`, `sum()`

# min() – აბრუნებს სიაში არსებულ ყველაზე პატარა მნიშვნელობას.
# მაგალითი: min([3, 7, 1, 9]) = 1

# max() – აბრუნებს სიაში არსებულ ყველაზე დიდ მნიშვნელობას.
# მაგალითი: max([3, 7, 1, 9]) = 9

# sum() – კრებს სიაში არსებულ ყველა რიცხვს და უმატებს ერთმანეთს

#მაგალითი : sum([12 , 3 , 7]) = 22

# 2) მოიფიქრეთ თუ როგორ გამოიყენებთ მათ პრაქტიკაში

# min() – გამოვიყენებ პროდუქტების ფასებიდან ყველაზე იაფი პროდუქტის საპოვნელად.

# max() – გამოვიყენებ პროდუქტების ფასებიდან ყველაზე ძვირი პროდუქტის საპოვნელად.

# sum() – გამოვიყენებ ყველა პროდუქტის ფასის შესაკრებად, რათა გავიგო საერთო ღირებულება.

# 3) შექმენით ფუნქცია `max_difference(numbers)`, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სხვაობას ყველაზე დიდ და ყველაზე პატარა ელემენტს შორის.
# მაგალითი:
# [8, 3, 15, 6] -> 12
# გამოიყენეთ `max()` და `min()` ფუნქციები.

def max_difference(numbers):
    difference = max(numbers) - min(numbers)
    
    return difference

print(max_difference([12 , 3 , 6]))

# 4) შექმენით ფუნქცია `unique_characters(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს სიას იმ სიმბოლოებისგან, რომლებიც ტექსტში მხოლოდ ერთხელ გვხვდება.
# მაგალითი:
# "banana" -> ["b", "n"]

def unique_charachters(text):
    unique_chars = []
    for i in range (len(text)):
        if text[i] not in unique_chars:
            unique_chars.append(text[i])

    return unique_chars

# 5) შექმენით ფუნქცია `highest_char(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს იმ სიმბოლოს, რომელსაც ყველაზე დიდი char code აქვს.
# მაგალითი:
# "Az9" → "z"
# გამოიყენეთ `max()` ფუნქცია.

def highest_char(text):
    highest_charachter = max(text)

    return highest_charachter

# 6) შექმენით ფუნქცია `numbers_summary(numbers)`, რომელიც მიიღებს რიცხვების სიას და **დააბრუნებს** შემდეგი ფორმატის ტექსტს:
# მაგალითი:
# [5, 10, 15]
# შედეგი:
# "რაოდენობა: 3 | ჯამი: 30 | მინიმალური: 5 | მაქსიმალური: 15"

def numbers_summary(numbers):
    return f"count: {len(numbers)} // summary: {sum(numbers)} // smallest number: {min(numbers)} // biggest number: {max(numbers)}"

# 7) მოიძიეთ ინფორმაცია `ord()` ფუნქციაზე და შექმენით ფუნქცია `char_code_sum(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს მის ყველა სიმბოლოს char code-ების ჯამს.
# მაგალითი:
# "ABC" -> 198

def char_code_sum(text):
    summary = 0
    for i in range(len(text)):
        summary += ord(text[i])
    
    return summary