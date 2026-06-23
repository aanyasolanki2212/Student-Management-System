f=open("Students.txt","a")
print("Welcome to the Student Management System!")
students=[]
print("You can add students, view students, delete students or searcj students or exit the app.")
print("1.Add Student")
print("2.View Students")
print("3.Delete Student")
print("4.Search Student")
print("5.Exit")
a=int(input("Enter your choice: "))
while a:
    if a==1:
        students.append(input("Enter the name of the student you want to add: "))
        students.append(input("Enter the age of the student you want to add: "))
        students.append(input("Enter the grade of the student you want to add: "))
        print("Student added successfully!")
    elif a==2:
        print("Your students are:")
        for i in students:
            print(f"{i}")
    elif a==3:
        f=open("Students.txt","w")
        student=input("Enter the name of the student you want to delete: ")
        if student in students:
            students.remove(student)
            print("Student deleted successfully!")
        else:
            print("Student not found in the list.")
    elif a==4:
        student=input("Enter the name of the student you want to search: ")
        if student in students:
            print(f"{student} is present in the list.")
        else:
            print(f"{student} is not present in the list.")
    elif a==5:
        print("Exiting the app. Goodbye!")
        break

f.close()