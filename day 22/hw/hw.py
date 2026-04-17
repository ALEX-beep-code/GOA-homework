# 1) შექმენი სტრინგი, სადაც ჩაწერ შენს სახელს.
#   -> დაბეჭდე პირველი სიმბოლო ინდექსის გამოყენებით

name = "Alex"
print(name[0])

# 2) შექმენი სტრინგი, სადაც ჩაწერ შენს გვარს.
#   -> დაბეჭდე ბოლო სიმბოლო ინდექსის გამოყენებით

surname = "Krixeli"
print(surname[6])

# 3) შექმენი სტრინგი: "Python"
#   -> დაბეჭდე მესამე სიმბოლო

array = "Python"
print(array[2])

# 4) შექმენი სტრინგი: "Programming"
#   -> დაბეჭდე პირველი 4 სიმბოლო (სლაისინგით)

GOA = "Programming"
print(GOA[: 3])

# 5) შექმენი სტრინგი: "Computer"
#   -> დაბეჭდე ბოლო 3 სიმბოლო (სლაისინგით)

array = "Computer"
print(array[5 : ])

# 6) შექმენი სტრინგი: "HelloWorld"
#   -> დაბეჭდე შუაში არსებული სიმბოლოები (მაგ: loWo)

Print = "HelloWorld"
print(Print[3 : 7])

# 7) შექმენი სტრინგი: "Georgia"
#   -> დაბეჭდე 2-დან 5-მდე ინდექსზე არსებული სიმბოლოები

country = "Georgia"
print(country[2 : 6])

# 8) შექმენი სტრინგი, სადაც ჩაწერ შენს საყვარელ სიტყვას
#   -> თუ პირველი სიმბოლო არის "A":
#       დაბეჭდე პირველი 3 სიმბოლო
#   -> სხვა შემთხვევაში:
#       დაბეჭდე ბოლო 3 სიმბოლო

favourite_word = "asparagus"
if favourite_word[0] == "A":
    print(favourite_word[0:3])
else:
    print(favourite_word[-3:])

# 9) შექმენი სტრინგი: "Education"
#   -> ამოიღე პირველი და ბოლო სიმბოლო და დაბეჭდე დარჩენილი ნაწილი

study = "Education"
print(study[1:-1])

# 10) შექმენი სტრინგი: "Developer"
#   -> შეაერთე პირველი 3 და ბოლო 3 სიმბოლო (ახალ სტრინგში) და დაბეჭდე

Web = "Developer"
Game = Web[:3] + Web[-3:]
print(Game)

# 11) შექმენი სტრინგი, სადაც ჩაწერ რაიმე წინადადებას
#   -> დაბეჭდე მხოლოდ პირველი სიტყვა (სლაისინგის გამოყენებით)

sentance  = ("Hello my name is Alex")
print(sentance[:5])

# 12) შექმენი სტრინგი: "abcdef"
#   -> დაბეჭდე ყოველი მეორე სიმბოლო

string = "abcdef"
print(string[::2])

# 13) შექმენი სია, სადაც შეინახავ 8 ელემენტს (ნებისმიერი ტიპის)
#   -> დაბეჭდე შუაში არსებული 4 ელემენტი

array = ["Hi" , 2 , 3.5 , True , "Bye" , 6,  5.1 , False]
print(array[2: 6])

# 14) შექმენი სია, სადაც შეინახავ 6 მუსიკოსის სახელს
#   -> დაბეჭდე ბოლო 2 ელემენტი (სლაისინგით)

popular_singers = ["Taylor Swift" , "Drake" , "Bad Bunny" , "The Weeknd" , "Morgan Wallen" , "Kendrick Lamar"]
print(popular_singers[-2:])