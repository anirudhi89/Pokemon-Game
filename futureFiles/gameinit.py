
def gameInit():
#letting user pick from list of available pokemon (one from each region)
    pokemonlistKanto = ["Bulbasaur" , "Charmander", "Squirtle"]
    pokemonlistJohto = ["Chikorita" , "Cyndaquil", "Totodile"]
    pokemonlistSinnoh = ["Turtwig", "Chimchar", "Piplup"]

    listOfList= []
    listOfList.append(pokemonlistKanto)
    listOfList.append(pokemonlistJohto)
    listOfList.append(pokemonlistSinnoh)


    chosenKanto = False
    chosenJohto = False
    chosenSinnoh = False
    validInput = False

    # empty list of all three of the player's pokemon
    playerspokemon = []
    print("initialized")