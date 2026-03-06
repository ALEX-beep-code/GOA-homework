Temperature=float(input("Enter the temperature"))
if Temperature > 30:
    print("ძალიან ცხელია")
elif Temperature > 20:
    print("სასიამოვნო ამინდია")
elif Temperature > 10:
    print("ცოტა ცივა")
elif Temperature > 0:
    print("ძალიან ცივა თვილად ჩაიცვი")
else:
    print("გაიყინები სახლში დარჩი")


score=int(input("enter the score"))
attendence=int(input("enter attendece"))
if score > 80 and attendence > 90:
    print("შენ შესანიშნავად დაწერე გამოცდა")
if score > 50 and attendence > 70:
    print("საშუალოდ დაწერე გამოცდა")
if score > 30 and attendence > 50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")
else:
    print("ჩაიჭერი!")


temp=float(input("enter temperature"))
rain=str(input("is it raining? (yes or no)"))
if temp > 25 and rain == "no":
    print("შესანიშნავი ამინდია სასეირნოდ!")
if temp > 25 and rain == "yes":
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!")
if temp < 10 and rain == "yes":
    print( "სჯობს სახლში დარჩე")
else:
    print("სასიამოვნო ამინდია")

Age=int(input("enter your age"))
is_student=str(input("are you a student? (yes or no?)"))
if Age < 12 or Age >= 65:
    print("ბილეთი უფასოა")
if is_student == "yes" and Age > 12:
    print( "ბილეთი ნახევარ ფასად")
else:
    print("სრული ფასი უნდა გადაიხადო")


username=str(input("enter your username"))
password=str(input("enter your password"))
if username == "admin" and password == "supersecretpassword125":
    print("მოგესალმები, ადმინ!")
if username == "guest" and password == "1234":
    print("მოგესალმები, სტუმარო!")
else:
    print("მომხმარებელი არ მოიძებნა!")