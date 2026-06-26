grades = []
teachers = []
students = []

def chains_deco():
    print("════════════════════════════════════════")

def show_grades():
    chains_deco()
    print(f"Current Grades: {grades}")
    chains_deco()

def show_students():
    chains_deco()
    print(students)
    chains_deco()

def show_teachers():
    chains_deco()
    print(teachers)
    chains_deco()

def remove_students():
    chains_deco()
    print(students)
    current_student = input("Enter the student to remove: ")
    
    if current_student in students:
        students.remove(current_student)
        print("Current Students!:", students)
        chains_deco()
        return students
    else:
        print("Student not found!")
        chains_deco()

def remove_teachers():
    chains_deco()
    print(teachers)
    current_teacher = input("Enter the teacher to remove: ")
    
    if current_teacher in teachers:
        students.remove(current_teacher)
        print("Current teachers!:", teachers)
        chains_deco()
        return teachers
    else:
        print("teacher not found!")
        chains_deco()
        return teachers

def remove_grades():
    chains_deco()
    print(f"Current Grades: {grades}")
    points = int(input("Remove Grade: "))
    if points in grades:
        grades.remove(points)
        print(grades)
        chains_deco()
        return grades
    else:
        print("grade not found! ")
        chains_deco()
        return grades

def add_students():
    chains_deco()
    show_students
    student = input("Add Student: ")
    students.append(student)
    print(students)
    yes_or_no = input("do you want to add more: yes or no :  ").lower()
    if yes_or_no == "yes":
        student = input("Add Student: ")
        students.append(student)
        print(students)
        chains_deco()  
        return students  
    else:
        print(f"current students are {students}")
        chains_deco()

def add_grades():
    print(f"Current Grades: {grades}")
    point = int(input("Add Grades: "))
    grades.append(point)
    print(grades)
    return grades

def add_teachers():
    chains_deco()
    print(f"current teachers: {teachers}")
    teacher = input("Add teacher: ")
    teachers.append(teacher)
    print(teachers)
    yes_or_no = input("do you want to add more: yes or no :  ").lower()
    if yes_or_no == "yes":
        teacher = input("Add teacher: ")
        teachers.append(teacher)
        print(teachers)
        chains_deco()
        return teachers 
    else:
        print(f"current teachers are {teachers}")
        chains_deco()
        return teachers

def sum_of_grades():
    print(sum(grades))

def instructions():
    chains_deco()
    print("type 0 to stop")
    print("type 1 for instructions")
    print("type 2 to show students")
    print("type 3 to show teachers")
    print("type 4 to show grades")
    print("type 5 to remove students")
    print("type 6 to remove teachers")
    print("type 7 to remove grades")
    print("type 8 to change grades")
    print("type 9 to add students")
    print("type 10 to add teachers")
    print("type 11 to add grades")
    print("type 12 to see the highest grade")
    print("type 13 to see the smallest grade")
    print("type 14 to see the sum of all grades")
    chains_deco()

def change_grade():
    chains_deco()
    print(students)

    index = int(input("Enter student position: "))

    if index >= len(students):
        print("Invalid position")

    print("Current grade:", grades[index])

    new_grade = int(input("Enter new grade: "))
    grades[index] = new_grade

    print(grades)
    chains_deco()
    return grades

def highest_grade():
    print( "the highest grade is",max(grades))

def smallest_grade():
    print("the smallest grade is" , min(grades))

def main():
    print("type 1 for intructions")
    print("                             ")
    while True:
        choice = input("Enter a number 1-?: ")
        
        if choice == "0":
            break
        elif choice == "1":
            instructions()
        elif choice == "2":
            show_students()
        elif choice == "3":
            show_teachers()
        elif choice == "4":
            show_grades()
        elif choice == "5":
            remove_students()
        elif choice == "6":
            remove_teachers()
        elif choice == "7":
            remove_grades()
        elif choice == "8":
            change_grade()
        elif choice == "9":
            add_students()
        elif choice == "10":
            add_teachers()
        elif choice == "11":
            add_grades()
        elif choice == "12":
            highest_grade()
        elif choice == "13":
            smallest_grade()
        elif choice == "14":
            sum_of_grades()
        else:
            print("Try Again")

chains_deco()
print("Hello!" , "How are you? ;)"
"                                             ")
while True:
         email = "email"
         password = "password"
         inp = input("Enter Email: ")
         if inp == email:
            print("Correct Email Continue ")
         else:
            print("Access Denied! ")  

         inp2 = input("Enter Password: ")
         if inp2 == password:
            print("access granted!  hello director! ")
            chains_deco()
            break
         else:
            print("Access Denided! ")
chains_deco()



main()
