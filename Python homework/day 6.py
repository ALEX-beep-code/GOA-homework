#Data-type არის საჭირო სხვადასხვა ინფორმაციის სხვადასხვა ნაირად წარმოდგენისთვის
#input და Output-ის ერთ-ერთი მაგალითი არის მაუსი და კომპიუტერი


Name="Alex"
Age=14
Weight=55.5
print(type(Name))
print(type(Age))
print(type(Weight)) 

Distance=int(input("Enter the distance in kilometers"))
print(Distance * 1000)

number1=int(input("type a random number"))
number2=int(input("enter a random number"))
print(number1 + number2)
print(number2 - number1)
print(number1 * number2)
print(number1 / number2)
print(number1 // number2)

#BMI calculator)
weight=float(input("enter your weight"))
height=int(input("enter your height"))
print(height * height // weight)