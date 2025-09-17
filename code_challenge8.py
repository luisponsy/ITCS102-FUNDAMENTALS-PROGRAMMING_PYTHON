print ("MULTIPLICATION TABLE MAKER")


num = eval(input("Enter a number: "))

print ("Multiplication table for", num,":")
for i in range (1, 11):
    print (num, "x", i, "=", num * i)

