def activity3():
    odd_sum = 0
    for i in range(1,11,1):
        num = eval(input("enter a number"))
        if num % 2 ==1:
            odd_sum += 1
        print(f"there are {odd_sum} odd number")