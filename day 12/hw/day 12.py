#sequencing - როცა კოდს თანმიმდევრობით წერ მაგალითად: number = 1 და მერე print(number - 1)
#პითონში ინდენტაცია ძალიან მნიშვნელოვან როლს თამაშობს და იგი არის ძალიან საჭირო. მაგალითად ინდენტაცია არის საჭირო ამ მაგალითში
number=12
if number > 10:
    print("number is bigger")
#ეს გამოტოვებული ადგილი არის ინდენტაცია რომელიც პითონმა ავტომატურად ჩამისვა და იგი ამ მაგალითს ინდენტაციის გარეშე თუ არ გავაკეთებთ მაშინ კოდში შეცდომა იქნება.


math = float(input("enter your score in math"))
physics = float(input("enter your score in physics"))
english = float(input("enter your score in english"))
if math >= 90 and english >= 90 and physics >= 90:
    print("კარგი შედეგებია")
    print("ყველა საგანში მაღალი შედეგი გაქვს")
if math >= 70 and english >= 70 and physics >= 70:
    print("კარგი შედეგებია")
    print("სასწავლო წელი წარმატებულია")
if math < 50 or english < 50 or physics < 50:
    print("ერთ-ერთ საგანში დაბალი ქულა გაქვს")
    print("მეტი სწავლა დაგჭირდება")
else:
    print( "შედეგები საშუალოა")
    print("შეგიძლია უკეთესად")


Age = int(input("enter your age"))
has_license = str(input("do you have driver's license? yes or no?"))
is_drunk = (input("yes or no?"))
if Age >= 18 and has_license == "yes" and is_drunk == "no":
    print("შეგიძლია მანქანის მართვა")
    print("უსაფრთხო მგზავრობას გისურვებთ")
if Age >= 18 and has_license == "no" and is_drunk == "no":
    print( "ასაკი საკმარისია")
    print( "მაგრამ მართვის მოწმობა არ გაქვს")
if is_drunk == "yes" or Age < 18 or license == "no":
    print("მანქანის მართვა აკრძალულია")
    print("ეს შეიძლება საშიში იყოს")
else:
    print("მონაცემები ვერ გადამოწმდა")
    print("სცადე თავიდან")


price = float(input("enter the price"))
quantity = int(input("enter the quantity"))
is_member = (input("yes or no?"))
if price >= 100 and quantity >= 3 and is_member == "yes":
    print("დიდი ფასდაკლება მიიღე")
    print("მადლობა ერთგული მომხმარებლობისთვის")
if price >= 100 and quantity >= 3 and is_member == "no":
    print("ფასდაკლება მიიღო")
    print("წევრობის შემთხვევაში უფრო მეტს მიიღებ")
if price < 50 or quantity == 1 or is_member == "no":
    print("ფასდაკლება არ გეკუთვნის")
    print("მეტი პროდუქტი შეიძინე")
else:
    print("მცირე ფასდაკლება მიიღე")
    print("გმადლობთ შენაძენისთვის")


weight = float(input("enter your weight"))
height = float(input("enter your height"))
age = int(input("enter your age"))
BMI = weight/ (height * height)
if BMI < 18.5 and age >= 18:
    print("შენი BMI დაბალია")
    print("შესაძლოა წონის მომატება დაგჭირდეს")
if BMI >= 18.5 and BMI <= 24.9 and age >= 18:
    print("შენი BMI ნორმალურია")
    print("ჯანმრთელ ფორმაში ხარ")
if BMI >= 25 and BMI < 30 or age < 18:
    print("BMI საშუალოზე მაღალია")
    print("ჯანსაღი კვება მნიშვნელოვანია")
if BMI >= 30:
    print("BMI მაღალია")
    print("სასურველია ექიმთან კონსულტაცია")
else:
    print("მონაცემები ვერ დამუშავდა")
    print("სცადე თავიდან")

