def greet(name):\
    print(f"hi {name} kamusta ka na?")

def summation(x):
    sum = 0
    for y in range (x, 0, -1):
        sum += y 
    print(f"The sum of {x} is {sum} ")

greet("Luis")
summation(18)