#FACTORIAL PROGRAM
print("Welcome to the Factorial Program!")

num = int(input("Enter a number: "))

number = 1

for x in range(num, 0, -1):
    number *= x

print("The factorial of", num, "is", number)
