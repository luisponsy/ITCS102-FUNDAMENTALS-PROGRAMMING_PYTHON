print("Welcome to Manga Reader Recommendation!")

print("Please select a genre:")
genre = input("1. Romance\n2. Comedy\n3. Action\nEnter the number of your choice: ")

print("\nWhat is your preferred manga length?")
length = input("1. Short\n2. Medium\n3. Long\nEnter the number of your choice: ")

print("\nWhich decade do you prefer?")
decade = input("1. 2000s\n2. 2010s\nEnter the number of your choice: ")

if genre == "1":
    if length == "1":  
        if decade == "1":
            print("\nRecommendation: Lovely Complex (2000s)")
        else:
            print("\nRecommendation: Kimi ni Todoke (2010s)")
    elif length == "2":  
        if decade == "1":
            print("\nRecommendation: Fruits Basket (2000s)")
        else:
            print("\nRecommendation: My Little Monster (2010s)")
    else:  
        if decade == "1":
            print("\nRecommendation: Nana (2000s)")
        else:
            print("\nRecommendation: Your Lie in April (2010s)")

elif genre == "2":  
    if length == "1":  
        if decade == "1":
            print("\nRecommendation: Azumanga Daioh (2000s)")
        else:
            print("\nRecommendation: Barakamon (2010s)")
    elif length == "2":  
        if decade == "1":
            print("\nRecommendation: One Punch Man (2000s)")
        else:
            print("\nRecommendation: Gintama (2010s)")
    else:  
        if decade == "1":
            print("\nRecommendation: One Piece (2000s)")
        else:
            print("\nRecommendation: KonoSuba (2010s)")

elif genre == "3":  
    if length == "1": 
        if decade == "1":
            print("\nRecommendation: Death Note (2000s)")
        else:
            print("\nRecommendation: Attack on Titan (2010s)")
    elif length == "2":  
        if decade == "1":
            print("\nRecommendation: Naruto (2000s)")
        else:
            print("\nRecommendation: Demon Slayer (2010s)")
    else:  
        if decade == "1":
            print("\nRecommendation: Bleach (2000s)")
        else:
            print("\nRecommendation: My Hero Academia (2010s)")
else:
    print("Invalid input.")