# 1) შექმენით nums სია სადაც ჩაწერთ რენდომ ინტეჯერებს
#   - list comperhension-ის საშუალებით შექმენით ახალი groups სია და იტერაცია მოახდინეთ nums სიაზე/
#   - groups სიაში თითოეული რიცხვი უნდა შეინახოს შემდეგ ფორმატში - "group{number}"

nums = [1, 2, 7, 12, 17]

groups = [f"group{i}" for i in nums if i % 5 == 0 or i % 3 == 0]

print(groups)