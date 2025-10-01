for x in range (3):
    for y in range (1, 5):
        stars = 2 * y - 1 + 2 * x
        print(" "* (6 - y - x )+ "*" * stars)

for z in range (3):
    print(" "* 5 + "||")