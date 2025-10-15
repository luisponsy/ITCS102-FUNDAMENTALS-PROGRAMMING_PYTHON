isDirty = True
while isDirty == True:
    confirm = input("Do you wish to continue washing (yes/no)").lower()

    if confirm == 'yes':
        print("Continuing the Cycle")

    elif confirm == 'no':
        print("Cycle Stops")
        break
    else:
        print("Invalid Choice")