import os 
import random
import json
import time
from getpass import getpass
def activity1():
    print ("Hello World")

def activity2():
    name = input("What is your name?:")
    print("Hi", name,"Welcome to the Matrix.")  

def activity3():
    print("Good \n Morning \n Sa'yo")
    print("Kamusta \tka na?")

def activity4():
    name = input("Enter a string -> ") 
    print("Your name has ",len (name), "characters")

def activity5():
    something =eval(input("Input something ->"))
    print ("The data type of something is", type (something)) 
    answer = 6 + something
    print("the answer is ", answer)

def activity6():
    n1 = eval(input("Enter the first number : "))
    n2 = eval(input("Enter the second number : "))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2

    print("\nThe sum of",n1,"and",n2,"is",s)
    print("The difference of", n1,"and",n2,"is",d)
    print("The product of",n1,"and",n2,"is",p)
    print("The quotient of",n1,"and",n2,"is",q)
    print(n1,"exponent by",n2,"is",n1**n2)
    print("The remainder of",n1,"and",n2,"is",n1 % n2)
    print("The floor division of",n1,"and",n2,"is",n1//n2)

def activity7():
    a = 1

    print("The value of a is:", a)

    a += 564548711
    print("The value of a is:", a)

    a -= 75477444
    print("The value of a is:", a)

    a *= 2
    print("The value of a is:", a)

    a /= 4
    print("The value of a is:", a)

def activity8():
    a = 'pogi ba'
    b = 'ako?'
    print('a' != 'b')

def activity9():
    username = 'luis'
    password = '0123456789'
    #print((username == 'luis') and (password == '0123456789'))
    print((username == 'luis') or (password =='0123456789'))

def activity10():
    name = input("Input your name :")
    isStudent = input("Are you a student (Yes / No):")
    fare = eval(input("bayad:"))

    if isStudent.lower()== "yes":
	    discount = fare * .2
	    new_fare = fare - discount
	    print("Hi", name, "Student discount is:", discount, "Discounted fare is", new_fare)

    else: 
	    print("Sorry,", name,"you are not eligible for the student discount") 
          
def activity11():
#create a program that accepts float value
#determine temperature reading 
#1 to 20 cold
#21 to 30 lukewarm
#31 to 40 warm
#41 to 50 hot

    temp = eval(input("Enter temperature:"))

    if temp >= 1 and temp <=20:
	    print("Temperature outside is cold")
    elif temp >= 21 and temp <=30:
	    print("Temperature outside is lukewarm")
    elif temp >= 31 and temp <=40:
	    print("Temperature outside is warm")
    elif temp >= 41 and temp <=50:
	    print("Temperature outside is hot")
    else:
	    print("invalid temperature")

def activity12():
    for ikot in range (11):
        print(ikot,'Hello World')

def activity13():
    numero = 0
    for basta in range (10):
        num = eval(input('Maglagay ng Numero:'))
        numero += num
        print('Sumatotal:',numero)
    
def activity14():
    for basta in range (21, 0, -1):
        print ('basta')

def activity15():
    #APPLYING FORMAT IN FACTORIAL PROGRAM
    print("Welcome to the Factorial Program!") 
    num = eval(input("Enter a number:"))
    number = 1 
    for x in range(num,0,-1):
        number *= x
    print(f"The Factorial of {num} is number {number}")    

def activity16():
    #using loop to print 1 - 10 horizontally
    for i in range (1,11,1):
        print(i,end=",")

def activity17():
    for x in range  (1,11,1):
        for i in range(1,11,1):
            print(i,end=" ")
        print()

def activity18():
    for x in range (1,11,1):
        for y in range (1,x,1):
            print (y, end=" ")
        print()

def activity19():
    for x in range (1,11,1):
        for y in range (1,x,1):
            print ("*", end=" ")
        print()

def activity20():
    for x in range (1,11,1):
    # for y in range (1,x,1):
        # print(" ", end=" ")
        for z in range (10,x,-1):
            print("*",end=" ")
        print()

def activity21():
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

def activity22():
    x = random.randint(1,10)
    while True:
        y = eval(input("Guess the number!(1 - 10):"))
        if y == x:
            print(f"Number: {y} You Win!")
            break
        else:
            print("Incorrect Number, Try Again!")  
  
def activity23():
    x = ['January','February','March','April','May','June','July']

    x.insert(7,"August")
    print(x)
    x.append("September")
    print(x)
    x.pop(8)
    print(x)
    x.remove("August")
    print(x)

    for i in x:
        print(i)

    full_name = 'Luis Ponsy Atienza Buñag'
    for i in full_name[0:1]:
        print(i)
    for i in full_name[::-1]:
        print(i)

    x.reverse()
    print(x)

    y = list(full_name)
    y.reverse()
    print(y)

def activity24():
    def greet(name):\
        print(f"hi {name} kamusta ka na?")

    def summation(x):
        sum = 0
        for y in range (x, 0, -1):
            sum += y 
        print(f"The sum of {x} is {sum} ")
    greet("Luis")
    summation(18)

def activity24_1():
    def greet(name):
        print(f"hi {name} kamusta ka na?")

    def summation(x):
        sum = 0
        for y in range (x, 0, -1):
            sum += y 
        print(f"The sum of {x} is {sum} ")
    greet("Luis")
    summation(18)   

def activity25():
     print("Activity 25 is just like this program.")

def activity26():
    programming_language = ['Python','TurboC','C++','JavaScript','Perl','Java' ]
    promramming_language2 = {'madali':'Python','medyo luma na':'TurboC','mas mahirap':'C++','pang lolo':'JavaScript','':'Perl','':'Java'}
    print(programming_language[4])

def activity27():
    print("Adding Data to Dictionary")
    print("==============")
    tuloy = True
    empty_dictionary = {}
    def print_anime():
        for i,j in empty_dictionary.items():
            print(f"CODE:{i} TITLE:{j}")
    def pang_search(key):
        print("Searching...")
        print(f"result shows {empty_dictionary[key].upper()} on our database")
        while tuloy == True:
            keys = input("Input keys for this anime:")
            value = input("Enter anime title:")
            empty_dictionary[keys] = value
            choice = input("Would you like to continue adding anime \ny-Yes\nn-No\np-Print\ns-Search/n:").lower()
            if choice == 'y':
                print("Continuing")
                continue
            elif choice == 'n':
                print("Program Stops")
                break
            elif choice == 'p':
                print_anime()
                continue
            elif choice == 's':
                code = input("Please input the code of the anime:")
                pang_search(code)
            else:
                print("Invalid Choice")
                continue
def code_challenge1():
    name = input("what is your name?")
    print("\t          * \n\t        *   *       \n\t      *       *  \n\t    *           *  \n\t  *      Hi \t  *\n\t*\t",name,"\t    *\n\t  *               *  \n\t    *           *\n\t      *       *\n\t        *   *\n\t          *")

def code_challenge2():
    amount = int(input("Enter amount to deposit: "))

    print("Here is a breakdown using PH denomination:")

    print("PHP 1000:", amount // 1000)
    amount = amount % 1000

    print("PHP 500:", amount // 500)
    amount = amount % 500

    print("PHP 200:", amount // 200)
    amount = amount % 200

    print("PHP 100:", amount // 100)
    amount = amount % 100

    print("PHP 50:", amount // 50)
    amount = amount % 50

    print("PHP 20:", amount // 20)
    amount = amount % 20

    print("PHP 10:", amount // 10)
    amount = amount % 10

    print("PHP 5:", amount // 5)
    amount = amount % 5

    print("PHP 1:", amount // 1)
def code_challenge3():
    username="luis"
    password="123"

    user = input("Enter username:")
    passwrd = getpass("Enter password:")

    if username == user and passwrd == password:
	    print("Access Granted")

    else:
	    print("Access Denied")

def code_challenge4():
    number = (eval(input("Input a number:")))

    answer = number % 2
    if answer == 0:
	    print("The number is even")
    else:
	    print("The number is odd")

def code_challenge5():
    print("Welcome to Manga Reader Recommendation!")

    print("Please select a genre:")
    genre = input("1. Romance\n2. Comedy\n3. Action\nEnter the number of your choice: ")

    print("\nWhat is your preferred manga length?")
    length = input("1. Short\n2. Medium\n3. Long\nEnter the number of your choice: ")

    print("\nWhich decade do you prefer?")
    decade = input("1. 2000s\n2. 2010s\nEnter the number of your choice: ")

    if genre == "1":
        if length == "1":  
            if decade == "1":
                print("\nRecommendation: Lovely Complex (2000s)")
            else:
                print("\nRecommendation: Kimi ni Todoke (2010s)")
        elif length == "2":  
            if decade == "1":
                print("\nRecommendation: Fruits Basket (2000s)")
            else:
                print("\nRecommendation: My Little Monster (2010s)")
        else:  
            if decade == "1":
                print("\nRecommendation: Nana (2000s)")
            else:
                print("\nRecommendation: Your Lie in April (2010s)")
    elif genre == "2":  
        if length == "1":  
            if decade == "1":
                print("\nRecommendation: Azumanga Daioh (2000s)")
            else:
                print("\nRecommendation: Barakamon (2010s)")
        elif length == "2":  
            if decade == "1":
                print("\nRecommendation: One Punch Man (2000s)")
            else:
                print("\nRecommendation: Gintama (2010s)")
        else:  
            if decade == "1":
                print("\nRecommendation: One Piece (2000s)")
            else:
                print("\nRecommendation: KonoSuba (2010s)")
    elif genre == "3":  
        if length == "1": 
            if decade == "1":
                print("\nRecommendation: Death Note (2000s)")
            else:
                print("\nRecommendation: Attack on Titan (2010s)")
        elif length == "2":  
            if decade == "1":
                print("\nRecommendation: Naruto (2000s)")
            else:
                print("\nRecommendation: Demon Slayer (2010s)")
        else:  
            if decade == "1":
                print("\nRecommendation: Bleach (2000s)")
            else:
                print("\nRecommendation: My Hero Academia (2010s)")
    else:
        print("Invalid input.")

def code_challenge6():
    #FACTORIAL PROGRAM
    print("Welcome to the Factorial Program!")

    num = int(input("Enter a number: "))

    number = 1

    for x in range(num, 0, -1):
        number *= x

    print("The factorial of", num, "is", number)

def code_challenge7():
    print("Odd Numbers Summation")

    odd_numbers = []
    sum_of_odds = 0


    for i in range(10):
        num = int(input("Enter a Number: "))
        if num % 2 != 0:
            odd_numbers.append(num)
            sum_of_odds += num

    print("Odd numbers:", odd_numbers)
    print("Sum of odd numbers:", sum_of_odds)

def code_challenge8():
    print ("MULTIPLICATION TABLE MAKER")


    num = eval(input("Enter a number: "))

    print ("Multiplication table for", num,":")
    for i in range (1, 11):
        print (num, "x", i, "=", num * i)

def code_challenge9():
    print("COUNTDOWN TIMER SIMULATOR")
    time = eval(input("Enter the starting number for countdown:"))

    print("Countdown started:")
    for i in range(time, 0, -1):
        print(i)
    print("Liftoff!")

def code_challenge10():
    print("\t\t")
    for w in range (1,11,1):
        for x in range (10,w,-1):
            print("", end=" ")
        for y in range (1,w,1):
            print("*",end=" ")
        for z in range (1,w,1):
            print("",end=" ")
        print()

def code_challenge11():   
    for w in range (1,11):
        for x in range (10,w,-1):
            print(" ", end="")
        for y in range (1,w,1):
            print("*",end="")
        for z in range (1,w,1):
            print("*",end="")
        print()
    for a in range (9,0,-1):
        for b in range (10,a,-1):
            print(" ", end="")
        for c in range (1,a,1):
            print("*",end="")
        for d in range (1, a,1):
            print("*",end="")
        print()

def code_challenge12(): 
    for w in range (1,7):
        for x in range (7,w,-1): 
            print(" ",end=" ")
        for y in range(w,0,-1): 
            print(y,end=" ")
        for z in range (1,w,1):
            print(z+1,end=" ")
        print()

def code_challenge13():
    for i in range(1, 5, 1):
        for x in range(19, i, -1):
            print("",end=" ")
        for z in range(1,i,-1):
            print("*", end = " ")
        for y in range(0, i, 1):
            print("*", end= " ")
        print()
    for i in range(5, 0, -1):                
        for x in range(19, i, -1):
            print(" ", end="")
        for z in range(1, i, -1):
            print("*", end=" ")
        for y in range(0, i, 1):
            print("*", end=" ")
        print()
    for i in range(1, 11, 1):
        for y in range(10, i, -1):
            print(" ", end=" ")
        for x in range(1, i, 1):
            print("*", end=" ")
        for z in range(0, i, 1):
            print("*", end=" ")
        print()
    for i in range(1, 11, 1):
        for y in range(10, i, -1):
            print(" ", end=" ")
        for x in range(1, i, 1):
            print("*", end=" ")
        for z in range(0, i, 1):
            print("*", end=" ")
        print()
    for i in range(1, 11, 1):
        for y in range(10, i, -1):
            print(" ", end=" ")
        for x in range(1, i, 1):
            print("*", end=" ")
        for z in range(0, i, 1):
            print("*", end=" ")
        print()
    for i in range(4):  
        for y in range(8):  
            print(" ", end=" ")
        for x in range(3):  
            print("*", end=" ")
        print()

def code_challenge14():
    name = input("What is your name?:")
    print("++++++++++++++++++++++++++++")
    print("ODD number compiler, type '0' to terminate the loop")

    sum = 0
    odd = ""
    number = True

    while number == True:
        num = eval(input("Enter a number:"))
    
        if num % 2 == 1:
            print("ODD number detected")
            odd += str(num) + ","
            sum += num
            continue  
        elif num == 0:
            print("Loop is Terminated")
            break
        else:
            if num % 2 == 0:
                print("EVEN number detected")   
            else:
                print("Invalid Number")
                continue
    print(f"Hi {name} the sum of all ODD number is {sum}")
    print(f"All the ODD numbers you input is {odd}")

def code_challenge15():
    anime_list = []
    while True:
        anime = input("Enter the Title of an Anime (or type 'exit' to finish): ").capitalize()
        if anime== "Exit":
            print("You have Exited the Anime Program")
            break
        else: 
            anime_list.append(anime)   
            print(f"{anime} has been added to your list.")
    print("Your Anime List:")
    for title in anime_list:
        print(f"-{title}")

def code_challenge16():
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

name = input("Hi, Whats your Name?:\t").capitalize()
while True:
    print(f"\n\nWelcome {name} to my Code Compiler.\nSelect a program section you want to run:")
    x = input("A - Activity 1-5\nB - Activity 6-10\nC - Activity 11-15\nD - Activity 16-20\nE - Activity 21-25\nF - Activity 26-27\nG - Code Challenge 1-5\nH - Code Challenge 6-10\nI - Code Challenge 11-16\nX - Exit Program\nType Here:\t").capitalize()
    if x == "A":
        y = input("\n\nSelected Section A:\nA - Activity 1\nB - Activity 2\nC - Activity 3\nD - Activity 4\nE - Activity 5\nType Here:\t").upper()
        if y == "A":
            print("---------------------")
            print("Prints Hello World\n")
            print("---------------------")
            activity1()
        elif y == "B":
            print("---------------------")
            print("Input and Output.\n")
            print("---------------------")
            activity2()
        elif y == "C":
            print("---------------------")
            print("Escape Sequences.(\\t\\n)\n")
            print("---------------------")
            activity3()
        elif y == "D":
            print("---------------------")
            print("Length Function.\n")
            print("---------------------")
            activity4()
        elif y == "E":
            print("---------------------")
            print("Data Types.\n")
            print("---------------------")
            activity5()         
        else:
            print("Please Select within the options")
    elif x == "B":
        y = input("\n\nSelected Section B:\nA - Activity 6\nB - Activity 7\nC - Activity 8\nD - Activity 9\nE - Activity 10\nType Here:\t").upper()
        if y == "A":
            print("---------------------")
            print("Arithmetic Operators.\n")
            print("---------------------")
            activity6()
        elif y == "B":
            print("---------------------")
            print("Assignment Operators.\n")
            print("---------------------")
            activity7()
        elif y == "C":
            print("---------------------")
            print("Comparison Operators.\n")
            print("---------------------")
            activity8()
        elif y == "D":
            print("---------------------")
            print("Logical Operators.\n")
            print("---------------------")
            activity9()
        elif y == "E":
            print("----------------------")
            print("Conditional Statements.\n")
            print("----------------------")
            activity10()
        else:
            print("Please Select within the options")
    elif x == "C":
        y = input("\n\nSelected Section C:\nA - Activity 11\nB - Activity 12\nC - Activity 13\nD - Activity 14\nE - Activity 15\nType Here:\t").upper()
        if y == "A":
            print("-----------------------------------------")
            print("Conditional Statements and Elif Function.\n")
            print("-----------------------------------------")
            activity11()
        elif y == "B":
            print("---------------------")
            print("For Loop Function.\n")
            print("---------------------")
            activity12()
        elif y == "C":
            print("----------------------------")
            print("Using For Loop in Summation.\n")
            print("----------------------------")
            activity13()
        elif y == "D":
            print("---------------------")
            print("For Loop, Descending.\n")
            print("---------------------")
            activity14()
        elif y == "E":
            print("---------------------")
            print("For Loop with input.\n")
            print("---------------------")
            activity15()
        else:
            print("Please Select within the options")
    elif x == "D":
        y = input("\n\nSelected Section D:\nA - Activity 16\nB - Activity 17\nC - Activity 18\nD - Activity 19\nE - Activity 20\nType Here:\t").upper()
        if y == "A":
            print("-------------------------------------")
            print("Using For Loop to print horizontally.\n")
            print("-------------------------------------")
            activity16()
        elif y == "B":
            print("---------------------")
            print("Nested For Loop\n")
            print("---------------------")
            activity17()
        elif y == "C":
            print("---------------------------------")
            print("Nested For Loop(Number Triangle).\n")
            print("---------------------------------")
            activity18()
        elif y == "D":
            print("--------------------------------")
            print("Nested For Loop.(Star Triangle).\n")
            print("--------------------------------")
            activity19()
        elif y == "E":
            print("-----------------------------------")
            print("Nested For Loop(Inverted Triangle).\n")
            print("-----------------------------------")
            activity20()
        else:
            print("Please Select within the options")
    elif x == "E":
        y = input("\n\nSelected Section E:\nA - Activity 21\nB - Activity 22\nC - Activity 23\nD - Activity 24\nE - Activity 25\nType Here:\t").upper()
        if y == "A":
            print("----------------------------")
            print("While Loop(Washing Machine).\n")
            print("----------------------------")
            activity21()
        elif y == "B":
            print("--------------------------")
            print("While Loop(Guessing Game).\n")
            print("--------------------------")
            activity22()
        elif y == "C":
            print("---------------------")
            print("Lists.\n")
            print("---------------------")
            activity23()
        elif y == "D":
            print("---------------------")
            print("Functions.\n")
            print("---------------------")
            activity24()
            print("---------------------")
            print("From, Import.")
            print("---------------------")
            activity24_1()
        elif y == "E":
            print("---------------------")
            print("Activity Compiler.")
            print("---------------------")
            activity25()
        else:
            print("Please Select within the options")
    elif x == "F":
        y = input("\n\nSelected Section F:\nA - Activity 26\nB - Activity 27\nType Here:\t").upper()
        if y == "A":
            print("---------------------")
            print("Dictionary.\n")
            print("---------------------")
            activity26()
        elif y == "B":
            print("---------------------")
            print("Dictionary Functions.\n")
            print("---------------------")
            activity27()
        else:
            print("Please Select within the options.")
    elif x == "G":
        y = input("\n\nSelected Section G:\nA - Code Challenge 1\nB - Code Challenge 2\nC - Code Challenge 3\nD - Code Challenge 4\nE - Code Challenge 5\nType Here:\t").upper()
        if y == "A":
            print("------------------------------------------------")
            print("It Prints Your Name Inside Of Asterisks Diamond.")
            print("------------------------------------------------")
            code_challenge1()
        elif y == "B":
            print("-----------------------")
            print("PHP Money Denomination.\n")
            print("-----------------------")
            code_challenge2()
        elif y == "C":
            print("---------------------")
            print("Account Access.\n")
            print("---------------------")
            code_challenge3()
        elif y == "D":
            print("--------------------------")
            print("Number Checker (Even/Odd).\n")
            print("--------------------------")
            code_challenge4()
        elif y == "E":
            print("----------------------------")
            print("Manga Reader Recommendation.")
            print("----------------------------")
            code_challenge5()
        else:
            print("Please Select within the options")
    elif x == "H":    
        y = input("\n\nSelected Section H:\nA - Code Challenge 6\nB - Code Challenge 7\nC - Code Challenge 8\nD - Code Challenge 9\nE - Code Challenge 10\nType Here:\t").upper()
        if y == "A":
            print("---------------------")
            print("Factorial Program.")
            print("---------------------")
            code_challenge6()
        elif y == "B":
            print("-----------------------")
            print("Odd Numbers Summation.\n")
            print("-----------------------")
            code_challenge7()
        elif y == "C":
            print("---------------------------")
            print("Multiplication Table Maker.\n")
            print("---------------------------")
            code_challenge8()
        elif y == "D":
            print("--------------------------")
            print("Countdown Timer Simulator.\n")
            print("--------------------------")
            code_challenge9()
        elif y == "E":
            print("---------------------")
            print("Diamond Pattern.")
            print("---------------------")
            code_challenge10()
        else:
            print("Please Select within the options")
    elif x == "I":    
        y = input("\n\nSelected Section I:\nA - Code Challenge 11\nB - Code Challenge 12\nC - Code Challenge 13\nD - Code Challenge 14\nE - Code Challenge 15\nF - Code Challenge 16\nType Here:\t").upper()
        if y == "A":
            print("---------------------")
            print("Diamond Pattern.")
            print("---------------------")
            code_challenge11()
        elif y == "B":
            print("-----------------------")
            print("Diamond Pattern.\n")
            print("-----------------------")
            code_challenge12()
        elif y == "C":
            print("---------------------------")
            print("Tree Asterisks.\n")
            print("---------------------------")
            code_challenge13()
        elif y == "D":
            print("--------------------------")
            print("Odd Number Compiler.\n")
            print("--------------------------")
            code_challenge14()
        elif y == "E":
            print("---------------------")
            print("Anime List.")
            print("---------------------")
            code_challenge15()
        elif y == "F":
            print("---------------------------")
            print("Student Information System.")
            print("---------------------------")
            code_challenge16()
        else:
            print("Please Select within the options")
    elif x == "X":
        print("----------------") 
        print("Exiting Program.")
        print("----------------")
        break
    else: 
        print("Please Select within the options")