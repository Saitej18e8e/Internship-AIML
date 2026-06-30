import os

studname = input("Enter student name: ")
folders = ["Assignment", "Attendance", "Project"]

if not os.path.exists(studname):
    os.mkdir(studname)

    for folder in folders:
        os.mkdir(os.path.join(studname, folder))
        print(f"{folder} folder created successfully.")

    print("All folders created successfully.")

else:
    print("Folder already exists.")