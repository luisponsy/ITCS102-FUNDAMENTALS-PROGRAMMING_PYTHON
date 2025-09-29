
for w in range (1,7):
    for x in range (7,w,-1): 
        print(" ",end=" ")
    for y in range(w,0,-1): 
        print(y,end=" ")
    for z in range (1,w,1):
        print(z+1,end=" ")
    print()