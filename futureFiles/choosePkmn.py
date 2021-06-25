from gameinit import gameInit


# Choose your 3 pokemon, one from each region
def choosePkmn():
    gameInit()
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
    validInput = False

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
            if PickThree > 3:
                chosenKanto = False
            PickThree = 0
        elif str(i) == str(pokemonlistJohto):
            print("Pick a Johto Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            print("#1" , i[0])
            print("#2" , i[1])
            print ("#3" , i[2])
            PickThree = int(input("\nPick a Pokemon to use in battle! "))
            if PickThree > 3:
                print("error - pick a pokemon from this list")
                continue
            print("You have chosen " + i[PickThree - 1])
            playerspokemon.append(pokemonlistJohto[PickThree - 1])
            print("Your current pokemon are: ", playerspokemon, "\n")
            chosenJohto = True
            if PickThree > 3:
                chosenJohto = False
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
            if PickThree > 3:
                chosenSinnoh = False
            PickThree = 0
            counter += 1
        if chosenKanto is True and chosenJohto is True and chosenSinnoh is True:
            break
    print("The Pokemon you chose are: ", playerspokemon)
    print("ended")
            
            
    mybattlepoke = '' #empty string, represents the pokemon used at the battle
    pokeindex = 5

    while pokeindex > 2:
        pokeindex = int(input(
            "\nNow pick ONE of these to use in battle: " + "#1 " + playerspokemon[0] + ", " + "#2 " + playerspokemon[
                1] + ", and " + "#3 " + playerspokemon[2] +
            ". Enter the number... "))
        if pokeindex == 1:
            mybattlepoke = playerspokemon[0]
        elif pokeindex == 2:
            mybattlepoke = playerspokemon[1]
        elif pokeindex == 3:
            mybattlepoke = playerspokemon[2]
        else:
            print('error : choose one from the list')
            continue
        print(mybattlepoke)
        print(pokeindex)
    print("You have picked... " + mybattlepoke + "! Best of luck!")
    # self.remainingpokemonlist = pokemonlist
    # self.battlepokeuser = mybattlepoke

choosePkmn()

