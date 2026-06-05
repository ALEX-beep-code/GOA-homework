# # 1) რა არის ფუნქცია? ახსენით საკუთარი სიტყვებით.

# #ფუნქცია არის კოდის ნაწილი რომელიც კონკრტულ დავალებას ასრულებს

# # 2) რატომ არის ფუნქციები საჭირო პროგრამირებაში? - ჩამოწერეთ მინიმუმ 3 მიზეზი

# #1 კოდის წერის გაადვილებაში
# #2 კოდის წერაში საჭირო დროის დამოკლებაში
# #3 პროგრამის წაკითხვა უფრო ადვილი ხდება

# # 3) რა არის პარამეტრი (Parameter)?

# #პარამეტრი არის ინფორმაცია, რომელსაც ფუნქციას ვაწვდით, რათა იცოდეს რა მონაცემზე იმუშაოს.

# # 4) რა არის არგუმენტი (Argument)?

# #არგუმენტი (Argument) არის მნიშვნელობა, რომელსაც ფუნქციის გამოძახების დროს გადავცემთ.

# # 5) რა განსხვავებაა პარამეტრსა და არგუმენტს შორის?

# # პარამეტრი არის ცვლადი, რომელიც ფუნქციის შექმნის დროს იწერება,
# # ხოლო არგუმენტი არის რეალური მნიშვნელობა, რომელსაც ფუნქციის გამოძახების დროს გადავცემთ.

# # 6) შექმენით ფუნქცია repeat_word(word, count).
# # - ფუნქციამ count-ჯერ უნდა დაბეჭდოს `word`
# # - გამოიყენეთ for ციკლი

# def repeat_word(word , count):
#     for i in range(count):
#         print(word)

# repeat_word("hi" , 12)

# # 7) შექმენით ფუნქცია print_numbers(start, end).
# # - ფუნქციამ უნდა დაბეჭდოს ყველა რიცხვი start-დან end-მდე

# def print_numbers(start , end ):
#     for i in range(start , end):
#         print(i)

# # 8) შექმენით ფუნქცია count_even(numbers).
# # - პარამეტრად მიიღოს სია
# # - დაითვალოს რამდენი ლუწი რიცხვია სიაში
# # - გამოიტანოს შედეგი

# def count_even(numbers):
#     counter = 0
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == 0:
#             counter += 1
#     print("there are " + str(counter) + " even numbers")

# # 9) შექმენით ფუნქცია count_vowels(text).
# # - პარამეტრად მიიღოს სტრინგი
# # - დაითვალოს რამდენი ხმოვანია ტექსტში
# # - გამოიტანოს შედეგი

# def count_vowels(text):
#     text = text.upper()
#     vowels = "AEIOU"
#     counter = 0
#     for letter in text:
#         if letter in vowels:
#             counter += 1
#     print(counter)

# count_vowels("AEIOU")


# # 10) შექმენით ფუნქცია longest_word(words).
# # - პარამეტრად მიიღოს სიტყვების სია
# # - გამოიტანოს ყველაზე გრძელი სიტყვა

# def longest_word(words):
#     longest = ""

#     for i in range(len(words)):
#         if len(words[i]) > len(longest):
#             longest = words[i]

#     print(longest)

# longest_word(["strong", "bold", "html", "br"])

# # 11) შექმენით ფუნქცია filter_long_words(words, n).
# # - პარამეტრად მიიღოს წინადადება
# # - გამოიტანოს მხოლოდ ის სიტყვები, რომელთა სიგრძე n-ზე მეტია

# def filter_long_words(words ,  n):
#     words_list = words.split()
#     for i in range(len(words_list)):
#         if len(words_list[i]) > n:
#             print(words_list[i])

# filter_long_words("hi hello bye" , 3)

# # 12) მომხმარებელს შემოატანინეთ რამდენიმე სახელი ერთი სტრინგის სახით (მაგ: "nika luka ana gio").
# # - split მეთოდით გადააქციეთ სიად
# # - შექმენით ფუნქცია name_lengths(names)
# # - ფუნქციამ თითოეული სახელის გვერდით უნდა დაბეჭდოს მისი სიგრძე

# names = str(input("Enter names"))
# names = names.split()

# def name_lengths(names):
#     for i in range(len(names)):
#         print(names[i] + " " + str(len(names[i])))

# # 13) შექმენით ფუნქცია find_max(numbers).
# # - პარამეტრად მიიღოს რიცხვების სია
# # - ციკლის გამოყენებით იპოვოს ყველაზე დიდი რიცხვი

# def find_max(numbers):
#     biggest = numbers[0]
#     for i in range(len(numbers)):
#         if biggest < numbers[i]:
#             biggest = numbers[i]
#     print(biggest)

# # 15) შექმენით ფუნქცია remove_duplicates(numbers).
# # - პარამეტრად მიიღოს სია
# # - შექმნას ახალი სია დუბლიკატების გარეშე
# # - გამოიტანოს შედეგი

# def remove_duplicates(numbers):
#     new_list = []

#     for i in range(len(numbers)):
#         found = 0

#         for j in range(len(new_list)):
#             if numbers[i] == new_list[j]:
#                 found = 1

#         if found == 0:
#             new_list.append(numbers[i])

#     print(new_list)

# remove_duplicates([1, 2, 2, 3, 4, 4, 5])


# # 16) მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13").
# # - split() მეთოდით დაყავით ელემენტებად
# # - გადააქციეთ integer-ებად
# # - შექმენით ფუნქცია `analyze_numbers(numbers)`
# # - ფუნქციამ უნდა:
# #   - გამოიტანოს ჯამი
# #   - გამოიტანოს საშუალო არითმეტიკული
# #   - გამოიტანოს ყველაზე დიდი რიცხვი
# #   - გამოიტანოს ყველაზე პატარა რიცხვი
# #   - დაითვალოს ლუწი რიცხვების რაოდენობა

numbers = input("enter numbers here")
numbers = numbers.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
def analyize_numbers(numbers):
    Sum = 0
    avarage = 0
    biggest = numbers[0]
    smallest = numbers[0]
    even_numbers = 0

    for i in range(len(numbers)):
        Sum += numbers[i]

    avarage = Sum / len(numbers)

    for i in range(len(numbers)):
        if biggest < numbers[i]:
            biggest = numbers[i]

    for i in range(len(numbers)):
        if smallest > numbers[i]:
            smallest = numbers[i]

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_numbers += 1

    print("sum is " + str(Sum))
    print("average is " + str(avarage))
    print("biggest is " + str(biggest))
    print("smallest is " + str(smallest))
    print("there are " + str(even_numbers) + " even numbers")

analyize_numbers(numbers)