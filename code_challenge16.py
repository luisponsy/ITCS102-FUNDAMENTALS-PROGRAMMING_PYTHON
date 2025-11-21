import os
import json
os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("----------------------------\n")

student_records = {}
while True:
    print("Select From The Options Below\nA-Add Information\nB-Print All Record\nC-Search a Record\nD-Delete a Record\nE-Modify a Record\nF-Export Student Data\nG-Import Student Data\nH-Exit ")

    choice = input("Your choice:           ").lower()

    if choice == 'a':
        print("Adding Student Information.")
        print("--------------------------------")
        student_id= input("Key search for this student:")

        first_name = input("Input Student First Name:").upper()
        last_name = input("Input Student Last Name:").upper()
        course = input("Input Student Course:").upper()
        email = input("Input Student E-mail Address:")

        student_records[student_id]=[]
        print("Data Saved.")

        student_records = {student_id: [first_name, last_name, course, email]}
        print("Data Saved.")

        os.system('cls')
        continue
    elif choice == 'b':
        print("=======================")
        print("Printing Student Record.")
        print("=======================")

        for id, record in student_records.items():
            print(f"Student ID {id} in Student Record {record}")
            continue

    elif choice == 'c':
        os.system('cls')
        print("Search Student Record.")
        print("==================================")

        search_id = input("Input ID to search:").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("=====================")
                print("Record Found.")
                print("=====================")
                for i in student_records[student_id]:
                    print(f"--{i}")
            else:
                print("=====================")
                print("No Existing Record.")
                print("=====================")
        pass
        continue
    elif choice == 'd':
        print("Delete Existing Record.")
        search_id = input("Input ID to search:").lower()
        if search_id in student_records.keys():
                print("=====================")
                print("Record Found.")
                print("=====================")
                for i in student_records[student_id]:
                    print(f"--{i}")
                student_records.pop(search_id)
                print("Record Deleted.")
        else:
                print("=====================")
                print("\nNo Existing Record.")
                print("=====================")
        continue
    elif choice == 'e':
        for i,j in student_records.items():
            search_id = input("Input ID to search:").lower()
            print("Editing Existing Record.")
            first_name = input("Input New Student First Name:").upper()
            last_name = input("Input New Student Last Name:").upper()
            course = input("Input New Student Course:").upper()
            email = input("Input New Student E-mail Address:").upper()

            student_records[student_id][0] = first_name
            student_records[student_id][1] = last_name
            student_records[student_id][2] = course
            student_records[student_id][3] = email
            ("=====================")
            print("Data Updated.")
            ("=====================")
        else:
            ("=====================")
            print("\nNo Existing Record.")
            print("=====================")
        continue
    elif choice == 'f':
        os.system('cls')
        print("Export Student Data.")
                #file name, read / write
        with open('student_record.json','w') as new_file:
            json.dump(student_records, new_file, indent=4)
        student_records = student_json
        print("Data Exported to Json.")
    elif choice == 'g':
        os.system('cls')
        print("Import Student Data.")
                #file name, read / write
        with open('student_record.json','r') as new_file:
            student_json = json.load(new_file)
            student_records = student_json
            print("Data Imported to Json.")
        continue
    elif choice == 'h':
        print("Exit.")
        break