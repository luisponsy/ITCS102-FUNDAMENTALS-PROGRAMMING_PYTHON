print("\t\t")
for w in range (1,11,1):
    for x in range (10,w,-1):
        print("", end=" ")
    for y in range (1,w,1):
        print("*",end=" ")
    for z in range (1,w,1):
        print("",end=" ")
    print()