# 1) შექმენით სია სადაც შეინახავთ რაიმე რიცხვებს, მთელებიც და არამთელებიც.
#   - თქცენი დავალებაა შექმნათ ფუნქცია, რომელიც მიიღებს არგუმენტად სიას.
#   - თქვენმა ფუნქციამ უნდა დაპრინტოს მინიმალური და მაქსიმალური რიცხვები (გამოიყენეთ f string)
#   - და უნდა დააბრუნოს ამ რიცხვების კამი

def math (list):
    mini = min(list)
    maximum = max(list)
    summary = sum(list)
    print(f"smallest number is {mini}")
    print(f"biggest number is {maximum}")
    return summary