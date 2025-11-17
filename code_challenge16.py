import os
os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("-----------------------------------------------\n")

student_records = {}
while True:
    print("Select From The Options Below\nA-Add Information\nB-Search a Record\nC-Delete a Record\nD-Modify a Record\nP-Print all Data\nE-Exit")

    choice = input("Your choice:           ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("--------------------------------")
        search_code = input("Key search for this student:")

        first_name = input("Input Student First Name:").upper()
        last_name = input("Input Student Last Name:").upper()
        course = input("Input Student Course:").upper()
        email = input("Input Student E-mail Address:")
        isSingle = input("Are you Single (Yes/No):")
        student_records = {search_code : [first_name, last_name, course, email,isSingle]}
        print("DATA SAVED.")

        os.system('cls')
        continue
    elif choice == 'b':
        os.system('cls')
        code = input("Iput Search code:")
        
        for j in student_records.keys():
            if code in student_records.keys():
                print("Record Found.")
                
                for i in student_records[code].values():
                    print(i)
                
            else:
                print("No Record Found.")
        os.system('cls')
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        print("Editing Existing Record.")
        continue
    elif choice == 'p':
        for i,j in student_records.items():
            print(f"Code - {i} STORED INFORMATION:f")
        print("Editing Existing Record.")
        continue
    elif choice == 'e':
        print("System Exit.")
        break