import random

x = random.randint(1,10)
while True:
    y = eval(input("Guess the number!(1 - 10):"))
    if y == x:
        print(f"Number: {y} You Win!")
        break
    else:
        print("Incorrect Number, Try Again!")  
  