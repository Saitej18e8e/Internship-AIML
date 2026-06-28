
def addNewstud():
    name=input("Enter student name:")
    with open("studentInfo.txt","a") as file:
        file.write(name +"\n")
    print("student added successfully")

def viewStudent():
    try:
        with open("studentInfo.txt","r")as file:
            student=file.readlines()
        if(len(student)==0):
            print("No student")
        else:
            print("=====Student Info=====")
            for i,student in enumerate(student,start=1):
                print(f"{i}.{student.strip()}")
    except FileNotFoundError:
        print("No such file")

while True:
    print("======student record manager")
    print("1. Add Student")
    print("2. View Students")
    print("3.Exit")

    choice=input("Enter choice:")

    if(choice == "1"):
        addNewstud()
    elif(choice == "2"):
        viewStudent()
    elif(choice == "3"):
        print("Thank u")
        break
    else:
        print("Invalid choice")