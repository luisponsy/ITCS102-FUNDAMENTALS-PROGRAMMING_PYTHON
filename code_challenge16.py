import os
os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("----------------------------\n")

student_records = {}
while True:
    print("Select From The Options Below\nA-Add Information\nB-Print All Record\nC-Search a Record\nD-Delete a Record\nE-Modify a Record\nF-Export student\nG-Exit")

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
    elif choice == 'p':
        for i,j in student_records.items():
            print(f"Code - {i} STORED INFORMATION:f")
        print("Editing Existing Record.")
        continue
    elif choice == 'e':
        print("Edit Student Record.")
    elif choice == 'f':
        print("Export Data.")
    elif choice == 'g':
        print("Exit.")
        break