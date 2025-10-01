
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