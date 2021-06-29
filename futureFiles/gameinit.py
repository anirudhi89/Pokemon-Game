
def gameInit():
    # add a dictionary for each pokemon's properties: of name, type, hp, attack, and defesne
    # make HP, Attack and Defense all add up to 150 for simplicity
    # ie:

    # Kanto
    Bulbasaur = {'Name': 'Bulbasaur', 'Type': 'Grass', 'HP': 50, 'Attack': 48, 'Defense': 52}
    Charmander = {'Name': 'Charmander', 'Type': 'Fire', 'HP': 55, 'Attack': 46, 'Defense': 49}
    Squirtle = {'Name': 'Squirtle', 'Type': 'Water', 'HP': 48, 'Attack': 52, 'Defense': 50}

    # Johto
    Chikorita = {'Name': 'Chikorita', 'Type': 'Grass', 'HP': 50, 'Attack': 48, 'Defense': 52}
    Cyndaquil = {'Name': 'Cyndaquil', 'Type': 'Fire', 'HP': 55, 'Attack': 46, 'Defense': 49}
    Totodile = {'Name': 'Totodile', 'Type': 'Water', 'HP': 48, 'Attack': 52, 'Defense': 50}

    # Sinnoh
    Turtwig = {'Name': 'Turtwig', 'Type': 'Grass', 'HP': 50, 'Attack': 48, 'Defense': 52}
    Chimchar = {'Name': 'Chimchar', 'Type': 'Fire', 'HP': 55, 'Attack': 46, 'Defense': 49}
    Piplup = {'Name': 'Piplup', 'Type': 'Water', 'HP': 48, 'Attack': 52, 'Defense': 50}

    # List
    pokemonlistKanto = [Bulbasaur, Charmander, Squirtle]
    pokemonlistJohto = [Chikorita, Cyndaquil, Totodile]
    pokemonlistSinnoh = [Turtwig, Chimchar, Piplup]

    totalPkmn = []
    totalPkmn.append(pokemonlistKanto)
    totalPkmn.append(pokemonlistJohto)
    totalPkmn.append(pokemonlistSinnoh)

    # since we need to prompt the user three times, making a counter variable
    global chosenKanto
    global chosenJohto
    global chosenSinnoh
    chosenKanto = False
    chosenJohto = False
    chosenSinnoh = False


    # empty list of all three of the player's pokemon
    playerspokemon = []
    attributeplayerpoke = []
    global PickThree
    PickThree = 1000  # index of pokemon
    print("initialized")

    global compKanto
    global compJohto
    global compSinnoh

    compsPkmn = []
    attributeCompPkmn = []

    compbattlepoke = ''  # empty string, represents the pokemon used at the battle