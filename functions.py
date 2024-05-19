import json

def add_student(data):
    found = True
    
    name = input("Enter Student Name:- ")
    if len(data) > 0:
        while found:
            roll_no = input("Enter Student Roll No (must be unique):- ")
            
            for student in data:
                if student["roll_no"] == roll_no:
                    found = True
                    print("Student with this roll no already exist...!!!")
                    break
                found = False
    else:
        roll_no = input("Enter Student Roll No (must be unique):- ")
    
    grade = input("Enter Student Grade:- ")

    new_data = {"name": name, "roll_no": roll_no, "grades": grade}
    data.append(new_data)


def display_all(data):
    if len(data) > 0:
        for i, student in enumerate(data, 1):
            print("\nStudent ", i, ":\n", "\t   ", "Name:",
                student["name"], "\n", "\t   ", "Roll No:", student["roll_no"], "\n", "\t   ", "Grades:", student["grades"], "\n")
    else:
        print("\nNo record found...!!!")


def search_student(data):
    roll_no = input("\nEnter student roll_no: ")
    found = False
    for student in data:
        if student["roll_no"] == roll_no:
            print("\nStudent :\n\t Name:", student["name"], "\n\t Roll No:",
                  student["roll_no"], "\n\t Grades:", student["grades"], "\n")
            found = True
            break
    if not found:
        print("\nStudent With This Roll No doesn't exist...!!!")
        

def update_student(data):
    roll_no = input("\nEnter student roll_no: ")
    found = False
    for student in data:
        if student["roll_no"] == roll_no:
            name = input("Update Student's Name: ")
            grade = input("Update Student's Grade: ")
            student["name"] = name
            student["grades"] = grade
            print("\nRecord of Student with roll no",
                    '"', roll_no, '" ', "has been Updated")
            found = True
            break
    if not found:
        print("\nStudent With This Roll No doesn't exist...!!!")
        

def delete_student(data):
    roll_no = input("\nEnter student roll_no: ")
    found = False
    for student in data:
        if student["roll_no"] == roll_no:
            del data[data.index(student)]
            print("\nRecord of Student with roll no",
                    '"', roll_no, '" ', "deleted Successfully")
            found = True
            break
    if not found:
        print("\nStudent With This Roll No doesn't exist...!!!")
        

def exit(data):
    with open('student_record.json', 'w') as file:
        json.dump(data, file)
