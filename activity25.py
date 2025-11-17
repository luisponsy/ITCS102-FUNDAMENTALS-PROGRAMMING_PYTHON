from activity25_1 import *
from activity25_2 import *

name = input("Hi, What is your name?:")

print(f"Welcome {name}, to my Compiler Program")

isContinue = True

while isContinue == True:
    print("Select a Program")
    print("A - Activity1\nB - Activity2\nC - Activity3\nE - Exit")

    choose = input("What program/code would you like to run?: ").lower()

    if choose == 'a':
        activity1()
        continue
    elif choose == 'b':
        activity2()
        continue
    elif choose == 'c':
        activity3()
        continue
    elif choose == 'd':
        pass
        continue
    elif choose == 'e':
        print("System Exit. ")
        break
    else:
        print("Invalid Option.")