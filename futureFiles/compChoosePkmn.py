import random
from random import *
def compChoose():
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

    '''Copy from here on out'''

    global compKanto
    global compJohto
    global compSinnoh

    compsPkmn = []
    attributeCompPkmn = []

    compbattlepoke = ''  # empty string, represents the pokemon used at the battle

    for i in totalPkmn:
        if (str(i) == str(pokemonlistKanto)):
            k = randint(0,2)
            compsPkmn.append(pokemonlistKanto[k].get('Name'))
            attributeCompPkmn.append(pokemonlistKanto[k])
            compKanto = True
        elif (str(i) == str(pokemonlistJohto)):
            j = randint(0,2)
            compsPkmn.append(pokemonlistJohto[j].get('Name'))
            attributeCompPkmn.append((pokemonlistJohto[j]))
            compJohto = True
        elif (str(i) == str(pokemonlistSinnoh)):
            s = randint(0,2)
            compsPkmn.append(pokemonlistSinnoh[s].get('Name'))
            attributeCompPkmn.append(pokemonlistSinnoh[s])
            compSinnoh = True
    print("The opponent's Pokemon are", compsPkmn)

    i = randint(0,2)
    compbattlepoke = compsPkmn[i]
    print(f"The opponent chose {compbattlepoke}")


compChoose()