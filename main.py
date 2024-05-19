import json
from functions import *


def main():
    action = None
    student_data = None

    with open('student_record.json', 'r') as file:
        student_data = json.load(file)

    while action != "6":
        print("\n1). Add a Student.\n2). Display all Students.\n3). Search for Student.\n4). Update Student Grade.\n5). Delete a Student.\n6). Exit.\n")
        action = input("\nPlease select one option from above:- ")

        if action == "1":
            add_student(student_data)

        elif action == "2":
            display_all(student_data)

        elif action == "3":
            search_student(student_data)

        elif action == "4":
            update_student(student_data)

        elif action == "5":
            delete_student(student_data)

        elif action == "6":
            exit(student_data)

        else:
            print("\nPlease choose a valid option...!!!\n")


main()
