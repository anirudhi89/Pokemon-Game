def choosePkmn():
    #letting user pick from list of available pokemon (one from each region)
    pokemonlistKanto = ["Bulbasaur" , "Charmander", "Squirtle"]
    pokemonlistJohto = ["Chikorita" , "Cyndaquil", "Totodile"]
    pokemonlistSinnoh = ["Turtwig", "Chimchar", "Piplup"]

    listOfList = []
    listOfList.append(pokemonlistKanto)
    listOfList.append(pokemonlistJohto)
    listOfList.append(pokemonlistSinnoh)

    #since we need to prompt the user three times, making a counter variable
    counter = 1
    chosenKanto = False 
    chosenJohto = False
    chosenSinnoh = False

    #empty list of all three of the player's pokemon
    playerspokemon = []
    PickThree = 1000 #index of pokemon
    for i in listOfList:
        if (str(i) == str(pokemonlistKanto)):
            print("Pick a Kanto Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            print("#1" , i[0])
            print("#2" , i[1])
            print ("#3" , i[2])
            PickThree = int(input("\nPick a Pokemon to use in battle! "))
            if PickThree > 3:
                print("error - pick a pokemon from this list")
            print("You have chosen " + i[PickThree - 1])
            playerspokemon.append(pokemonlistKanto[PickThree - 1])
            print("Your current pokemon are: ", playerspokemon, "\n")
            chosenKanto = True
            PickThree = 0
        elif str(i) == str(pokemonlistJohto):
            print("Pick a Johto Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            print("#1" , i[0])
            print("#2" , i[1])
            print ("#3" , i[2])
            PickThree = int(input("\nPick a Pokemon to use in battle! "))
            if PickThree > 3:
                print("error - pick a pokemon from this list")
            print("You have chosen " + i[PickThree - 1])
            playerspokemon.append(pokemonlistJohto[PickThree - 1])
            print("Your current pokemon are: ", playerspokemon, "\n")
            chosenJohto = True
            PickThree = 0
            counter += 1
        elif str(i) == str(pokemonlistSinnoh):
            print("Pick a Sinnoh Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            print("#1" , i[0])
            print("#2" , i[1])
            print ("#3" , i[2])
            PickThree = int(input("\nPick a Pokemon to use in battle! "))
            if PickThree > 3:
                print("error - pick a pokemon from this list")
            print("You have chosen " + i[PickThree - 1])
            playerspokemon.append(pokemonlistSinnoh[PickThree - 1])
            print("Your current pokemon are: ", playerspokemon, "\n")
            chosenSinnoh = True
            PickThree = 0
            counter += 1
        if chosenKanto == True and chosenJohto == True and chosenSinnoh == True:
            print("brek sequence worked")
            break
    print("The Pokemon you chose are: ", playerspokemon)
    print("ended")
choosePkmn()          
            
            
            
            
            
            # while chosenJohto == False:
            #     print("Pick a Johto Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            #     print("#1" , pokemonlistJohto[0])
            #     print("#2" , pokemonlistJohto[1])
            #     print ("#3" , pokemonlistJohto[2])
            #     PickThree = input("\nPick a Pokemon to use in battle! ")
            #     if PickThree > 3:
            #         print("error - pick a pokemon from this list")
            #     print("You have chosen " + pokemonlistKanto[PickThree - 1])
            # playerspokemon.append(pokemonlistKanto[PickThree])
            # chosenJohto = True
            # PickThree = 0
            # counter += 1
            # while chosenSinnoh == False:
            #     print("Pick a Sinnoh Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            #     print("1" , pokemonlist[0])
            #     print("#2" , pokemonlist[1])
            #     print ("#3" , pokemonlist[2])
            #     PickThree = input("\nPick a Pokemon to use in battle! ")
            #     if PickThree > 3:
            #         print("error - pick a pokemon from this list")
            #     print("You have chosen " + pokemonlistKanto[PickThree - 1])
            # playerspokemon.append(pokemonlistKanto[PickThree])
            # chosenSinnoh = True
            # PickThree = 0
            # counter +=1