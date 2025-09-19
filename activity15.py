#APPLYING FORMAT IN FACTORIAL PROGRAM
print("Welcome to the Factorial Program!") 
num = eval(input("Enter a number:"))
number = 1 
for x in range(num,0,-1):
    number *= x
print(f"The Factorial of {num} is number {number}")