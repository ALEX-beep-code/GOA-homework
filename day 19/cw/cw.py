#შექმენით პროგრამა, რომელიც მომხმარებელს რიცხვს შემოატანინებს მანამ სანამ 0-ს არ შეიყვანს:
#დადებითი რიცხვების რაოდენობა დაითვალეთ
#უარყოფითებისაც
#ბოლოს(ანუ როცა 0 შემოიყვანა) დაპრინტეთ ეს რაოდენობები
number= int(input("enter a number"))
postive = 0
negative = 0
while number != 0:
    if number < 0:
        negative += 1
        number= int(input("enter a number"))
    elif number > 0:
        postive += 1
        number = int(input("enter a number again (0 to stop)"))
print ("positive" + str(postive))
print ( "negative" + str(negative))