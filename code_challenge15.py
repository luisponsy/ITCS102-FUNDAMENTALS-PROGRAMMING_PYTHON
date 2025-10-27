anime_list = []
while True:
    anime = input("Enter the Title of an Anime (or type 'exit' to finish): ").capitalize()

    if anime== "Exit":
         print("You have Exited the Anime Program")
         break
    else: 
        anime_list.append(anime)   
        print(f"{anime} has been added to your list.")
    
print("Your Anime List:")
for title in anime_list:
    print(f"-{title}")